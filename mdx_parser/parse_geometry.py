from mathutils import Vector, Quaternion, Matrix

from ..classes.WarCraft3Geoset import WarCraft3Geoset
from . import binary_reader
from .. import constants
from .get_vertex_groups import get_vertex_groups


def parse_geometry( data: bytes, version: int ) -> WarCraft3Geoset:
    '''
        메시 데이터 파싱.  
        '''
        
    br                      = binary_reader.Reader( data )
    data_size               = len( data )
    
    geoset                  = WarCraft3Geoset()
    geoset.name             = 'temp'

    # 'VRTX' 정점들의 위치
    chunk_id                = br.getid( constants.CHUNK_VERTEX_POSITION )
    vertex_count            = br.getf('<I')[0]
    for _ in range( vertex_count ):
        pos_x, pos_y, pos_z = br.getf('<3f')
        geoset.vertices.append( ( pos_x, pos_y, pos_z ) )

    # 'NRMS' 정점들의 법선, ...
    chunks_to_skip          = [ [constants.CHUNK_VERTEX_NORMAL,   '<3f'],   # 'NRMS'
                                [constants.CHUNK_FACE_TYPE_GROUP, '<I'],    # 'PTYP'
                                [constants.CHUNK_FACE_GROUP,      '<I'] ]   # 'PCNT' 인덱스 수 = 삼각형 수 * 3
    for chunk in chunks_to_skip:
        chunk_id            = br.getid( chunk[0] )      # FourCC
        chunk_data_count    = br.getf('<I')[0]          # Data Count
        for _ in range( chunk_data_count ):
            chunk_data      = br.getf( chunk[1] )       # unpack format

    # 'PVTX' 정점들의 삼각형 구성 인덱스들
    chunk_id                = br.getid( constants.CHUNK_FACE )
    indices_count           = br.getf('<I')[0]
    if indices_count % 3 != 0:
        raise Exception( 'bad indices ( indices_count % 3 != 0 )' )     # 숫자 에러 체크

    for _ in range( indices_count // 3 ):
        face_a, face_b, face_c = br.getf('<3H')
        geoset.triangles.append( ( face_a, face_b, face_c ) )

    # parse vertex groups
    chunk_id            = br.getid( constants.CHUNK_VERTEX_GROUP )  # 'GNDX'
    matrix_groups_count = br.getf('<I')[0]
    matrix_groups       = []

    for _ in range( matrix_groups_count ):
        matrix_group    = br.getf('<B')[0]
        matrix_groups.append( matrix_group )

    # 'MTGC' 변환행렬 그룹ID 배열 parse matrix Groups
    chunk_id            = br.getid( constants.CHUNK_MATRIX_GROUP )  # 'MTGC'
    matrix_groups_sizes_count = br.getf('<I')[0]
    matrix_groups_sizes = []

    for _ in range( matrix_groups_sizes_count ):
        matrix_group_size = br.getf('<I')[0]
        matrix_groups_sizes.append( matrix_group_size )

    # 'MATS' 변환행렬 ID 배열 parse MatrixIndices
    chunk_id                = br.getid( constants.CHUNK_MATRIX_INDEX )
    matrix_indices_count    = br.getf('<I')[0]
    matrix_indices          = []

    for _ in range( matrix_indices_count ):
        matrix_index        = br.getf('<I')[0]
        matrix_indices.append( matrix_index )

    # parse vertex groups
    vertex_groups, vertex_groups_ids = get_vertex_groups( matrix_groups, matrix_groups_sizes, matrix_indices )
    geoset.vertex_groups    = vertex_groups
    geoset.vertex_groups_ids = vertex_groups_ids

    # 재질 인덱스
    geoset.material_id      = br.getf('<I')[0]
    selection_group         = br.getf('<I')[0]
    selection_flags         = br.getf('<I')[0]

    if version > 800:
        lod                 = br.getf('<I')[0]
        lod_name            = br.gets(80)

    bounds_radius           = br.getf('<f')[0]
    minimum_extent          = br.getf('<3f')
    maximum_extent          = br.getf('<3f')
    
    extents_count           = br.getf('<I')[0]

    for _ in range( extents_count ):
        bounds_radius       = br.getf('<f')[0]
        minimum_extent      = br.getf('<3f')
        maximum_extent      = br.getf('<3f')

    if version > 800:
        chunk_id            = br.getid( ( constants.CHUNK_TANGENTS, constants.CHUNK_SKIN, constants.CHUNK_TEXTURE_VERTEX_GROUP ) )
        
        if chunk_id == constants.CHUNK_TANGENTS:                    # 'TANG'
            tangent_size    = br.getf('<I')[0]
            br.skip( 16 * tangent_size )
            chunk_id        = br.getid( ( constants.CHUNK_SKIN, constants.CHUNK_TEXTURE_VERTEX_GROUP ) )
            
        # 'SKIN' BoneIndices('<4B') and BoneWeights('<4B')
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
    chunk_id                = br.getid( constants.CHUNK_VERTEX_TEXTURE_POSITION )  # 'UVBS'
    vertex_uv_count         = br.getf('<I')[0]
    for _ in range( vertex_uv_count ):
        u, v                = br.getf('<2f')
        geoset.uvs.append( ( u, 1 - v ) )

    return geoset
