import numpy as np
from vector import Vector

class Material:
    def __init__(self, ka, kd, ks, kr, kt, eta):
        self.ka = self._convert(ka)
        self.kd = self._convert(kd)
        self.ks = self._convert(ks)
        self.kr = self._convert(kr)
        self.kt = self._convert(kt)
        self.eta = eta

    def _convert(self, value):
        if isinstance(value, Vector):
            return value.to_numpy_array()
        return np.array(value, dtype=np.float32)