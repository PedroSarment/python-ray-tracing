import numpy as np
from intersection import Intersection

class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    
    def intersect(self, ray):
        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius ** 2
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return None
        else:
            t1 = (-b - np.sqrt(discriminant)) / (2 * a)
            t2 = (-b + np.sqrt(discriminant)) / (2 * a)
            t = min(t1, t2) if t1 > 1e-4 else t2
            if t > 1e-4:
                hit_point = ray.origin + ray.direction * t
                normal = (hit_point - self.center).normalize()
                return Intersection(t, hit_point, normal, self.material)
            return None
