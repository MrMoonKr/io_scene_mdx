from io import BufferedReader

from .parse_mdx import parse_mdx
from ..classes.MDXImportProperties import MDXImportProperties


def load_mdx( import_properties: MDXImportProperties ):
    """
        파일열어서 파일데이터 읽어들여 파서에 전달
        """
    mdx_file: BufferedReader = open( import_properties.mdx_file_path, 'rb' )
    mdx_file_data: bytes = mdx_file.read()
    mdx_file.close()
    
    parse_mdx( mdx_file_data, import_properties )
    
    print("Done!")
