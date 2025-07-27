import numpy as np
from vector import Vector

class Material:
    def __init__(self, ka, kd, ks, ke=None, ns=0, ni=1.0, d=1.0):
        # Coeficiente ambiental: influencia a luz ambiente
        self.ka = ka

        # Coeficiente difuso: cor do objeto iluminado
        self.kd = kd

        # Coeficiente especular: reflexo especular da luz
        self.ks = ks

        # Cor emissiva: luz emitida pelo objeto
        self.ke = ke if ke else Vector(0, 0, 0)

        # Brilho Phong
        self.ns = ns

        # Índice de refração do material 
        self.ni = ni

        # Opacidade
        self.d = d

        # reflectance = min(max((self.ni - 1) / (self.ni + 1), 0), 1)
        # self.kr = self.ks * reflectance

        transmission = 1.0 - self.d
        self.kt = Vector(transmission, transmission, transmission)


    