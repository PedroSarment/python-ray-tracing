from obj_reader import ObjReader
from point import Point
from vector import Vector
from sphere import Sphere
from plane import Plane
from ray import Ray
from camera import Camera
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

    image = np.zeros((camera_h_res, camera_v_res), dtype=np.uint8)

    # Lista de objetos
    objects = [
        Sphere(Point(0, 0, -5), 1, 255),
        Sphere(Point(-2, 1, -6), 1.2, 200),
        Sphere(Point(2, -1, -4), 0.8, 150),
        Plane(Point(0, -1, 0), Vector(0, 1, 0), 100)
    ]

    # Criando matriz de pixels
    image = np.zeros((camera_v_res, camera_h_res), dtype=np.uint8)

    # Testando interseções
    for j in range(camera_v_res):
        for i in range(camera_h_res):
            ray = camera.get_ray(i, j)
            closest_t = float('inf')
            color = 0
            
            for obj in objects:
                t = obj.intersect(ray)
                if t and t < closest_t:
                    closest_t = t
                    color = obj.color
            
            image[j, i] = color

    cv2.imshow("Ray Casting - Interseção com Esferas, Planos e Malhas de triângulos", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

   
