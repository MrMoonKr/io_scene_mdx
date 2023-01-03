from typing import List

from bpy.types import Material, Object

from ..classes.MDXImportProperties import MDXImportProperties
from ..classes.WarCraft3Model import WarCraft3Model
from .create_armature_actions import create_armature_actions
from .create_armature_object import create_armature_object
from .create_mesh_objects import create_mesh_objects
from .create_material import create_material
from .create_object_actions import create_object_actions


def load_warcraft_3_model(model: WarCraft3Model, import_properties: MDXImportProperties):

    #bpy_materials: List[Material] = create_material(model, import_properties.team_color)
    #bpy_mesh_objects: List[Object] = create_mesh_objects(model, bpy_materials)
    bpy_mesh_objects: List[Object] = create_mesh_objects(model, None )
    #armature_object: Object = create_armature_object(model, bpy_mesh_objects, import_properties.bone_size)
    #create_armature_actions(armature_object, model, import_properties.frame_time)
    #create_object_actions(model, bpy_mesh_objects, import_properties.frame_time)
