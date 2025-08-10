import bpy
from bpy.types import AddonPreferences


class WarCraft3Preferences( AddonPreferences ):
    '''
        WarCraft 3 Addon Preferences.  
        Edit -> Preferences -> Add-ons -> io_scene_mdx -> Preferences 항목에 표시된다.  
        '''
    
    bl_idname = __package__
    
    resourceFolder: bpy.props.StringProperty(
        name='Resource',
        default='',
        subtype='DIR_PATH',
        description='Resource Folder'
    ) # type: ignore
    
    alternativeResourceFolder: bpy.props.StringProperty( 
        name='Alternative Resource',
        default='',
        subtype='DIR_PATH',
        description='Alternative Resource Folder'
    )  # type: ignore
    
    textureExtension: bpy.props.StringProperty(
        name='Image Extension',
        default='dds',
        description=' Texture Image Extension'
    )  # type: ignore

    def draw( self, context ):
        layout = self.layout
        
        layout.prop( self, 'resourceFolder' )
        layout.prop( self, 'alternativeResourceFolder' )
        layout.prop( self, 'textureExtension' )

