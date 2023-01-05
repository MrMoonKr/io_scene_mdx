from typing import List

from . import binary_reader
from .parse_geometry import parse_geometry
from ..classes.WarCraft3Geoset import WarCraft3Geoset


def parse_geosets( data: bytes, version: int ) -> list[WarCraft3Geoset]:
    """
        'GEOS' chunk data
    """
    data_size = len( data )
    br = binary_reader.Reader( data )

    geosets: list[WarCraft3Geoset] = []
    
    while br.offset < data_size:
        inclusive_size = br.getf('<I')[0]
        geo_data_size = inclusive_size - 4
        geo_data = data[ br.offset : ( br.offset + geo_data_size ) ]
        br.skip( geo_data_size )
        
        mesh = parse_geometry( geo_data, version )
        
        geosets.append( mesh )
        
    return geosets

