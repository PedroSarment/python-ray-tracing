
from obj_reader import ObjReader
from color import Color
from mesh import Mesh
from transformation import Transformation
import copy
import numpy as np
from point import Point
from vector import Vector
from camera import Camera
from scene import Scene
from light import Light
from phong import Phong
from sphere import Sphere
from material import Material
from plane import Plane

def thirdDelivery():

    camera_position = Point(0, 0, 10)
    camera_look_at = Point(0, 0, 0)
    camera_up_vector = Vector(0, 1, 0)
    camera_distance = 1
    camera_h_res = 800
    camera_v_res = 600

    camera = Camera(camera_position, camera_look_at, camera_up_vector, camera_distance, camera_h_res, camera_v_res)

    image = np.zeros((camera_v_res, camera_h_res, 3), dtype=np.uint8)

    # obj_reader = ObjReader("./inputs/icosahedron/icosahedron.obj")

    # mesh = Mesh(
    #     vertices=obj_reader.get_vertices(),
    #     faces=obj_reader.get_faces(),
    #     normals=obj_reader.normals,
    # )

    objects = [
        #mesh
    ]


    # Parede Trás 
    objects.append(
        Plane(
            point=Point(0, 0, -2), 
            normal=Vector(0, 0, 1),
            material=Material(
                ka=Vector(0.0, 0.0, 0.1),
                kd=Vector(0.64, 0.0, 0.0),
                ks=Vector(0.0, 0.0, 0.0),
                ke=Vector(0.0, 0.0, 0.0),
                ns=10,
                ni=1.0,
                d=1.0
            )
        )
    )

    # Esfera Ambiente
    objects.append(Sphere(
        center=Point(0, 2, 0),
        radius=0.9,
        material=Material(
            ka=Vector(0.2, 0.4, 0.8),           
            kd=Vector(0.0, 0.0, 0.0),          
            ks=Vector(0.0, 0.0, 0.0),  
            ke=Vector(0.0, 0.0, 0.0),
            ns=1, 
            ni=1.0,                              
            d=1.0
        )
    ))

    # Esfera Difusa
    objects.append(Sphere(
        center=Point(3, 2, 0),
        radius=0.9,
        material=Material(
            ka=Vector(0.0, 0.0, 0.0),           
            kd=Vector(0.1, 0.1, 0.8),          
            ks=Vector(0.0, 0.0, 0.0),  
            ke=Vector(0.0, 0.0, 0.0),
            ns=1, 
            ni=1.0,                              
            d=1.0
        )
    ))

    # Esfera Especular
    objects.append(Sphere(
        center=Point(-3, 2, 0),
        radius=0.9,
        material=Material(
            ka=Vector(0.0, 0.0, 0.0),           
            kd=Vector(0.0, 0.0, 0.0),          
            ks=Vector(0.9, 0.9, 0.9),  
            ke=Vector(0.0, 0.0, 0.0),
            ns=1, 
            ni=1.0,                              
            d=1.0
        )
    ))

    # Esfera Equilibrada
    objects.append(Sphere(
        center=Point(0, -2, 0),
        radius=1.5,
        material=Material(
            ka=Vector(0.1, 0.1, 0.1),        # luz ambiente sutil
            kd=Vector(0.3, 0.4, 0.3),        # cinza com RGB invertido
            ks=Vector(0.4, 0.4, 0.4),        # brilho discreto
            ke=Vector(0.0, 0.0, 0.0),        # sem emissão
            ns=50,                           # brilho bem definido
            ni=1.0,                          # sem refração
            d=1.0  
        )
    ))

    scene_lights = Scene(
        lights=[
            Light(Point(0, 0, 10), (140, 140, 140)),
            Light(Point(0, -10, 10), (180, 180, 180))  
        ],
        ambient=(120, 120, 120)
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
                    view_dir = (camera.position - result.hit_point).normalize()
                    color = Phong.phong_illumination(
                        hit_point=result.hit_point,
                        normal=result.normal,
                        view_dir=view_dir,
                        material=result.material,
                        scene_lights=scene_lights,
                        objects=objects
                    )

            image[j, i] = color.array()

    return image