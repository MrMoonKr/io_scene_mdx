from typing import List

from ..classes.WarCraft3Model import WarCraft3Model
from ..classes.WarCraft3Sequence import WarCraft3Sequence
from . import binary_reader


def parse_sequences( data: bytes ) -> List[WarCraft3Sequence]:
    """
        'SEQS' chunk data
        """
    
    br = binary_reader.Reader( data )
    data_size = len( data )

    if data_size % 132 != 0:
        raise Exception( 'bad sequence data (size % 132 != 0)' )

    sequence_count = data_size // 132

    sequences: List[WarCraft3Sequence] = []
    
    for _ in range( sequence_count ):
        sequence = WarCraft3Sequence()
        
        sequence.name           = br.gets( 80 )
        sequence.interval_start = br.getf('<I')[0]
        sequence.interval_end   = br.getf('<I')[0]
        move_speed              = br.getf('<f')[0]
        flags                   = br.getf('<I')[0]
        rarity                  = br.getf('<f')[0]
        sync_point              = br.getf('<I')[0]
        bounds_radius           = br.getf('<f')[0]
        minimum_extent          = br.getf('<3f')
        maximum_extent          = br.getf('<3f')
        
        sequences.append( sequence )
        
    return sequences
