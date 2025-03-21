
from obj_reader import ObjReader
from color import Color
from mesh import TriangleMesh
from transformation import Transformation
import copy
import numpy as np
from material import Material

def thirdDelivery():
    obj_reader = ObjReader("./inputs/icosahedron/icosahedron.obj")

    material = Material(
        ka=obj_reader.get_ka(), 
        kd=obj_reader.get_kd(),
        ks=obj_reader.get_ks(),
        kr=(0.0, 0.0, 0.0), 
        kt=(0.0, 0.0, 0.0),
        eta=obj_reader.get_ns()
    )
    mesh = TriangleMesh(
        vertices=obj_reader.get_vertices(),
        faces=[face.vertice_indices for face in obj_reader.get_faces()],
        normals=obj_reader.normals,
        material=material
    )

    objects = [
        mesh
    ]

    #Mesh transladada e rotacionadaa
    meshRotated = copy.deepcopy(mesh)
    translation_matrix = Transformation.translation(2, 0, 0) 
    meshRotated.transform(translation_matrix)
    matrix = Transformation.rotation_x(np.radians(60))
    meshRotated.transform(matrix)
    matrix = Transformation.rotation_z(np.radians(60))
    meshRotated.transform(matrix)
    objects.append( meshRotated )

    return objects