from triangle import Triangle
from transformation import Transformation
from intersection import Intersection
from vector import Vector
from material import Material

class Mesh:
    def __init__(self, vertices, faces, normals):
        self.triangles = []

        for face in faces:
            v0 = vertices[face.vertice_indices[0]]
            v1 = vertices[face.vertice_indices[1]]
            v2 = vertices[face.vertice_indices[2]]

            normal = None
            if face.normal_indices and face.normal_indices[0] < len(normals):
                normal = normals[face.normal_indices[0]]

            material = Material(
                ka=face.ka, 
                kd=face.kd, 
                ks=face.ks,    
                ke=face.ke,   
                ns=face.ns, 
                ni=face.ni, 
                d=face.d         
            )

            triangle = Triangle(
                v0=v0,
                v1=v1,
                v2=v2,
                normal=normal,
                material=material 
            )
            self.triangles.append(triangle)

    def transform(self, transformation_matrix):
        for triangle in self.triangles:
            triangle.transform(transformation_matrix)

    def intersect(self, ray):
        closest_t = float('inf')
        closest_hit = None
        for triangle in self.triangles:
            hit = triangle.intersect(ray)
            if hit and hit.t < closest_t:
                closest_t = hit.t
                closest_hit = hit
        return closest_hit