from .binary_reader import Reader
from ..classes.WarCraft3Transformation import WarCraft3Transformation
from .. import constants


def parse_attachment_visibility( br: Reader ):
    '''
        Animation Data of Attachment Visibility.  
        data type : '<f'  
        '''
        
    chunk_id    = br.getid( constants.CHUNK_ATTACHMENT_VISIBILITY ) # 'KATV'
    
    visibility                      = WarCraft3Transformation()
    
    visibility.tracks_count         = br.getf('<I')[0]
    visibility.interpolation_type   = br.getf('<I')[0]
    global_sequence_id              = br.getf('<I')[0]

    for _ in range( visibility.tracks_count ):
        time: int                   = br.getf('<I')[0]
        value: float                = br.getf('<f')[0]    # visibility value
        
        if visibility.interpolation_type > constants.INTERPOLATION_TYPE_LINEAR:
            in_tan                  = br.getf('<f')[0]
            out_tan                 = br.getf('<f')[0]

        visibility.times.append( time )
        visibility.values.append( value )

    return visibility
