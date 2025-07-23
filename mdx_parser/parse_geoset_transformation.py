from .binary_reader import Reader
from ..classes.WarCraft3Transformation import WarCraft3Transformation
from .. import constants

# format:
# scaling, translation: '<3f'
# rotation: '<4f'


def parse_geoset_transformation( r: Reader, value_format: str ) -> WarCraft3Transformation:
    """
        node animation data
        """
    transformation = WarCraft3Transformation()
    
    transformation.tracks_count         = r.getf('<I')[0] # Keyframe Count
    transformation.interpolation_type   = r.getf('<I')[0] # Keyframe Interpolation Type
    global_sequence_id                  = r.getf('<I')[0] # Unknown

    for _ in range( transformation.tracks_count ): # read keyframes
        time        = r.getf('<I')[0] # keyframe time
        values      = r.getf( value_format ) # keyframe values

        if value_format == '<4f':
            values  = ( values[3], values[0], values[1], values[2] ) # rotation correction ( w, x, y, z )

        transformation.times.append( time )
        transformation.values.append( values )

        if transformation.interpolation_type > constants.INTERPOLATION_TYPE_LINEAR:
            in_tan  = r.getf( value_format )
            out_tan = r.getf( value_format )

    return transformation
