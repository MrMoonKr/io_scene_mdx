from .binary_reader import Reader
from ..classes.WarCraft3Transformation import WarCraft3Transformation
from .. import constants

# format:
# scaling, translation: '<3f'
# rotation: '<4f'


def parse_node_animation( br: Reader, value_format: str ) -> WarCraft3Transformation:
    """
        node animation data.  
        format:  
        scaling, translation : '<3f'  
        rotation : '<4f'
        """
        
    transformation                      = WarCraft3Transformation()
    
    transformation.tracks_count         = br.getf('<I')[0]      # Keyframe Count
    transformation.interpolation_type   = br.getf('<I')[0]      # Keyframe Interpolation Type
    global_sequence_id                  = br.getf('<I')[0]      # Unknown

    for _ in range( transformation.tracks_count ):              # read keyframes
        time            = br.getf('<I')[0]                      # keyframe time
        values          = br.getf( value_format )               # keyframe values
        if value_format == '<4f':
            values      = ( values[3], values[0], values[1], values[2] ) # rotation correction ( w, x, y, z )

        if transformation.interpolation_type > constants.INTERPOLATION_TYPE_LINEAR:
            in_tan      = br.getf( value_format )
            out_tan     = br.getf( value_format )

        transformation.times.append( time )
        transformation.values.append( values )

    return transformation
