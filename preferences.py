import bpy


class WarCraft3Preferences( bpy.types.AddonPreferences ):
    '''
        WarCraft 3 Addon Preferences
    '''
    
    bl_idname = __package__
    
    resourceFolder: bpy.props.StringProperty( # type: ignore
        name='Resource',
        default='',
        subtype='DIR_PATH'
    )
    alternativeResourceFolder: bpy.props.StringProperty( # type: ignore
        name='Alternative Resource',
        default='',
        subtype='DIR_PATH'
    )
    textureExtension: bpy.props.StringProperty( # type: ignore
        name='Image Extension',
        default='dds'
    ) 

    def draw( self, context ):
        layout = self.layout
        
        layout.prop( self, 'resourceFolder' )
        layout.prop( self, 'alternativeResourceFolder' )
        layout.prop( self, 'textureExtension' )

