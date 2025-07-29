from .binary_reader import Reader
from ..classes.WarCraft3Transformation import WarCraft3Transformation
from .. import constants


def parse_fresnel_color( br: Reader ) -> WarCraft3Transformation:
    '''
        색상( 3 floats ) 애니메이션 파싱.  
        key format : '<3f'
        '''
    fresnel_color       = WarCraft3Transformation()
    
    fresnel_color.tracks_count = br.getf('<I')[0]
    fresnel_color.interpolation_type = br.getf('<I')[0]
    global_sequence_id  = br.getf('<I')[0]

    for _ in range( fresnel_color.tracks_count ):
        time            = br.getf('<I')[0]
        value           = [ br.getf('<f')[0], br.getf('<f')[0], br.getf('<f')[0] ]
        if fresnel_color.interpolation_type > constants.INTERPOLATION_TYPE_LINEAR:
            in_tan      = [ br.getf('<f')[0], br.getf('<f')[0], br.getf('<f')[0] ]
            out_tan     = [ br.getf('<f')[0], br.getf('<f')[0], br.getf('<f')[0] ]

        fresnel_color.times.append( time )
        fresnel_color.values.append( value )

    return fresnel_color

