from color import Color
from transformation import Transformation

class TriangleMesh:
    def __init__(self, vertices, faces, normals, color):
        self.vertices = vertices 
        self.faces = faces
        self.normals = [Vector(n.x, n.y, n.z) for n in normals]
        self.color = color
        self.n_triangles = len(faces)
        self.n_vertices = len(vertices)
    
    def transform(self, transformation_matrix):
        self.vertices = [Transformation.apply_transformation(transformation_matrix, v) for v in self.vertices]
    
    def intersect(self, ray):
        closest_t = float('inf')
        hit = False

        print(f"Faces {self.n_triangles}:")
        
        for face in self.faces:
            print(f"rodou uma face")

            v0, v1, v2 = [self.vertices[i] for i in face]
            edge1 = v1 - v0
            edge2 = v2 - v0
            h = ray.direction.cross(edge2)
            a = edge1.dot(h)
            
            if -1e-6 < a < 1e-6:
                continue  # O raio é paralelo ao triângulo
            
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
                hit = True
        
        return closest_t if hit else None