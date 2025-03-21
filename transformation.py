
import numpy as np
from point import Point

class Transformation:
    @staticmethod
    def translation(tx, ty, tz):
        return np.array([
            [1, 0, 0, tx],
            [0, 1, 0, ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def scaling(sx, sy, sz):
        return np.array([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def rotation_x(angle):
        c, s = np.cos(angle), np.sin(angle)
        return np.array([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def rotation_y(angle):
        c, s = np.cos(angle), np.sin(angle)
        return np.array([
            [c, 0, s, 0],
            [0, 1, 0, 0],
            [-s, 0, c, 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def rotation_z(angle):
        c, s = np.cos(angle), np.sin(angle)
        return np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])


    @staticmethod
    def apply_transformation(matrix, point):
        p = np.array([point.x, point.y, point.z, 1])
        transformed_p = matrix @ p
        return Point(transformed_p[0], transformed_p[1], transformed_p[2])