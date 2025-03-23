from intersection import Intersection
from vector import Vector
from transformation import Transformation

class Triangle:
    def __init__(self, v0, v1, v2, normal=None, material=None):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2
        self.material = material

        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0
        self.normal = (edge1.cross(edge2)).normalize() if not normal else normal

    def intersect(self, ray):
        EPSILON = 1e-6
        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0
        h = ray.direction.cross(edge2)
        a = edge1.dot(h)

        if -EPSILON < a < EPSILON:
            return None

        f = 1.0 / a
        s = ray.origin - self.v0
        u = f * s.dot(h)
        if u < 0.0 or u > 1.0:
            return None

        q = s.cross(edge1)
        v = f * ray.direction.dot(q)
        if v < 0.0 or u + v > 1.0:
            return None

        t = f * edge2.dot(q)
        if t > EPSILON:
            hit_point = ray.origin + ray.direction * t
            return Intersection(
                t=t,
                hit_point=hit_point,
                normal=self.normal,
                material=self.material  # aqui vai o Face que tem kd, ka, etc
            )
        else:
            return None

    def transform(self, matrix):
        self.v0 = Transformation.apply_transformation(matrix, self.v0)
        self.v1 = Transformation.apply_transformation(matrix, self.v1)
        self.v2 = Transformation.apply_transformation(matrix, self.v2)
        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0
        self.normal = edge1.cross(edge2).normalize()