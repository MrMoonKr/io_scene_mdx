from typing import List

from . import binary_reader
from ..classes.WarCraft3Model import WarCraft3Model
from ..classes.WarCraft3Texture import WarCraft3Texture


def parse_textures( data: bytes ):
    """
        'TEXS' chunk data.  텍스쳐 파일 데이터 파싱.  
        """
    
    br = binary_reader.Reader( data )
    data_size = len( data )

    if data_size % 268 != 0:
        raise Exception('bad Texture data (size % 268 != 0)')

    textures_count = data_size // 268
    textures: List[WarCraft3Texture] = []

    for _ in range( textures_count ):
        texture = WarCraft3Texture()
        
        texture.replaceable_id  = br.getf('<I')[0]
        texture.image_file_name = br.gets( 260 )
        texture.flags           = br.getf('<I')[0]
        
        textures.append( texture )

    return textures
