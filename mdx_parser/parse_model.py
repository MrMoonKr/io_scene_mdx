from . import binary_reader
from ..classes.WarCraft3Model import WarCraft3Model


def parse_model( data: bytes ) -> str:
    """
        'MODL' chunk data
    """
    br = binary_reader.Reader( data )
    
    name = br.gets( 80 )
    animation_file_name = br.gets( 260 )
    bounds_radius = br.getf('<f')[0]
    minimum_extent = br.getf('<3f')
    maximum_extent = br.getf('<3f')
    blend_time = br.getf('<I')[0]
    
    return name
