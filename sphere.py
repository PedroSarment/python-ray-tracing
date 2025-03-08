class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
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
            return min(t1, t2) if t1 > 0 else t2 if t2 > 0 else None