#from typing import List

from ..classes.WarCraft3Layer import WarCraft3Layer
from .. import constants
from . import binary_reader
from .parse_material_alpha import parse_material_alpha
from .parse_material_texture_id import parse_material_texture_id
from .parse_fresnel_color import parse_fresnel_color


def parse_layers( data: bytes, version: int ) -> list[WarCraft3Layer]:
    """
        'LAYS' chunk and chunk data
    """
    br = binary_reader.Reader( data )
    
    chunk_id = br.getid( constants.CHUNK_LAYER )
    layers_count = br.getf('<I')[0]
    
    layers: list[WarCraft3Layer] = []

    for _ in range( layers_count ):
        layer = WarCraft3Layer()
        
        inclusive_size = br.offset + br.getf('<I')[0]
        layer.filterMode = br.getf('<I')[0]
        layer.shadingFlags = br.getf('<I')[0]
        layer.texture_id = br.getf('<I')[0]
        layer.textureAnimationId = br.getf('<I')[0]
        layer.coordId = br.getf('<I')[0]
        layer.alpha = br.getf('<f')[0]
        # if constants.MDX_CURRENT_VERSION > 800:
        if version > 800:
            layer.emissive_gain = br.getf('<f')[0]
            # if constants.MDX_CURRENT_VERSION > 900:
            if version > 900:
                layer.fresnel_color = [br.getf('<f')[0], br.getf('<f')[0], br.getf('<f')[0]]
                layer.fresnel_opacity = br.getf('<f')[0]
                layer.fresnel_team_color = br.getf('<f')[0]
                
                track_count = br.getf('<I')[0]
                unknown_count = br.getf('<I')[0]
                br.skip( unknown_count * 2 * 4 )
                
                
        while br.offset < inclusive_size:
            chunk_id = br.getid( constants.SUB_CHUNKS_LAYER )
            
            if chunk_id == constants.CHUNK_MATERIAL_TEXTURE_ID:
                layer.material_texture_id = parse_material_texture_id(br)
                
            elif chunk_id == constants.CHUNK_MATERIAL_ALPHA:
                layer.material_alpha = parse_material_alpha( br )
                
            elif chunk_id == constants.CHUNK_MATERIAL_FRESNEL_COLOR:
                layer.fresnel_color = parse_fresnel_color(br)
                
            elif chunk_id == constants.CHUNK_MATERIAL_EMISSIONS:
                layer.emissions = parse_material_alpha(br)
                
            elif chunk_id == constants.CHUNK_MATERIAL_FRESNEL_ALPHA:
                layer.fresnel_alpha = parse_material_alpha(br)
                
            elif chunk_id == constants.CHUNK_MATERIAL_FRESNEL_TEAMCOLOR:
                layer.fresnel_team_color = parse_material_alpha(br)

        layers.append( layer )

    return layers
