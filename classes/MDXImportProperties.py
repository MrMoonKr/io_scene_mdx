import bpy


class MDXImportProperties:
    '''
        임포트 옵션
        '''
    def __init__( self ):
        self.mdx_file_path: str     = ''
        self.team_color: str        = 'RED'
        self.bone_size: float       = 1.0
        self.use_custom_fps: bool   = False
        self.fps: float             = 30
        self.frame_time: float      = 1.0

    def calculate_frame_time( self ):
        if not self.use_custom_fps:
            self.fps = bpy.context.scene.render.fps
        self.frame_time = 1000 / self.fps
