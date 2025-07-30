from typing import List

from ..classes.WarCraft3Bone import WarCraft3Bone
from . import binary_reader
from .parse_node import parse_node
from ..classes.WarCraft3Node import WarCraft3Node


def parse_bones( data: bytes ) -> list[WarCraft3Node]:
    """
        'BONE' chunk data.  
        """
        
    br              = binary_reader.Reader( data )
    data_size       = len( data )

    nodes: list[WarCraft3Node] = []
    
    while br.offset < data_size:
        bone        = WarCraft3Bone()
        
        parse_node( br, bone )
        
        bone.geoset_id              = br.getf('<I')[0]
        bone.geoset_animation_id    = br.getf('<I')[0]
        
        nodes.append( bone )
        
    return nodes


