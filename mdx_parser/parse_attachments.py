from typing import List

from . import binary_reader
from .parse_attachment import parse_attachment
from ..classes.WarCraft3Model import WarCraft3Model
from ..classes.WarCraft3Node import WarCraft3Node


def parse_attachments( data: bytes ):
    data_size = len( data )
    br = binary_reader.Reader( data )

    nodes: List[WarCraft3Node] = []
    
    while br.offset < data_size:
        inclusive_size      = br.getf('<I')[0]
        attach_data_size    = inclusive_size - 4
        attach_data         = data[ br.offset : br.offset + attach_data_size ]
        br.skip( attach_data_size )
        attachment          = parse_attachment( attach_data )
        
        nodes.append( attachment )
    
    return nodes
