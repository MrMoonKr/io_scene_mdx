from typing import List, Optional

from .WarCraft3Vertex import WarCraft3Vertex


class WarCraft3Geoset:
    def __init__(self):
        self.name: str                              = None
        self.wc3_vertices: list[WarCraft3Vertex]    = []
        self.vertices: list[tuple[float]]           = []
        self.normals: list[float]                   = []
        self.triangles: list[tuple[int]]            = []
        self.uvs: list[tuple[float]]                = []
        self.material_id: int                       = 0
        self.vertex_groups: list[list[int]]         = []
        self.vertex_groups_ids: Optional[list[int]] = None
        self.skin_weights: list[list[int]]          = []

