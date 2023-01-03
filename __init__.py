
bl_info = {
    'name': 'io_scene_mdx',
    'author': 'MrMoonKr & Pavel_Blend & twilac',
    'version': (0, 0, 0),
    'blender': (2, 80, 0),
    'category': 'Development', #'category': 'Import-Export',
    'location': 'File > Import',
    'description': 'Import *.mdl/*.mdx files ( 3d models of WarCraft 3 )',
    'doc_url': 'https://github.com/tw1lac/Blender_WarCraft-3',
    'tracker_url': 'https://github.com/tw1lac/Blender_WarCraft-3/issues'
}


import bpy

from .operators import (
    WarCraft3OperatorImportMDX,
    WarCraft3OperatorAddSequenceToArmature,
    WarCraft3OperatorRemoveSequenceToArmature,
    WarCraft3OperatorUpdateBoneSettings
)

from .ui import (
    WarCraft3PanelBone,
    WarCraft3PanelArmature
)

from .preferences import (
    WarCraft3Preferences
)

from .props import (
    WarCraft3ArmatureSequenceList,
    WarCraft3ArmatureProperties,
    WarCraft3BoneProperties
)


def menu_import_mdx( self, context ):
    self.layout.operator( WarCraft3OperatorImportMDX.bl_idname, text='Warcraft 3 (.mdl/.mdx)' )


wc_classes = (
    WarCraft3OperatorImportMDX,
    WarCraft3OperatorAddSequenceToArmature,
    WarCraft3OperatorRemoveSequenceToArmature,
    WarCraft3OperatorUpdateBoneSettings,
    WarCraft3PanelBone,
    WarCraft3PanelArmature,
)

prop_classes = (
    WarCraft3Preferences,
    WarCraft3ArmatureSequenceList,
    WarCraft3ArmatureProperties,
    WarCraft3BoneProperties
)


def register():
    print( "io_scene_mdx register() called" )
    
    for cls in prop_classes:
        bpy.utils.register_class( cls )
        
    WarCraft3ArmatureProperties.bpy_type.warcraft_3 = bpy.props.PointerProperty(type=WarCraft3ArmatureProperties)
    WarCraft3BoneProperties.bpy_type.warcraft_3 = bpy.props.PointerProperty(type=WarCraft3BoneProperties)

    for cls in wc_classes:
        bpy.utils.register_class( cls )
        
    bpy.types.TOPBAR_MT_file_import.append( menu_import_mdx )

def unregister():
    print( "io_scene_mdx unregister called" )
    
    bpy.types.TOPBAR_MT_file_import.remove( menu_import_mdx )
    
    del WarCraft3BoneProperties.bpy_type.warcraft_3
    del WarCraft3ArmatureProperties.bpy_type.warcraft_3
    
    for cls in reversed( wc_classes ):
        bpy.utils.unregister_class( cls )
        
    for cls in reversed( prop_classes ):
        bpy.utils.unregister_class( cls )


if __name__ == "__main__":
    register()

