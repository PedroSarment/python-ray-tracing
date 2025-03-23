from intersection import Intersection

class Plane:
    def __init__(self, point, normal, material):
        self.point = point
        self.normal = normal.normalize()
        self.material = material 

    def intersect(self, ray):
        denom = self.normal.dot(ray.direction)
        if abs(denom) > 1e-6:
            t = (self.point - ray.origin).dot(self.normal) / denom
            if t > 1e-4:
                hit_point = ray.origin + ray.direction * t
                return Intersection(
                    t=t,
                    hit_point=hit_point,
                    normal=self.normal,
                    material=self.material
                )
        return None