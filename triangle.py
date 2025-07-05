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
        
        # Calcula as duas arestas do triângulo para formar o plano
        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0

        # Calcula o vetor perpendicular ao plano do triângulo
        h = ray.direction.cross(edge2)

        # Calcula o determinante
        a = edge1.dot(h)

        # Verifica se o raio é paralelo ao triângulo
        if -EPSILON < a < EPSILON:
            return None

        # Calcula as coordenadas baricêntricas
        f = 1.0 / a
        s = ray.origin - self.v0
        u = f * s.dot(h)
        if u < 0.0 or u > 1.0:
            return None
        
        q = s.cross(edge1)
        v = f * ray.direction.dot(q)
        if v < 0.0 or u + v > 1.0:
            return None

        # calcula a distancia do ponto de interseção
        t = f * edge2.dot(q)
        if t > EPSILON:
            # Calcula o ponto de interseção
            hit_point = ray.origin + ray.direction * t
            return Intersection(
                t=t,
                hit_point=hit_point,
                normal=self.normal,
                material=self.material
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