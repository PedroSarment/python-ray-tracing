import numpy as np

class Light:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = np.array(intensity)