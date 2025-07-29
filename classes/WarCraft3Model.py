from typing import List

from .WarCraft3GeosetAnimation import WarCraft3GeosetAnimation
from .WarCraft3Material import WarCraft3Material
from .WarCraft3Geoset import WarCraft3Geoset
from .WarCraft3Node import WarCraft3Node
from .WarCraft3Sequence import WarCraft3Sequence
from .WarCraft3Texture import WarCraft3Texture


class WarCraft3Model:
    def __init__( self ):
        self.file = ''
        self.version = 800
        self.name = ''
        self.geosets: list[WarCraft3Geoset] = []
        self.materials: list[WarCraft3Material] = []
        self.textures: list[WarCraft3Texture] = []
        # self.nodes: List[]  = []
        self.nodes: list[WarCraft3Node] = []
        self.sequences: list[WarCraft3Sequence] = []
        self.geoset_animations: list[WarCraft3GeosetAnimation] = []
        self.pivot_points: list[list[float]] = []

    def normalize_meshes_names( self ):
        for mesh in self.geosets:
            mesh.name = self.name
    def normalize_materials_names( self ):
        for i, mat in enumerate( self.materials ):
            mat.name = self.name + '_' + str( i )
