import math
import numpy as np


class Vector:

    def __init__(self, x: float, y: float, z:float):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def to_array(self):
        return np.array([self.x, self.y, self.z])
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vector(self.x * other, self.y * other, self.z * other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def normalize(self):
        mag = self.magnitude()
        return Vector(self.x / mag, self.y / mag, self.z / mag) if mag != 0 else Vector(0, 0, 0)
    
    def rotateX (self, alpha):
        ry = math.cos(alpha) * self.y - math.sin(alpha) * self.z
        rz = math.sin(alpha) * self.y + math.cos(alpha) * self.z

        return Vector(self.x, ry, rz)

    def rotateY(self, alpha):
        rx = math.cos(alpha) * self.x + math.sin(alpha) * self.z
        rz = -math.sin(alpha) * self.x + math.cos(alpha) * self.z

        return Vector(rx, self.y, rz)

    def rotateZ(self, alpha):
        rx = math.cos(alpha) * self.x - math.sin(alpha) * self.y
        ry = math.sin(alpha) * self.x + math.cos(alpha) * self.y

        return Vector(rx, ry, self.z)

    def translateX (self, num):
        return Vector(self.x + num, self.y, self.z)

    def translateY (self, num):
        return Vector(self.x, self.y + num, self.z)
    
    def translateZ (self, num):
        return Vector(self.x, self.y, self.z + num)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def angle(self, other):
        EPSILON = 1e-6
        cost = self.dot(other) / (self.norm() * other.norm())
        cost = min(max(cost, -1 + EPSILON), 1.0 - EPSILON)

        return math.acos(cost)

    def magnitude(self):
        return np.linalg.norm(self.to_array())

    def to_numpy_array(self):
        return np.array([self.x, self.y, self.z], dtype=np.float32)
        