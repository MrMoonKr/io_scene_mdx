# Constants for MDX file format

MDX_VERSIONS                    = [800, 900, 1000, 1100, 1200]
MDX_CURRENT_VERSION             = 1200

# MDX FILE CHUNKS
CHUNK_MDX_MODEL                 = 'MDLX'

# MDX MODEL SUB-CHUNKS
CHUNK_VERSION                   = 'VERS'
CHUNK_MODEL                     = 'MODL'
CHUNK_SEQUENCE                  = 'SEQS'
CHUNK_MATERIAL                  = 'MTLS'
CHUNK_TEXTURE                   = 'TEXS'
CHUNK_GEOSET                    = 'GEOS'
CHUNK_GEOSET_ANIMATION          = 'GEOA'
CHUNK_BONE                      = 'BONE'
CHUNK_ATTACHMENT                = 'ATCH'
CHUNK_PIVOT_POINT               = 'PIVT'
CHUNK_CORN                      = 'CORN'
CHUNK_CAMS                      = 'CAMS'
CHUNK_EVENT_OBJECT              = 'EVTS'
CHUNK_COLLISION_SHAPE           = 'CLID'
CHUNK_CLID                      = 'FAFX'
CHUNK_BPOS                      = 'BPOS'
CHUNK_HELPER                    = 'HELP'

# GEOSET SUB-CHUNKS
CHUNK_VERTEX_POSITION           = 'VRTX'
CHUNK_VERTEX_NORMAL             = 'NRMS'
CHUNK_FACE_TYPE_GROUP           = 'PTYP'
CHUNK_FACE_GROUP                = 'PCNT'
CHUNK_FACE                      = 'PVTX'
CHUNK_VERTEX_GROUP              = 'GNDX'
CHUNK_MATRIX_GROUP              = 'MTGC'
CHUNK_MATRIX_INDEX              = 'MATS'
CHUNK_TANGENTS                  = 'TANG'
CHUNK_SKIN                      = 'SKIN'
CHUNK_TEXTURE_VERTEX_GROUP      = 'UVAS'
CHUNK_VERTEX_TEXTURE_POSITION   = 'UVBS'

# MATERIAL SUB-CHUNKS
CHUNK_LAYER                     = 'LAYS'
# LAYER SUB-CHUNKS
CHUNK_MATERIAL_TEXTURE_ID       = 'KMTF'
CHUNK_MATERIAL_ALPHA            = 'KMTA'
CHUNK_MATERIAL_EMISSIONS        = 'KMTE'
CHUNK_MATERIAL_FRESNEL_COLOR    = 'KFC3'
CHUNK_MATERIAL_FRESNEL_ALPHA    = 'KFCA'
CHUNK_MATERIAL_FRESNEL_TEAMCOLOR = 'KFTC'

# NODE SUB-CHUNKS
CHUNK_GEOSET_TRANSLATION        = 'KGTR'
CHUNK_GEOSET_ROTATION           = 'KGRT'
CHUNK_GEOSET_SCALING            = 'KGSC'

# ATTACHMENT SUB-CHUNKS
CHUNK_ATTACHMENT_VISIBILITY     = 'KATV'

# EVENT OBJECT SUB-CHUNKS
CHUNK_TRACKS                    = 'KEVT'

# GEOSET ANIMATION SUB-CHUNKS
CHUNK_GEOSET_COLOR              = 'KGAC'
CHUNK_GEOSET_ALPHA              = 'KGAO'

# SUB-CHUNKS
SUB_CHUNKS_MDX_MODEL = (
    CHUNK_VERSION,
    CHUNK_GEOSET,
    CHUNK_TEXTURE,
    CHUNK_MATERIAL,
    CHUNK_MODEL,
    CHUNK_BONE,
    CHUNK_PIVOT_POINT,
    CHUNK_HELPER,
    CHUNK_ATTACHMENT,
    CHUNK_EVENT_OBJECT,
    CHUNK_COLLISION_SHAPE,
    CHUNK_SEQUENCE,
    CHUNK_GEOSET_ANIMATION
)

SUB_CHUNKS_LAYER = (
    CHUNK_MATERIAL_TEXTURE_ID,
    CHUNK_MATERIAL_ALPHA,
    CHUNK_MATERIAL_EMISSIONS,
    CHUNK_MATERIAL_FRESNEL_COLOR,
    CHUNK_MATERIAL_FRESNEL_ALPHA,
    CHUNK_MATERIAL_FRESNEL_TEAMCOLOR
)

