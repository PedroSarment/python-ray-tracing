from vector import Vector

class Point:
    """
    Representa um ponto em um espaço tridimensional.

    Atributos:
        x (float): Coordenada X do ponto.
        y (float): Coordenada Y do ponto.
        z (float): Coordenada Z do ponto.
    """

    def __init__(self, x: float, y: float, z:float):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
 
    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
           
    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Vector):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Subtração apenas entre dois pontos ou entre um ponto e um vetor.")
    
    def scale(self, factor):
        return Point(self.x * factor, self.y * factor, self.z * factor)
    
    def reflect_xy(self):
        return Point(self.x, self.y, -self.z)
    
    def reflect_xz(self):
        return Point(self.x, -self.y, self.z)
    
    def reflect_yz(self):
        return Point(-self.x, self.y, self.z)
    
    def distance_to_plane(self, normal, point_on_plane):
        if isinstance(normal, Vector) and isinstance(point_on_plane, Point):
            d = -normal.dot(Vector(*point_on_plane.to_array()))
            return abs(normal.dot(Vector(*self.to_array())) + d) / normal.magnitude()
        raise TypeError("Normal deve ser um Vector e ponto no plano deve ser Point.")
    
    def distance_to_line(self, line_point, line_vector):
        if isinstance(line_point, Point) and isinstance(line_vector, Vector):
            return np.linalg.norm(np.cross(self.to_array() - line_point.to_array(), line_vector.to_array())) / line_vector.magnitude()
        raise TypeError("line_point deve ser Point e line_vector deve ser Vector.")
    