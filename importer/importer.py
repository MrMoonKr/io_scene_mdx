from typing import List

from bpy.types import Material, Object

from ..classes.MDXImportProperties import MDXImportProperties
from ..classes.WarCraft3Model import WarCraft3Model
from ..classes.WarCraft3Node import WarCraft3Node
from .create_armature_actions import create_armature_actions
from .create_armature_object import create_armature_object
from .create_mesh_objects import create_mesh_objects
from .create_material import create_material
from .create_object_actions import create_object_actions


def load_warcraft_3_model( model: WarCraft3Model, import_properties: MDXImportProperties ):

    make_heirarchy_nodes( model= model )

    bpy_materials: list[Material]   = create_material( model, import_properties.team_color )
    bpy_mesh_objects: list[Object]  = create_mesh_objects( model, bpy_materials )
    #armature_object: Object         = create_armature_object( model, bpy_mesh_objects, import_properties.bone_size )
    #create_armature_actions( armature_object, model, import_properties.frame_time )
    #create_object_actions( model, bpy_mesh_objects, import_properties.frame_time )
    
def make_heirarchy_nodes( model: WarCraft3Model ):
    """
        Hierarchy 구성    
        """
    nodes: list[WarCraft3Node]      = model.nodes
    pivot_points: list[list[float]] = model.pivot_points
    
    for nodeIndex, node in enumerate( nodes ):
        #print( str( nodeIndex ) + " : " + node.name )
        if node.parent is None:
            node.part = None
        else:
            parent = nodes[ node.parent ]
            if parent.children is None:
                parent.children = []
            parent.children.append( node )
            node.part = parent
