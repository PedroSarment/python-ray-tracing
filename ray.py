
from point import Point
from vector import Vector


class Ray:
    def __init__(self, origin: Point, direction: Vector):
        self.origin = origin 
        self.direction = direction.normalize()
    
