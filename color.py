import numpy as np

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def array(self):
        return np.array([self.r, self.g, self.b], dtype=np.uint8)