import numpy as np

class Color:
    def __init__(self, r, g, b):
        self.r = float(r)
        self.g = float(g)
        self.b = float(b)

    def array(self):
        return np.array([self.r, self.g, self.b], dtype=np.uint8)

    def to_numpy(self):
        return np.array([self.r, self.g, self.b], dtype=np.float32)

    def clip(self):
        """
        Garante que os valores estejam no intervalo [0, 255]
        e retorna um novo objeto Color clamped.
        """
        r = np.clip(self.r, 0, 255)
        g = np.clip(self.g, 0, 255)
        b = np.clip(self.b, 0, 255)
        return Color(r, g, b)

    def __add__(self, other):
        if isinstance(other, Color):
            return Color(self.r + other.r, self.g + other.g, self.b + other.b)
        elif isinstance(other, (int, float)):
            return Color(self.r + other, self.g + other, self.b + other)
        else:
            raise TypeError("Unsupported operand type for +")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Color(self.r * other, self.g * other, self.b * other)
        elif isinstance(other, Color):
            return Color(self.r * other.r, self.g * other.g, self.b * other.b)
        elif isinstance(other, (np.ndarray, list, tuple)):
            return Color(self.r * other[0], self.g * other[1], self.b * other[2])
        elif hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):  # Suporte a Vector
            return Color(self.r * other.x, self.g * other.y, self.b * other.z)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return f"Color({self.r:.1f}, {self.g:.1f}, {self.b:.1f})"