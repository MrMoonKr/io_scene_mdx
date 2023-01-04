#from typing import List

from ..classes.WarCraft3Material import WarCraft3Material
from . import binary_reader
from .parse_layers import parse_layers


def parse_materials( data: bytes, version: int ) -> list[WarCraft3Material]:
    """
        'MTLS' chunk data
    """
    br = binary_reader.Reader( data )
    data_size = len( data )

    materials: list[WarCraft3Material] = []

    while br.offset < data_size:
        material = WarCraft3Material()
        
        inclusive_size = br.getf('<I')[0]
        priority_plane = br.getf('<I')[0]
        render_mode = br.getf('<I')[0]

        # if constants.MDX_CURRENT_VERSION > 800:
        # if version > 800:
        #     shader = br.gets(80)
        #     if shader == "Shader_HD_DefaultUnit":
        #         material.hd = True
        #     layer_chunk_data_size = inclusive_size - 92
        # else:
        #     layer_chunk_data_size = inclusive_size - 12
        layer_chunk_data_size = inclusive_size - 12

        if layer_chunk_data_size > 0:
            layer_chunk_data: bytes = data[ br.offset : br.offset + layer_chunk_data_size ]
            br.skip( layer_chunk_data_size )
            material.layers = parse_layers( layer_chunk_data, version )

        materials.append( material )
        
    return materials
