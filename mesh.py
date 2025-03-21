from color import Color
from transformation import Transformation
from material import Material
from intersection import Intersection
from vector import Vector

class TriangleMesh:
    def __init__(self, vertices, faces, normals, material):
        self.vertices = vertices 
        self.faces = faces
        self.normals = [Vector(n.x, n.y, n.z) for n in normals]
        self.material = material
        self.n_triangles = len(faces)
        self.n_vertices = len(vertices)
    
    def transform(self, transformation_matrix):
        self.vertices = [Transformation.apply_transformation(transformation_matrix, v) for v in self.vertices]
    
    def intersect(self, ray):
        closest_t = float('inf')
        hit_data = None

        for face in self.faces:
            v0, v1, v2 = [self.vertices[i] for i in face]
            edge1 = v1 - v0
            edge2 = v2 - v0
            h = ray.direction.cross(edge2)
            a = edge1.dot(h)
            
            if -1e-6 < a < 1e-6:
                continue
            
            f = 1.0 / a
            s = ray.origin - v0
            u = f * s.dot(h)
            if u < 0.0 or u > 1.0:
                continue
            
            q = s.cross(edge1)
            v = f * ray.direction.dot(q)
            if v < 0.0 or u + v > 1.0:
                continue
            
            t = f * edge2.dot(q)
            if t > 1e-6 and t < closest_t:
                closest_t = t
                hit_point = ray.origin + ray.direction * t
                normal = edge1.cross(edge2).normalize()
                hit_data = Intersection(
                    t=t,
                    hit_point=hit_point,
                    normal=normal,
                    material=self.material
                )
        
        return hit_data