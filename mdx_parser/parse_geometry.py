from ..classes.WarCraft3Geoset import WarCraft3Geoset
from .binary_reader import Reader
from .. import constants
from .get_vertex_groups import get_vertex_groups


def parse_geometry( data: bytes, version: int ) -> WarCraft3Geoset:
    '''
        지오메트리 데이터 파싱
        '''
    br          = Reader( data )
    
    geoset      = WarCraft3Geoset()
    geoset.name = 'temp'

    # parse vertices
    chunk_id        = br.getid( constants.CHUNK_VERTEX_POSITION )   # 'VRTX'
    vertex_count    = br.getf('<I')[0]
    for _ in range( vertex_count ):
        vertex_position_x, vertex_position_y, vertex_position_z = br.getf('<3f')
        # print(vertex_position_x, ", ", vertex_position_y, ", ", vertex_position_z)
        geoset.vertices.append( [ vertex_position_x, vertex_position_y, vertex_position_z ] )

    # Read and ignore
    chunks_to_skip = [ [constants.CHUNK_VERTEX_NORMAL,   '<3f'],    # 'NRMS'
                       [constants.CHUNK_FACE_TYPE_GROUP, '<I'],     # 'PTYP'
                       [constants.CHUNK_FACE_GROUP,      '<I'] ]    # 'PCNT'
    for chunk in chunks_to_skip:
        chunk_id            = br.getid( chunk[0] )  # FourCC
        chunk_data_count    = br.getf('<I')[0]      # Data Count
        for _ in range( chunk_data_count ):
            chunk_data      = br.getf( chunk[1] )   # unpack format

    # parse
    chunk_id        = br.getid( constants.CHUNK_FACE )              # 'PVTX'
    indices_count   = br.getf('<I')[0]
    if indices_count % 3 != 0:
        raise Exception( 'bad indices ( indices_count % 3 != 0 )' )

    for _ in range( indices_count // 3 ):
        vertex_index1, vertex_index2, vertex_index3 = br.getf('<3H')
        geoset.triangles.append( ( vertex_index1, vertex_index2, vertex_index3 ) )

    # parse vertex groups
    chunk_id            = br.getid( constants.CHUNK_VERTEX_GROUP )  # 'GNDX'
    matrix_groups_count = br.getf('<I')[0]
    matrix_groups       = []

    for _ in range( matrix_groups_count ):
        matrix_group    = br.getf('<B')[0]
        matrix_groups.append( matrix_group )

    # parse matrix Groups
    chunk_id            = br.getid( constants.CHUNK_MATRIX_GROUP )  # 'MTGC'
    matrix_groups_sizes_count = br.getf('<I')[0]
    matrix_groups_sizes = []

    for _ in range( matrix_groups_sizes_count ):
        matrix_group_size = br.getf('<I')[0]
        matrix_groups_sizes.append( matrix_group_size )

    # parse MatrixIndices
    chunk_id = br.getid( constants.CHUNK_MATRIX_INDEX )             # 'MATS'
    matrix_indices_count = br.getf('<I')[0]
    matrix_indices      = []

    for _ in range( matrix_indices_count ):
        matrix_index    = br.getf('<I')[0]
        matrix_indices.append( matrix_index )

    # parse vertex groups
    vertex_groups, vertex_groups_ids = get_vertex_groups( matrix_groups, matrix_groups_sizes, matrix_indices )
    geoset.vertex_groups        = vertex_groups
    geoset.vertex_groups_ids    = vertex_groups_ids
    
    geoset.material_id  = br.getf('<I')[0]
    selection_group     = br.getf('<I')[0]
    selection_flags     = br.getf('<I')[0]

    if version > 800:
        lod             = br.getf('<I')[0]
        lod_name        = br.gets(80)

    bounds_radius       = br.getf('<f')[0]
    minimum_extent      = br.getf('<3f')
    maximum_extent      = br.getf('<3f')
    
    extents_count       = br.getf('<I')[0]

    for _ in range( extents_count ):
        bounds_radius   = br.getf('<f')[0]
        minimum_extent  = br.getf('<3f')
        maximum_extent  = br.getf('<3f')

    if version > 800:
        chunk_id        = br.getid( ( constants.CHUNK_TANGENTS, constants.CHUNK_SKIN, constants.CHUNK_TEXTURE_VERTEX_GROUP ) )
        
        if chunk_id == constants.CHUNK_TANGENTS:                    # 'TANG'
            tangent_size    = br.getf('<I')[0]
            br.skip( 16 * tangent_size )
            chunk_id        = br.getid( ( constants.CHUNK_SKIN, constants.CHUNK_TEXTURE_VERTEX_GROUP ) )
            
        if chunk_id == constants.CHUNK_SKIN:                        # 'SKIN'
            skin_size       = br.getf('<I')[0]
            skin_weights    = []
            for i in range( skin_size ):
                skin_weights.append( br.getf('<B')[0] )
            for i in ( range( int( skin_size / 8 ) ) ):             # BoneIndices : '<4B' , BoneWeight : '<4B'
                skin_weights.append( skin_weights[ i*8 : i*8+8 ] )
            chunk_id = br.getid( constants.CHUNK_TEXTURE_VERTEX_GROUP )
    else:
        chunk_id = br.getid( constants.CHUNK_TEXTURE_VERTEX_GROUP ) # 'UVAS'
        
    texture_vertex_group_count = br.getf('<I')[0]

    # parse uv-coordinates
    chunk_id = br.getid( constants.CHUNK_VERTEX_TEXTURE_POSITION )  # 'UVBS'
    vertex_texture_position_count = br.getf('<I')[0]

    for _ in range( vertex_texture_position_count ):
        u, v = br.getf('<2f')
        geoset.uvs.append( ( u, 1 - v ) )

    return geoset
