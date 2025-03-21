import numpy as np

class Scene:
    def __init__(self, lights, ambient):
        self.lights = lights
        self.ambient = np.array(ambient)