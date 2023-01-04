from typing import Union, List

from ..classes.WarCraft3Helper import WarCraft3Helper
from . import binary_reader
from .parse_node import parse_node
from ..classes.WarCraft3Node import WarCraft3Node


def parse_helpers( data: bytes ):
    """
        'HELP' chunk data
    """
    data_size = len( data )
    br = binary_reader.Reader( data )

    nodes: list[WarCraft3Node] = []
    
    while br.offset < data_size:
        helper = WarCraft3Helper()
        
        parse_node( br, helper )
        
        nodes.append( helper )
        
    return nodes

