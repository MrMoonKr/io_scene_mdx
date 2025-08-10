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
        '''파일 경로명'''
        self.version = 800
        '''파일 버전'''
        self.name = ''
        '''모델 이름'''
        self.geosets: list[WarCraft3Geoset] = []
        '''메시 목록'''
        self.materials: list[WarCraft3Material] = []
        '''재질 목록'''
        self.textures: list[WarCraft3Texture] = []
        '''텍스쳐 목록'''
        # self.nodes: List[]  = []
        self.nodes: list[WarCraft3Node] = []
        '''노드 목록'''
        self.sequences: list[WarCraft3Sequence] = []
        '''애니메이션 목록'''
        self.geoset_animations: list[WarCraft3GeosetAnimation] = []
        '''메시 애니메이션 목록'''
        self.pivot_points: list[tuple[float,float,float]] = []
        '''노드 원점 목록'''

    def normalize_meshes_names( self ):
        for mesh in self.geosets:
            mesh.name = self.name
    def normalize_materials_names( self ):
        for i, mat in enumerate( self.materials ):
            mat.name = self.name + '_' + str( i )
