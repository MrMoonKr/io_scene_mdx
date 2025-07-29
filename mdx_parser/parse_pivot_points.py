from . import binary_reader
from ..classes.WarCraft3Model import WarCraft3Model


def parse_pivot_points( data: bytes ) -> list[ tuple[float] ]:
    """
        'PIVT' chunk data  
        """
        
    br                  = binary_reader.Reader( data )
    data_size           = len( data )

    if data_size % 12 != 0:
        raise Exception('bad Pivot Point data (size % 12 != 0)')

    pivot_points_count  = data_size // 12

    pivot_points: list[ tuple[float] ] = []
    
    for _ in range( pivot_points_count ):
        point           = br.getf('<3f')
        
        pivot_points.append( point )
        
    return pivot_points


