from io import BufferedReader

from .parse_mdx import parse_mdx
from ..classes.MDXImportProperties import MDXImportProperties
from ..importer import importer


def load_mdx( import_properties: MDXImportProperties ):
    """
        .mdx 파일의 파일데이터를 bytes로 읽어들여 파서에 전달
        """
    
    mdx_file: BufferedReader    = open( import_properties.mdx_file_path, 'rb' )
    mdx_file_data: bytes        = mdx_file.read()
    mdx_file.close()
    
    model                       = parse_mdx( mdx_file_data, import_properties )
    importer.load_warcraft_3_model( model, import_properties )
    
    print( "[io_scene_mdx] Import Done !!! : ", import_properties.mdx_file_path )
    
