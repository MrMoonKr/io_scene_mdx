import bpy
from bpy.types import PropertyGroup
from . import utils


class WarCraft3ArmatureSequenceList( PropertyGroup ):
    '''
        A Sequence Name of Armature
        '''
    name: bpy.props.StringProperty() # type: ignore


class WarCraft3ArmatureProperties( PropertyGroup ):
    '''
        Sequence Name List and Current Sequence Index of Armature
        '''
    bpy_type = bpy.types.Armature
    
    sequencesList: bpy.props.CollectionProperty( type=WarCraft3ArmatureSequenceList ) # type: ignore
    sequencesListIndex: bpy.props.IntProperty( 
        #update=utils.set_animation
        ) # type: ignore


class WarCraft3BoneProperties( PropertyGroup ):
    '''
        WarCraft 3 Bone Properties  
        This class defines the properties for bones in a WarCraft 3 armature.
        '''
    bpy_type = bpy.types.Bone
    
    nodeType: bpy.props.EnumProperty( # type: ignore
        items=[
            ('NONE', 'None', ''),
            ('BONE', 'Bone', ''),
            ('HELPER', 'Helper', ''),
            ('ATTACHMENT', 'Attachment', ''),
            ('EVENT', 'Event', ''),
            ('COLLISION_SHAPE', 'Collision Shape', '')
        ],
        name='Node Type',
        default='NONE'
        #update=utils.set_bone_node_type,
    )