SUB_CHUNKS_GEOSET_ANIMATION = (
    CHUNK_GEOSET_COLOR,
    CHUNK_GEOSET_ALPHA
)

SUB_CHUNKS_NODE = (
    CHUNK_GEOSET_TRANSLATION,
    CHUNK_GEOSET_ROTATION,
    CHUNK_GEOSET_SCALING
)

# INTERPOLATION TYPES
INTERPOLATION_TYPE_NONE     = 0
INTERPOLATION_TYPE_LINEAR   = 1
INTERPOLATION_TYPE_HERMITE  = 2
INTERPOLATION_TYPE_BEZIER   = 3
INTERPOLATION_TYPE_NAMES    = {
    0: 'CONSTANT',
    1: 'LINEAR',
    2: 'BEZIER',
    3: 'BEZIER'
}
INTERPOLATION_TYPE_NUMBERS  = {
    'DontInterp': 0,
    'Linear': 1,
    'Hermite': 2,
    'Bezier': 3
}

# TEAM COLORS
TEAM_COLORS = {
    'RED'           : (1.0, 0.000911, 0.000911),
    'DARK_BLUE'     : (0.0, 0.054480, 1.0),
    'TURQUOISE'     : (0.011612, 0.791298, 0.485150),
    'VIOLET'        : (0.088656, 0.000000, 0.219526),
    'YELLOW'        : (1.000000, 0.973446, 0.000304),
    'ORANGE'        : (0.991102, 0.254152, 0.004391),
    'GREEN'         : (0.014444, 0.527115, 0.000000),
    'PINK'          : (0.783538, 0.104617, 0.434154),
    'GREY'          : (0.300544, 0.304987, 0.309469),
    'BLUE'          : (0.208637, 0.520996, 0.879623),
    'DARK_GREEN'    : (0.005182, 0.122139, 0.061246),
    'BROWN'         : (0.076185, 0.023153, 0.001214),
    'BLACK'         : (0.021219, 0.021219, 0.021219)
}


TEAM_COLOR_IMAGE_PATH       = 'ReplaceableTextures\\TeamColor\\TeamColor'
TEAM_GLOW_IMAGE_PATH        = 'ReplaceableTextures\\TeamGlow\\TeamGlow'
TEAM_IMAGE_EXT              = '.blp'

def get_team_color( teamColorIndex: int ) -> str:
    return TEAM_COLOR_IMAGE_PATH + '{0:0>2}'.format( teamColorIndex ) + TEAM_IMAGE_EXT


def get_team_glow( teamGlowIndex: int ) -> str:
    return TEAM_GLOW_IMAGE_PATH + '{0:0>2}'.format( teamGlowIndex ) + TEAM_IMAGE_EXT


TEAM_COLOR_IMAGES = {
    'RED'           : get_team_color(0),
    'DARK_BLUE'     : get_team_color(1),
    'TURQUOISE'     : get_team_color(2),
    'VIOLET'        : get_team_color(3),
    'YELLOW'        : get_team_color(4),
    'ORANGE'        : get_team_color(5),
    'GREEN'         : get_team_color(6),
    'PINK'          : get_team_color(7),
    'GREY'          : get_team_color(8),
    'BLUE'          : get_team_color(9),
    'DARK_GREEN'    : get_team_color(10),
    'BROWN'         : get_team_color(11),
    'BLACK'         : get_team_color(12)
}

TEAM_GLOW_IMAGES = {
    'RED'           : get_team_glow(0),
    'DARK_BLUE'     : get_team_glow(1),
    'TURQUOISE'     : get_team_glow(2),
    'VIOLET'        : get_team_glow(3),
    'YELLOW'        : get_team_glow(4),
    'ORANGE'        : get_team_glow(5),
    'GREEN'         : get_team_glow(6),
    'PINK'          : get_team_glow(7),
    'GREY'          : get_team_glow(8),
    'BLUE'          : get_team_glow(9),
    'DARK_GREEN'    : get_team_glow(10),
    'BROWN'         : get_team_glow(11),
    'BLACK'         : get_team_glow(12)
}
