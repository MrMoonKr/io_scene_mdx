from .binary_reader import Reader
from ..classes.WarCraft3Transformation import WarCraft3Transformation
from .. import constants


def parse_material_alpha( br: Reader ):
    '''
        재질의 알파값 애니메이션 데이터 파싱. key type : '<f'
        '''
    alpha = WarCraft3Transformation()
    
    alpha.tracks_count          = br.getf('<I')[0]
    alpha.interpolation_type    = br.getf('<I')[0]
    global_sequence_id          = br.getf('<I')[0]

    for _ in range( alpha.tracks_count ):
        time        = br.getf('<I')[0] 
        value       = br.getf('<f')[0] # alpha value
        
        alpha.times.append( time )
        alpha.values.append( value )

        if alpha.interpolation_type > constants.INTERPOLATION_TYPE_LINEAR:
            in_tan  = br.getf('<f')[0]
            out_tan = br.getf('<f')[0]

    return alpha


