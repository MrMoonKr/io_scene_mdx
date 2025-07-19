import os

import bpy
import bpy_extras

from .classes.MDXImportProperties import MDXImportProperties
from .mdx_parser.load_mdx import load_mdx
from .mdl_parser.load_mdl import load_mdl
from . import constants
from . import utils



class WarCraft3OperatorImportMDX( bpy.types.Operator, bpy_extras.io_utils.ImportHelper ):
    '''
        WarCraft 3 Import MDX/MDL Operator
    '''
    
    bl_idname       = 'warcraft_3.import_mdl_mdx'
    bl_label        = 'Import *.mdl/*.mdx'
    bl_description  = 'Import *.mdl/*.mdx files (3d models of WarCraft 3)'
    bl_options      = {'UNDO'}

    filename_ext    = ['.mdx', '.mdl']
    filter_glob: bpy.props.StringProperty( 
        default='*.mdx;*.mdl',
        options={'HIDDEN'}
        ) # type: ignore
    filepath: bpy.props.StringProperty( 
        name='File Path',
        maxlen=1024,
        default='' 
        ) # type: ignore
    useCustomFPS: bpy.props.BoolProperty(
        name='Use Custom FPS',
        default=False 
        ) # type: ignore
    animationFPS: bpy.props.FloatProperty(
        name='Animation FPS',
        default=30.0,
        min=1.0, max=1000.0
        ) # type: ignore
    boneSize: bpy.props.FloatProperty(
        name='Bone Size',
        default=5.0,
        min=0.0001, max=1000.0
        ) # type: ignore
    teamColor: bpy.props.FloatVectorProperty(
        name='Team Color',
        default=constants.TEAM_COLORS['RED'],
        min=0.0,
        max=1.0,
        size=3,
        subtype='COLOR',
        precision=3
        ) # type: ignore
    setTeamColor: bpy.props.EnumProperty(
        items=[
            ('RED', 'Red', ''),
            ('DARK_BLUE', 'Dark Blue', ''),
            ('TURQUOISE', 'Turquoise', ''),
            ('VIOLET', 'Violet', ''),
            ('YELLOW', 'Yellow', ''),
            ('ORANGE', 'Orange', ''),
            ('GREEN', 'Green', ''),
            ('PINK', 'Pink', ''),
            ('GREY', 'Grey', ''),
            ('BLUE', 'Blue', ''),
            ('DARK_GREEN', 'Dark Green', ''),
            ('BROWN', 'Brown', ''),
            ('BLACK', 'Black', '')
        ],
        name='Set Team Color',
        update=utils.set_team_color_property,
        default='RED'
        ) # type: ignore

    def draw( self, context ):
        layout = self.layout
        
        split = layout.split( factor=0.9 )
        sub_split = split.split( factor=0.5 )
        sub_split.label( text='Team Color:' )
        sub_split.prop( self, 'setTeamColor', text='' )
        split.prop( self, 'teamColor', text='' )
        
        layout.prop( self, 'boneSize' )
        layout.prop( self, 'useCustomFPS' )
        if self.useCustomFPS:
            layout.prop( self, 'animationFPS' )

    def execute( self, context ):
        import_properties = MDXImportProperties()
        import_properties.mdx_file_path = self.filepath
        import_properties.team_color = self.setTeamColor
        import_properties.bone_size = self.boneSize
        import_properties.use_custom_fps = self.useCustomFPS
        import_properties.fps = self.animationFPS
        import_properties.calculate_frame_time()
        #constants.os_path_separator = os.path
        if ".mdl" in self.filepath:
            load_mdl( import_properties )
        else:
            load_mdx( import_properties )
            
        return {'FINISHED'}

    def invoke( self, context, event ):
        context.window_manager.fileselect_add( self )
        return {'RUNNING_MODAL'}


class WarCraft3OperatorAddSequenceToArmature( bpy.types.Operator ):
    '''
    '''
    
    bl_idname       = 'warcraft_3.add_sequence_to_armature'
    bl_label        = 'Warcraft 3 Add Sequence to Armature'
    bl_description  = 'Warcraft 3 Add Sequence to Armature'
    bl_options      = {'UNDO'}

    def execute( self, context ):
        if context.armature:
            warcraft3data   = context.armature.warcraft_3
            sequence        = warcraft3data.sequencesList.add()
            sequence.name   = '#UNANIMATED'
        return {'FINISHED'}


class WarCraft3OperatorRemoveSequenceToArmature( bpy.types.Operator ):
    '''
    '''
    
    bl_idname       = 'warcraft_3.remove_sequence_to_armature'
    bl_label        = 'Warcraft 3 Remove Sequence to Armature'
    bl_description  = 'Warcraft 3 Remove Sequence to Armature'
    bl_options      = {'UNDO'}

    def execute( self, context ):
        if context.armature:
            warcraft3data   = context.armature.warcraft_3
            warcraft3data.sequencesList.remove( warcraft3data.sequencesListIndex )
        return {'FINISHED'}


class WarCraft3OperatorUpdateBoneSettings( bpy.types.Operator ):
    '''
    '''
    
    bl_idname       = 'warcraft_3.update_bone_settings'
    bl_label        = 'Warcraft 3 Update Bone Settings'
    bl_description  = 'Warcraft 3 Update Bone Settings'
    bl_options      = {'UNDO'}

    def execute( self, context ):
        object = context.object
        for bone in object.data.bones:
            nodeType    = bone.warcraft_3.nodeType
            boneGroup   = object.pose.bone_groups.get( nodeType.lower() + 's', None )
            if not boneGroup:
                if nodeType in {'BONE', 'ATTACHMENT', 'COLLISION_SHAPE', 'EVENT', 'HELPER'}:
                    bpy.ops.pose.group_add()
                    boneGroup = object.pose.bone_groups.active
                    boneGroup.name = nodeType.lower() + 's'
                    if nodeType == 'BONE':
                        boneGroup.color_set = 'THEME04'
                    elif nodeType == 'ATTACHMENT':
                        boneGroup.color_set = 'THEME09'
                    elif nodeType == 'COLLISION_SHAPE':
                        boneGroup.color_set = 'THEME02'
                    elif nodeType == 'EVENT':
                        boneGroup.color_set = 'THEME03'
                    elif nodeType == 'HELPER':
                        boneGroup.color_set = 'THEME01'
                else:
                    boneGroup = None
            object.pose.bones[bone.name].bone_group = boneGroup
        return {'FINISHED'}
