import io_scene_warcraft_3.classes
from io_scene_warcraft_3 import binary
from io_scene_warcraft_3.parser.parse_attachment_visibility import parse_attachment_visibility
from io_scene_warcraft_3.parser.parse_node import parse_node


def parse_attachment(data, model):
    r = binary.Reader(data)
    dataSize = len(data)
    attachment = io_scene_warcraft_3.classes.WarCraft3Attachment.WarCraft3Attachment()
    attachment.node = parse_node(r)
    path = r.gets(260)
    attachmentId = r.getf('<I')[0]
    if r.offset < dataSize:
        parse_attachment_visibility(r)
    model.nodes.append(attachment)