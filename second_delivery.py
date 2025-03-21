from obj_reader import ObjReader
from color import Color
from mesh import TriangleMesh
from transformation import Transformation
import copy
import numpy as np

def secondDelivery():
    obj_reader = ObjReader("./inputs/icosahedron/icosahedron.obj")
    mesh = TriangleMesh(
        vertices=obj_reader.get_vertices(),
        faces=[face.vertice_indices for face in obj_reader.get_faces()],
        normals=obj_reader.normals,
        color=Color(0, 255, 0)
    )

    objects = [
        mesh
    ]

    #Mesh transladada e rotacionadaa
    meshRotated = copy.deepcopy(mesh)
    translation_matrix = Transformation.translation(5, 0, 0) 
    meshRotated.transform(translation_matrix)
    matrix = Transformation.rotation_x(np.radians(60))
    meshRotated.transform(matrix)
    objects.append( meshRotated )

    return objects
