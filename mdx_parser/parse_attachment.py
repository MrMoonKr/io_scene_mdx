from ..classes.WarCraft3Attachment import WarCraft3Attachment
from . import binary_reader
from .parse_attachment_visibility import parse_attachment_visibility
from .parse_node import parse_node


def parse_attachment( data: bytes ):
    '''
        Attachment Chunk.  
        '''
        
    br              = binary_reader.Reader( data )
    data_size       = len( data )
    
    attachment      = WarCraft3Attachment()
    
    parse_node( br, attachment )
    
    path            = br.gets( 260 )
    attachment_id   = br.getf('<I')[0]

    if br.offset < data_size:
        parse_attachment_visibility( br )
        
    return attachment


