from typing import List, Dict, Set

import bpy
from bpy.types import Object, Armature, ArmatureEditBones

from ..classes.WarCraft3Model import WarCraft3Model
from ..classes.WarCraft3Node import WarCraft3Node


def create_armature_object( model: WarCraft3Model, bpy_mesh_objects: list[Object], bone_size: float ) -> Object:
    """
        blender armature 생성.  
        """
        
    print( "[io_scene_mdx] creating armature" )
    
    nodes: list[WarCraft3Node]      = model.nodes
    pivot_points: list[list[float]] = model.pivot_points
    
    # Armature Object 생성
    
    bpy_armature_object: Object     = get_bpy_armature_object( model.name + ' Armature' )
    bpy_armature: Armature          = bpy_armature_object.data
    # bpy_armature.display_type = 'STICK'
    
    # Armature에 EditBone들 생성

    bone_types                      = get_bone_type_dict( bone_size, bpy_armature.edit_bones, nodes, pivot_points )
    # bone_types = add_and_get_node_bone_dict( bone_size, bpy_armature.edit_bones, nodes, pivot_points )

    print( bpy_armature_object.data.edit_bones[0] )

    # EditBone의 부모 EditBone 연결
    for indexNode, node in enumerate( nodes ):
        e_bone = bpy_armature.edit_bones[ indexNode ]
        if node.parent is not None:
            parent = bpy_armature.edit_bones[ node.parent ]
            e_bone.parent = parent
            #e_bone.use_connect = True
            #parent.tail = e_bone.head

    for a_bone in bpy_armature.bones:
        a_bone.warcraft_3.nodeType = bone_types[a_bone.name].upper()

    set_vertex_group_names( bpy_armature, bpy_mesh_objects )

    bpy.ops.object.mode_set( mode='POSE' )
    bone_groups = get_bone_group_dict( bone_types, bpy_armature_object )

    for p_bone in bpy_armature_object.pose.bones:
        p_bone.rotation_mode = 'XYZ'
        #p_bone.bone_group = bone_groups[ bone_types[ p_bone.name ] ]
        #bone_group = bone_groups[ bone_types[ p_bone.name ] ]
        #bone_group.bones.add( p_bone.bone )

    bpy.ops.object.mode_set( mode='OBJECT' )
    bpy.context.active_object.select_set( False )
    
    add_mesh_modifier( bpy_armature_object, bpy_mesh_objects )

    return bpy_armature_object


# def get_bpy_armature_object(bpy_armature1: bpy.types.Armature, name: str) -> Object:
def get_bpy_armature_object( name: str ) -> Object:
    """
        blender armature 생성 후 EditMode로 전환 후 반환.  
        """
    
    # Armature 생성
    bpy_armature: bpy.types.Armature        = bpy.data.armatures.new( name )
    bpy_armature_object: bpy.types.Object   = bpy.data.objects.new( name, bpy_armature )
    
    # Scene의 Collection내에 등록
    bpy.context.scene.collection.objects.link( bpy_armature_object )
    
    # 'Edit' 모드 전환
    bpy_armature_object.select_set( True )
    # bpy_armature_object.show_in_front = True
    # bpy_armature_object.mode = 'EDIT'
    bpy.context.view_layer.objects.active = bpy_armature_object
    # bpy.context.scene.objects.active = bpy_armature_object
    bpy.ops.object.mode_set( mode='EDIT' )
    
    return bpy_armature_object


def add_mesh_modifier( bpy_armature_object: Object, bpy_mesh_objects: list[Object] ):
    """
        Mesh오브젝트에 Armature모디파이어 등록
        """
    for mesh in bpy_mesh_objects:
        mesh.modifiers.new( name='Armature', type='ARMATURE' )
        mesh.modifiers['Armature'].object = bpy_armature_object


def set_vertex_group_names( bpy_armature: bpy.types.Armature, 
                            bpy_mesh_objects: list[bpy.types.Object] ):
    '''
        메시오브젝트의 정점그룹 이름 교정.  
        '''
    for mesh in bpy_mesh_objects:
        for vertexGroup in mesh.vertex_groups:
            vertex_group_index  = int( vertexGroup.name )
            bone_name           = bpy_armature.edit_bones[vertex_group_index].name
            vertexGroup.name    = bone_name


def get_bone_group_dict( node_to_bone: dict[WarCraft3Node, bpy.types.EditBone],
                         bpy_armature_object: Object ) :
    """
        BoneGruops 룩업테이블 구성.   
        BoneGroup은 같은 색깔로 표시되는 Bone Collection임.
        """
    bone_groups = {}
    # node_types = collect_node_types(bone_types)
    node_types: list[str] = []
    
    # 노드타입들 추출
    for index, node in enumerate( node_to_bone ):
        if node.node_type not in node_types:
            node_types.append( node.node_type )
    node_types.sort()

    for nodeType in node_types:
        bone_group = get_new_bone_group( nodeType, bpy_armature_object.pose.bone_groups )
        bone_groups[nodeType] = bone_group
        
    return bone_groups


