class Plane:
    def __init__(self, point, normal, color):
        self.point = point
        self.normal = normal.normalize()
        self.color = color
    
    def intersect(self, ray):
        denom = self.normal.dot(ray.direction)
        if abs(denom) > 1e-6:
            t = (self.point - ray.origin).dot(self.normal) / denom
            return t if t > 0 else None
        return None