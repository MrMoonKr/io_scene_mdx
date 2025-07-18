import bpy


class WarCraft3PanelArmature( bpy.types.Panel ):
    '''
        WarCraft 3 Armature Panel
        This panel is used to manage WarCraft 3 sequences in the armature properties.
        It allows users to add and remove sequences, and displays a list of existing sequences.
        It is accessible in the Armature properties tab when an armature is selected.
        The panel is registered under the 'PROPERTIES' space type and 'data' context.
        It provides a user-friendly interface for managing animations specific to WarCraft 3 models.
        It includes a list of sequences with options to add or remove them.
        The sequences are stored in the armature's custom property `warcraft_3`.
        This panel is part of the WarCraft 3 Blender add-on, which enhances the functionality
        of Blender for importing and exporting WarCraft 3 models and animations.
        It is designed to work with the WarCraft 3 model format, allowing users to create
        and edit animations that are compatible with the game.
    '''
    bl_idname           = 'WC3_PT_armature_panel'
    bl_label            = 'WarCraft 3'
    bl_space_type       = 'PROPERTIES'
    bl_region_type      = 'WINDOW'
    bl_context          = 'data'

    @classmethod
    def poll( cls, context ):
        return context.armature

    def draw( self, context ):
        warcraft3data   = context.armature.warcraft_3
        layout          = self.layout
        
        layout.label( text='Animations:' )
        
        row = layout.row()
        row.template_list(
            listtype_name='UI_UL_list',
            list_id='name',
            dataptr=warcraft3data,
            propname='sequencesList',
            active_dataptr=warcraft3data,
            active_propname='sequencesListIndex',
            rows=2
            )
        col = row.column( align=True )
        col.operator( 'warcraft_3.add_sequence_to_armature', icon='ADD', text='' )
        col.operator( 'warcraft_3.remove_sequence_to_armature', icon='REMOVE', text='' )


class WarCraft3PanelBone( bpy.types.Panel ):
    '''

    '''
    bl_idname           = 'WC3_PT_bone_panel'
    bl_label            = 'WarCraft 3'
    bl_space_type       = 'PROPERTIES'
    bl_region_type      = 'WINDOW'
    bl_context          = 'bone'

    @classmethod
    def poll( cls, context ):
        return context.bone

    def draw( self, context ):
        bone            = context.bone
        warcraft3data   = bone.warcraft_3
        layout          = self.layout
        
        layout.prop( warcraft3data, 'nodeType' )
        if context.object.mode == 'POSE':
            layout.operator(
                'warcraft_3.update_bone_settings',
                text='Update All Nodes'
            )
