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
from second_delivery import secondDelivery
from material import Material
from light import Light
from scene import Scene
from phong import Phong
from third_delivery import thirdDelivery

def main():
   
    camera_position = Point(4, 0, 30)
    camera_look_at = Point(0, 0, 0)
    camera_up_vector = Vector(0, 1, 0)
    camera_distance = 1
    camera_h_res = 800
    camera_v_res = 600

    camera = Camera(camera_position, camera_look_at, camera_up_vector, camera_distance, camera_h_res, camera_v_res)

    image = np.zeros((camera_v_res, camera_h_res, 3), dtype=np.uint8)


    #objects = secondDelivery()

    objects = thirdDelivery()

    scene_lights = Scene(
        lights=[Light(Point(0, 10, 10), (255, 255, 255))],
        ambient=(0, 0, 0)
    )

    for j in range(camera.v_res):
        for i in range(camera.h_res):
            ray = camera.get_ray(i, j)
            closest_t = float('inf')
            color = np.array([255, 255, 255], dtype=np.uint8)

            for obj in objects:
                result = obj.intersect(ray)
                if result and result.t < closest_t:
                    closest_t = result.t
                    view_dir = (camera.position - result.hit_point).normalize()
                    color = Phong.phong_illumination(result.hit_point, result.normal, view_dir, result.material, scene_lights, objects)

            image[j, i] = color


    cv2.imshow("Ray Casting - Interseção com Esferas, Planos e Malhas de triângulos", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

   