def get_bone_group_dict( bone_types: dict[str, str], bpy_armature_object: Object ) -> dict[str,bpy.types.BoneCollection]:
    '''
        (본이름, 본타입) -> Armature 본 이름 수정.  
        '''
    bone_groups = {}
    # node_types = collect_node_types(bone_types)

    node_types: list[str] = [] # 노드 타입들 목록
    for index, b_name in enumerate( bone_types ):
        if bone_types[ b_name ] not in node_types:
            node_types.append( bone_types[ b_name ] )
    node_types.sort()

    for nodeType in node_types:
        bone_group              = get_new_bone_group( nodeType, bpy_armature_object.data.collections )
        bone_groups[nodeType]   = bone_group
        
    return bone_groups


def get_bone_type_dict( bone_size: float,
                        edit_bones: ArmatureEditBones,
                        nodes: list[WarCraft3Node],
                        pivot_points: list[list[float]] 
                        ) -> dict[str, str]:
    """
        W3Node에 해당하는 EditBone 생성 후 룩업테이블( 본이름, 노드타입 )로 반환
        """
    bone_types: dict[str, str] = {}
    
    for nodeIndex, node in enumerate( nodes ):
        node_position   = pivot_points[ nodeIndex ]
        bone_name       = node.name
        if bone_name in bone_types.keys():
            bone_name   = bone_name + ".001"
            if bone_name in bone_types.keys():
                bone_name = bone_name + ".002"
            node.name   = bone_name
            
        bone_parent = node.parent
        node_parent: WarCraft3Node = None
        if bone_parent is not None: 
            node_parent = nodes[ bone_parent ]

        print( "노드이름 : ( " + str(nodeIndex) + " ) "  + node.name + ", 부모 : " + str( bone_parent ) )
            
        bone            = edit_bones.new( bone_name )
        bone.head       = node_position
        bone.tail       = node_position
        #bone.tail[0]    += bone_size
        bone.tail[1]    += bone_size
        #bone.tail[2]    += bone_size

        
        bone_types[bone_name] = node.node_type

    return bone_types


def add_and_get_node_bone_dict( bone_size: float,
                                edit_bones: bpy.types.ArmatureEditBones,
                                nodes: List[WarCraft3Node],
                                pivot_points: List[List[float]] 
                                ) -> dict[WarCraft3Node, bpy.types.EditBone]:
    """
        W3Node에 해당하는 EditBone 생성 후 룩업테이블로 반환
    """
    node_to_bone: dict[WarCraft3Node, bpy.types.EditBone] = {}
    bone_names: set[str] = set()

    for indexNode, node in enumerate( nodes ):
        node_position = pivot_points[ indexNode ]
        
        bone_name = node.name
        if bone_name in bone_names:
            bone_name = bone_name + ".001"
            if bone_name in bone_names:
                bone_name = bone_name + ".002"
            node.name = bone_name
            
        bone_parent = node.parent
            
        bone = edit_bones.new( bone_name )
        bone.head = node_position
        bone.tail = node_position
        # bone.tail[2] += bone_size
        bone.tail[1] += bone_size
        bone_names.add( bone_name )
        
        node_to_bone[ node ] = bone

    return node_to_bone


def collect_node_types( node_to_bone: Dict[WarCraft3Node, bpy.types.EditBone] ) -> List[str]:
    """
        노드타입들 모은다
        """
    node_types: List[str] = []
    
    for index, bone in enumerate( node_to_bone ):
        if bone.node_type not in node_types:
            node_types.append( bone.node_type )
    node_types.sort()
    
    return node_types


def collect_node_types( bone_types: dict[str, str] ) -> list[str]:
    """
        노드의 타입 문자열을 모은다 dict( 노드이름, 노드타입 ) -> list( 노드타입 )
        """
    node_types: list[str] = []
    for index, b_name in enumerate( bone_types ):
        if bone_types[ b_name ] not in node_types:
            node_types.append( bone_types[ b_name ] )
    node_types.sort()
    return node_types


def get_new_bone_group( nodeType: str, bone_groups: bpy.types.BoneCollections ):
    """
        특정 종류의 BoneCollection 조회. 없으면 생성
        """
    bone_group: bpy.types.BoneCollection = bone_groups.get( nodeType + 's' )
    
    if bone_group is None:
        bone_group              = bone_groups.new( name=nodeType + 's' )
        #bone_group.color_set    = get_bone_group_color( nodeType )

    return bone_group


def get_new_bone_group11( nodeType: str, bone_groups: bpy.types.BoneCollections ):
    bone_groups.get( nodeType + 's' )
    bone_group: bpy.types.BoneGroup = bone_groups.new( nodeType + 's' )
    # bone_group: bpy.types.BoneGroup = bpy.types.BoneGroups.new(nodeType + 's')
    # bone_group: bpy.types.BoneGroup = bpy.types.BoneGroup()
    bone_group.color_set = get_bone_group_color(nodeType)
    bone_group.name = nodeType + 's'
    return bone_group


def get_bone_group_color( nodeType: str ) -> str:
    """
        특정 노드타입의 BoneCollection에 사용할 컬러셋 이름 조회
        """
    if nodeType == 'bone':
        return 'THEME04'
    elif nodeType == 'attachment':
        return 'THEME09'
    elif nodeType == 'collision_shape':
        return 'THEME02'
    elif nodeType == 'event':
        return 'THEME03'
    elif nodeType == 'helper':
        return 'THEME01'
    return 'DEFAULT'
