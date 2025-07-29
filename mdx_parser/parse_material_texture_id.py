from .binary_reader import Reader
from ..classes.WarCraft3Transformation import WarCraft3Transformation
from .. import constants


def parse_material_texture_id( br: Reader ) -> WarCraft3Transformation:
    '''
        재질의 텍스쳐 애니메이션 파싱.  
        key format : '<I'
        '''
        
    texture_id          = WarCraft3Transformation()
    
    texture_id.tracks_count         = br.getf('<I')[0]
    texture_id.interpolation_type   = br.getf('<I')[0]
    global_sequence_id              = br.getf('<I')[0]

    for _ in range( texture_id.tracks_count ):
        time            = br.getf('<I')[0]
        value           = br.getf('<I')[0]    # texture id value
        
        if texture_id.interpolation_type > constants.INTERPOLATION_TYPE_LINEAR:
            in_tan      = br.getf('<f')[0]
            out_tan     = br.getf('<f')[0]

        texture_id.times.append( time )
        texture_id.values.append( value )

    return texture_id

