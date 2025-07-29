from typing import List

from . import binary_reader
from ..classes.WarCraft3Model import WarCraft3Model
from ..classes.WarCraft3Texture import WarCraft3Texture


def parse_textures( data: bytes ) -> list[WarCraft3Texture]:
    """
        'TEXS' chunk data.  
        재질에 사용되는 텍스쳐 데이터 파싱.  
        """
    
    br                  = binary_reader.Reader( data )
    data_size           = len( data )

    if data_size % 268 != 0:
        raise Exception('[io_scene_mdx] bad Texture data (size % 268 != 0)')

    textures_count      = data_size // 268
    textures: list[WarCraft3Texture] = []

    for _ in range( textures_count ):
        texture                 = WarCraft3Texture()
        
        texture.replaceable_id  = br.getf('<I')[0]
        texture.image_file_name = br.gets( 260 )
        texture.flags           = br.getf('<I')[0]
        
        textures.append( texture )

    return textures

