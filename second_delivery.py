from obj_reader import ObjReader
from color import Color
from mesh import Mesh
from transformation import Transformation
import copy
import numpy as np
from point import Point
from vector import Vector
from camera import Camera

def secondDelivery():

    camera_position = Point(0, 0, 40)
    camera_look_at = Point(0, 0, 0)
    camera_up_vector = Vector(0, 1, 0)
    camera_distance = 4
    camera_h_res = 800
    camera_v_res = 600

    camera = Camera(camera_position, camera_look_at, camera_up_vector, camera_distance, camera_h_res, camera_v_res)

    image = np.zeros((camera_v_res, camera_h_res, 3), dtype=np.uint8)

    obj_reader = ObjReader("./inputs/cubo/cubo.obj")

    mesh = Mesh(
        vertices=obj_reader.get_vertices(),
        faces=obj_reader.get_faces(),
        normals=obj_reader.normals,
    )

    objects = [
        mesh
    ]

    meshRotated = copy.deepcopy(mesh)
    translation_matrix = Transformation.translation(2, 0, 0) 
    meshRotated.transform(translation_matrix)
    matrix = Transformation.rotation_z(np.radians(45))
    meshRotated.transform(matrix)
    #matrix = Transformation.rotation_x(np.radians(180))
    #meshRotated.transform(matrix)

    objects.append( meshRotated )


    for j in range(camera.v_res):
        for i in range(camera.h_res):
            ray = camera.get_ray(i, j)
            closest_t = float('inf')
            color = Color(255, 255, 255)

            for obj in objects:
                result = obj.intersect(ray)
                if result and result.t < closest_t:
                    closest_t = result.t
                    view_dir = (camera.position - result.hit_point).normalize()
                    color = Color(
                        int(result.material.kd.x * 255),
                        int(result.material.kd.y * 255),
                        int(result.material.kd.z * 255)
                    )

            image[j, i] = color.array()

    return image