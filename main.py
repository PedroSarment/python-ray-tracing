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
from mesh import Mesh
from transformation import Transformation
import copy
from second_delivery import secondDelivery
from material import Material
from light import Light
from scene import Scene
from phong import Phong
from third_delivery import thirdDelivery
from render import Render
from fourth_delivery import fourthDelivery
from first_delivery import firstDelivery

def main():

    #image = firstDelivery()

    image = secondDelivery()

    #image = thirdDelivery()

    #image = fourthDelivery()


    cv2.imshow("Ray Casting - Interseção com Esferas, Planos e Malhas de triângulos", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

   
