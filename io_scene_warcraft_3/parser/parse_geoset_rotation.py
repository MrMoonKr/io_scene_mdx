import io_scene_warcraft_3.classes
from io_scene_warcraft_3 import constants


def parse_geoset_rotation(r):
    rotation = io_scene_warcraft_3.classes.WarCraft3GeosetTransformation.WarCraft3GeosetTransformation()
    rotation.tracks_count = r.getf('<I')[0]
    rotation.interpolation_type = r.getf('<I')[0]
    globalSequenceId = r.getf('<I')[0]
    for _ in range(rotation.tracks_count):
        time = r.getf('<I')[0]
        rotX, rotY, rotZ, rotW = r.getf('<4f')
        if rotation.interpolation_type > constants.INTERPOLATION_TYPE_LINEAR:
            inTan = r.getf('<4f')
            outTan = r.getf('<4f')
        values = (rotW, rotX, rotY, rotZ)    # rotation values
        rotation.times.append(time)
        rotation.values.append(values)
    return rotation