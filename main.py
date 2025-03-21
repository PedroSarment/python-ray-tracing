from obj_reader import ObjReader
from point import Point
from vector import Vector
from sphere import Sphere
from plane import Plane
from ray import Ray
from camera import Camera
from color import Color
import numpy as np
import cv2
from mesh import TriangleMesh
from transformation import Transformation
import copy


def main():
   
    camera_position = Point(2, 0, 30)
    camera_look_at = Point(0, 0, 0)
    camera_up_vector = Vector(0, 1, 0)
    camera_distance = 1
    camera_h_res = 800
    camera_v_res = 600

    camera = Camera(camera_position, camera_look_at, camera_up_vector, camera_distance, camera_h_res, camera_v_res)

    image = np.zeros((camera_v_res, camera_h_res, 3), dtype=np.uint8)

    # Objetos primeira Entrega
    # objects = [
    #     mesh,
    #     Sphere(Point(-2, 1, -6), 1.2, Color(0, 255, 0)),
    #     Sphere(Point(2, -1, -4), 0.8, Color(0, 0, 255)),
    #     Plane(Point(0, -1, 0), Vector(0, 1, 0), Color(255, 255, 0)) 
    # ]

    # Malha de triângulos para a primeira parte da segunda entrega
    obj_reader = ObjReader("./inputs/icosahedron/icosahedron.obj")
    mesh = TriangleMesh(
        vertices=obj_reader.get_vertices(),
        faces=[face.vertice_indices for face in obj_reader.get_faces()],
        normals=obj_reader.normals,
        color=Color(0, 255, 0)
    )

    # Objetos primeira Entrega
    objects = [
        mesh
    ]

    
    # Mesh transladada e rotacionadaa
    meshRotated = copy.deepcopy(mesh)
    translation_matrix = Transformation.translation(5, 0, 0) 
    meshRotated.transform(translation_matrix)
    euler_matrix = Transformation.rotation_x(np.radians(60))
    meshRotated.transform(euler_matrix)
    objects.append( meshRotated )

 
    # Testando interseções
    for j in range(camera_v_res):
        for i in range(camera_h_res):
            ray = camera.get_ray(i, j)
            closest_t = float('inf')
            color =  Color(0, 0, 0).array()
            
            for obj in objects:
                t = obj.intersect(ray)
                if t and t < closest_t:
                    closest_t = t
                    color = obj.color.array()
            
            image[j, i] = color


    cv2.imshow("Ray Casting - Interseção com Esferas, Planos e Malhas de triângulos", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

   
