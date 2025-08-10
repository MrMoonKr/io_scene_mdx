
import bpy
from bpy.types import BoneCollection

from .props import WarCraft3ArmatureProperties, WarCraft3ArmatureSequenceList
from . import constants
from mathutils import ( Vector, Matrix, Quaternion, Euler, Color )


ACTION_NAME_UNANIMATED = '#UNANIMATED'


def set_animation( self: bpy.types.bpy_struct, context: bpy.types.Context ) -> None:
    '''
        WarCraft3ArmatureProperties.sequencesListIndex 속성의 update 함수.  
        '''
    warcraft_3: WarCraft3ArmatureProperties = context.armature.warcraft_3
    sequenceList: list[WarCraft3ArmatureSequenceList] = warcraft_3.sequencesList
    sequenceIndex: int = warcraft_3.sequencesListIndex
    sequenceName: str = sequenceList[sequenceIndex].name
    
    set_animation_name = context.armature.warcraft_3.sequencesList[context.armature.warcraft_3.sequencesListIndex].name
    if len( set_animation_name ) and bpy.data.actions.get( set_animation_name, None ):
        prepare_action( context, set_animation_name )
        for action in bpy.data.actions:
            for bpy_object in bpy.context.scene.objects:
                set_object_animation_name = set_animation_name + ' ' + bpy_object.name
                if action.name == set_object_animation_name:
                    if bpy_object.animation_data is None:
                        bpy_object.animation_data_create()
                    bpy_object.animation_data.action = action
    else:
        unanimated = ACTION_NAME_UNANIMATED
        action = bpy.data.actions.get( unanimated, None )
        if action:
            prepare_action( context, unanimated )
            for bpy_object in bpy.context.scene.objects:
                object_action_name = unanimated + ' ' + bpy_object.name
                if bpy.data.actions.get( object_action_name, None ):
                    if bpy_object.animation_data is None:
                        bpy_object.animation_data_create()
                    bpy_object.animation_data.action = bpy.data.actions[ object_action_name ]


def prepare_action( context: bpy.types.Context, action_name: str ) -> None:
    '''
        액션 관련 데이터 생성
        '''
    armature_object = context.object
    if armature_object.animation_data is None:
        armature_object.animation_data_create()
        
    set_action = bpy.data.actions[action_name]
    armature_object.animation_data.action = set_action
    bpy.context.scene.frame_start   = set_action.frame_range[0]
    bpy.context.scene.frame_end     = set_action.frame_range[1]


def set_team_color_property( self, context ):
    '''
        setTeamColor 열거형 변경시 update 콜백 함수
        '''
    self.teamColor = constants.TEAM_COLORS[self.setTeamColor]


def set_bone_node_type( self: bpy.types.bpy_struct, context: bpy.types.Context ) -> None:
    '''
        Set the bone node type and assign it to the appropriate bone group.
        This function checks the active bone's node type and assigns it to a bone group
        based on the node type. If the bone group does not exist, it creates a new
        '''
    bone            = context.active_bone
    if bone:
        node_type   = bone.warcraft_3.nodeType
        bpy_object  = context.object
        #bone_groups: bpy.types.BoneGroups = bpy_object.pose.bone_groups
        bone_collection: BoneCollection = bpy_object.data.collections.get( node_type.lower() + 's', None )
        if not bone_collection:
            if node_type in {'BONE', 'ATTACHMENT', 'COLLISION_SHAPE', 'EVENT', 'HELPER'}:
                #bcollections = bpy_object.data.collections.new( node_type.lower() + 's' )
                if node_type == 'BONE':
                    bone_collection.color_set = 'THEME04'
                elif node_type == 'ATTACHMENT':
                    bone_collection.color_set = 'THEME09'
                elif node_type == 'COLLISION_SHAPE':
                    bone_collection.color_set = 'THEME02'
                elif node_type == 'EVENT':
                    bone_collection.color_set = 'THEME03'
                elif node_type == 'HELPER':
                    bone_collection.color_set = 'THEME01'
            else:
                bone_group = None
        bpy_object.pose.bones[bone.name].bone_group = bone_group
        
        
        bone_group: bpy.types.BoneGroup  = bpy_object.pose.bone_groups.get( node_type.lower() + 's', None )
        if not bone_group:
            if node_type in {'BONE', 'ATTACHMENT', 'COLLISION_SHAPE', 'EVENT', 'HELPER'}:
                bpy.ops.pose.group_add()
                bone_group = bpy_object.pose.bone_groups.active
                bone_group.name = node_type.lower() + 's'
                if node_type == 'BONE':
                    bone_group.color_set = 'THEME04'
                elif node_type == 'ATTACHMENT':
                    bone_group.color_set = 'THEME09'
                elif node_type == 'COLLISION_SHAPE':
                    bone_group.color_set = 'THEME02'
                elif node_type == 'EVENT':
                    bone_group.color_set = 'THEME03'
                elif node_type == 'HELPER':
                    bone_group.color_set = 'THEME01'
            else:
                bone_group = None
        bpy_object.pose.bones[bone.name].bone_group = bone_group
