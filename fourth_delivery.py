
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
from render import Render
from sphere import Sphere
from plane import Plane
from material import Material

def fourthDelivery():

    camera_position = Point(-10, 0, 30)
    camera_look_at = Point(4, 0, 0)
    camera_up_vector = Vector(0, -1, 0)
    camera_distance = 2
    camera_h_res = 800
    camera_v_res = 600

    camera = Camera(camera_position, camera_look_at, camera_up_vector, camera_distance, camera_h_res, camera_v_res)

    image = np.zeros((camera_v_res, camera_h_res, 3), dtype=np.uint8)

    objects = []

    #Esfera Opaca Fundo
    objects.append(
        Sphere(
            center=Point(8, 0, -10),
            radius=6.0,
            material=Material(
                ka=Vector(0.0, 0.0, 0.9),           
                kd=Vector(0.1, 0.0, 0.0),          
                ks=Vector(1.0, 1.0, 1.0),  
                ke=Vector(0.0, 0.0, 0.0),
                ns=100, 
                ni=1.0,                              
                d=1.0
            )
        )
    )

    #espelho
    objects.append(
        Sphere(
            center=Point(8, 0, 0),
            radius=1.8,
            material=Material(
                ka=Vector(0.0, 0.0, 0.0),           
                kd=Vector(0.1, 0.0, 0.0),          
                ks=Vector(1.0, 1.0, 1.0),  
                ke=Vector(0.0, 0.0, 0.0),
                ns=1000, 
                ni=10,                              
                d=1.0
            )
        )
    )

    #vidro
    objects.append(
        Sphere(
            center=Point(0, 0, 0),
            radius=2,
            material=Material(
                ka=Vector(0.0, 0.0, 0.0),           
                kd=Vector(0.05, 0.05, 0.05),          
                ks=Vector(1.0, 1.0, 1.0),  
                ke=Vector(0.0, 0.0, 0.0),
                ns=300, 
                ni=1.5,                              
                d=0.0
            )
        )
    )

    #Esfera atrás da camera
    objects.append(
        Sphere(
            center=Point(0, 0, 30),
            radius=2,
            material=Material(
                ka=Vector(0.0, 0.1, 0.2),           
                kd=Vector(0.05, 0.05, 0.1),          
                ks=Vector(0.3, 0.3, 0.3),  
                ke=Vector(0.0, 0.0, 0.0),
                ns=10, 
                ni=1.0,                              
                d=1.0
            )
        )
    )

    objects.append(Plane(
        point=Point(0, -5, 0),
        normal=Vector(0, 1, 0),
        material=Material(
            ka=Vector(0.1, 0.1, 0.1),    
            kd=Vector(0.5, 0.5, 0.5),   
            ks=Vector(1.0, 1.0, 1.0),   
            ke=Vector(0.0, 0.0, 0.0),         
            ns=300,                          
            ni=1.0,                           
            d=1.0
        )
    ))


    scene_lights = Scene(
        lights=[
            Light(Point(4, 0, 30), (190, 190, 190)),
            Light(Point(-40, 10, 20), (40, 40, 40)),  
            Light(Point(0, 40, 0), (90, 90, 90))  

        ],
        ambient=(100, 100, 100)
    )

    for j in range(camera.v_res):
        for i in range(camera.h_res):
            ray = camera.get_ray(i, j)
            color = Render.render(ray, objects, scene_lights, ior_i=1.0, depth=0, max_depth=3)
            image[j, i] =  (int(color.b), int(color.g), int(color.r))

    return image