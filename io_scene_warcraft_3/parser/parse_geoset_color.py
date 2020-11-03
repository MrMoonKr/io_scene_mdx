import io_scene_warcraft_3.classes
from io_scene_warcraft_3 import constants


def parse_geoset_color(r):
    color = io_scene_warcraft_3.classes.WarCraft3GeosetTransformation.WarCraft3GeosetTransformation()
    color.tracks_count = r.getf('<I')[0]
    color.interpolation_type = r.getf('<I')[0]
    globalSequenceId = r.getf('<I')[0]
    for _ in range(color.tracks_count):
        time = r.getf('<I')[0]
        value = r.getf('<3f')    # color value
        color.times.append(time)
        color.values.append(value)
        if color.interpolation_type > constants.INTERPOLATION_TYPE_LINEAR:
            inTan = r.getf('<3f')
            outTan = r.getf('<3f')
    return color