from typing import List, Optional

from .WarCraft3Vertex import WarCraft3Vertex


class WarCraft3Geoset:
    def __init__(self):
        self.name: str                              = None
        self.wc3_vertices: list[WarCraft3Vertex]    = []
        self.vertices: list[list[float]]            = []
        self.normals: list[float]                   = []
        self.triangles: list[int]                   = []
        self.uvs: list[float]                       = []
        self.material_id: int                       = 0
        self.vertex_groups: List[List[int]]         = []
        self.vertex_groups_ids: Optional[List[int]] = None
        self.skin_weights: List[List[int]]          = []

