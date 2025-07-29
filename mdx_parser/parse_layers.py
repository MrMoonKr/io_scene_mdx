#from typing import List

from ..classes.WarCraft3Layer import WarCraft3Layer
from .. import constants
from . import binary_reader
from .parse_material_alpha import parse_material_alpha
from .parse_material_texture_id import parse_material_texture_id
from .parse_fresnel_color import parse_fresnel_color


def parse_layers( data: bytes, version: int ) -> list[WarCraft3Layer]:
    """
        'LAYS' chunk and chunk data. 재질의 레이어 데이터 파싱
        """
    
    br                  = binary_reader.Reader( data )
    data_size           = len( data )
    
    chunk_id            = br.getid( constants.CHUNK_LAYER ) # 'LAYS'
    layers_count        = br.getf('<I')[0]
    
    layers: list[WarCraft3Layer] = []

    for _ in range( layers_count ):
        layer           = WarCraft3Layer()
        
        # Layer Data
        inclusive_size              = br.offset + br.getf('<I')[0] # to end-offset
        layer.filterMode            = br.getf('<I')[0]
        layer.shadingFlags          = br.getf('<I')[0]
        layer.texture_id            = br.getf('<I')[0]
        layer.textureAnimationId    = br.getf('<I')[0]
        layer.coordId               = br.getf('<I')[0]
        layer.alpha                 = br.getf('<f')[0]

        if version > 800:
            layer.emissive_gain     = br.getf('<f')[0]

            if version > 900:
                layer.fresnel_color         = [ br.getf('<f')[0], br.getf('<f')[0], br.getf('<f')[0] ]
                layer.fresnel_opacity       = br.getf('<f')[0]
                layer.fresnel_team_color    = br.getf('<f')[0]
                
                track_count         = br.getf('<I')[0]
                map_count           = br.getf('<I')[0]
                # br.skip( map_count * 2 * 4 )
                layer.map_ids       = br.getf('<{}I'.format( map_count * 2 ))

        # Animation Data
        while br.offset < inclusive_size:
            chunk_id = br.getid( constants.SUB_CHUNKS_LAYER )
            
            if chunk_id == constants.CHUNK_MATERIAL_TEXTURE_ID: # 'KMTF'
                layer.material_texture_id = parse_material_texture_id( br )
                
            elif chunk_id == constants.CHUNK_MATERIAL_ALPHA: # 'KMTA'
                layer.material_alpha = parse_material_alpha( br )
                
            elif chunk_id == constants.CHUNK_MATERIAL_FRESNEL_COLOR: # 'KFC3'
                layer.fresnel_color = parse_fresnel_color( br )
                
            elif chunk_id == constants.CHUNK_MATERIAL_EMISSIONS: # 'KMTE'
                layer.emissions = parse_material_alpha( br )
                
            elif chunk_id == constants.CHUNK_MATERIAL_FRESNEL_ALPHA: # 'KFCA'
                layer.fresnel_alpha = parse_material_alpha( br )
                
            elif chunk_id == constants.CHUNK_MATERIAL_FRESNEL_TEAMCOLOR: # 'KFTC'
                layer.fresnel_team_color = parse_material_alpha( br )

        layers.append( layer )

    return layers


