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

def main():
   
    camera_position = Point(0, 0, 0)
    camera_look_at = Point(0, 0, -1)
    camera_up_vector = Vector(0, 1, 0)
    camera_distance = 1
    camera_h_res = 800
    camera_v_res = 600

    camera = Camera(camera_position, camera_look_at, camera_up_vector, camera_distance, camera_h_res, camera_v_res)

    image = np.zeros((camera_v_res, camera_h_res, 3), dtype=np.uint8)

    # Lista de objetos
    objects = [
        Sphere(Point(0, 0, -5), 1, Color(255, 0, 0)),
        Sphere(Point(-2, 1, -6), 1.2, Color(0, 255, 0)),
        Sphere(Point(2, -1, -4), 0.8, Color(0, 0, 255)),
        Plane(Point(0, -1, 0), Vector(0, 1, 0), Color(255, 255, 0)) 
    ]
 
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

   
