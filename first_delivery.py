from obj_reader import ObjReader
from color import Color
from mesh import Mesh
from transformation import Transformation
import copy
import numpy as np
from point import Point
from vector import Vector
from camera import Camera
from plane import Plane
from sphere import Sphere
from material import Material

def firstDelivery():

    camera_position = Point(0, 0, 60)
    camera_look_at = Point(3, 0, 0)
    camera_up_vector = Vector(0, -1, 0)
    camera_distance = 4
    camera_h_res = 800
    camera_v_res = 600

    camera = Camera(camera_position, camera_look_at, camera_up_vector, camera_distance, camera_h_res, camera_v_res)

    image = np.zeros((camera_v_res, camera_h_res, 3), dtype=np.uint8)

    objects = []

    objects.append(Sphere(
        center=Point(1, -5, 0),
        radius=1.5,
        material=Material(
            ka=Vector(0.0, 0.1, 0.0),           
            kd=Vector(0.1, 0.6, 0.1),          
            ks=Vector(1.0, 1.0, 1.0),  
            ke=Vector(0.0, 0.0, 0.0),
            ns=100, 
            ni=1.0,                              
            d=1.0
        )
    ))

    objects.append(Sphere(
        center=Point(5, -5, 0),
        radius=1.5,
        material=Material(
            ka=Vector(0.1, 0.1, 0.1),
            kd=Vector(0.1, 0.3, 0.8),
            ks=Vector(0.5, 0.5, 0.5),
            ke=Vector(0.0, 0.0, 0.0),
            ns=30,
            ni=1.5,
            d=1.0   
        )
    ))

    objects.append(
        Plane(
            point=Point(0, -5, 0), 
            normal=Vector(0, 1, 0),
            material=Material(
                ka=Vector(0.1, 0.1, 0.1),
                kd=Vector(0.2, 0.2, 0.2),
                ks=Vector(0.5, 0.5, 0.5),
                ke=Vector(0.0, 0.0, 0.0),
                ns=10,
                ni=1.0,
                d=1.0
            )
        )
    )


    for j in range(camera.v_res):
        for i in range(camera.h_res):
            ray = camera.get_ray(i, j)
            closest_t = float('inf')
            color = Color(255, 255, 255)

            for obj in objects:
                result = obj.intersect(ray)
                if result and result.t < closest_t:
                    closest_t = result.t
                    color = Color(
                        int(result.material.kd.x * 255),
                        int(result.material.kd.y * 255),
                        int(result.material.kd.z * 255)
                    )

            image[j, i] = color.array()

    return image