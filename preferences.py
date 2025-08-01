import bpy


class WarCraft3Preferences( bpy.types.AddonPreferences ):
    '''
        WarCraft 3 Addon Preferences.  
        Edit -> Preferences -> Add-ons -> io_scene_mdx -> Preferences 항목에 표시된다.  
        '''
    
    bl_idname = __package__
    
    resourceFolder: bpy.props.StringProperty( # type: ignore
        name='Resource',
        default='',
        subtype='DIR_PATH',
        description='Resource Folder'
    )
    alternativeResourceFolder: bpy.props.StringProperty( # type: ignore
        name='Alternative Resource',
        default='',
        subtype='DIR_PATH',
        description='Alternative Resource Folder'
    )
    textureExtension: bpy.props.StringProperty( # type: ignore
        name='Image Extension',
        default='dds',
        description=' Texture Image Extension'
    ) 

    def draw( self, context ):
        layout = self.layout
        
        layout.prop( self, 'resourceFolder' )
        layout.prop( self, 'alternativeResourceFolder' )
        layout.prop( self, 'textureExtension' )

