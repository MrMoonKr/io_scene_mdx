from .binary_reader import Reader
from ..classes.WarCraft3Node import WarCraft3Node
from .. import constants
from .parse_geoset_transformation import parse_geoset_transformation


def parse_node( br: Reader, node: WarCraft3Node ) -> WarCraft3Node:
    """
        node data + node animation ( .translations .rotations .scalings )
        """
        
    # Node Data
    inclusive_size  = br.offset + br.getf('<I')[0]  # end-offset
    node.name       = br.gets(80)
    node.id         = br.getf('<I')[0]
    node.parent     = br.getf('<I')[0]
    if node.parent == 0xffffffff:                   # for convenience
        node.parent = None
    flags           = br.getf('<I')[0]

    # Node Animation
    while br.offset < inclusive_size:
        chunk_id    = br.getid( constants.SUB_CHUNKS_NODE ) # node animation

        if chunk_id == constants.CHUNK_GEOSET_TRANSLATION: # 'KGTR'
            node.translations   = parse_geoset_transformation( br, '<3f' )
            
        elif chunk_id == constants.CHUNK_GEOSET_ROTATION: # 'KGRT'
            node.rotations      = parse_geoset_transformation( br, '<4f' )
            
        elif chunk_id == constants.CHUNK_GEOSET_SCALING: # 'KGSC'
            node.scalings       = parse_geoset_transformation( br, '<3f' )

    return node


