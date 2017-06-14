import numpy as np

class Particle:
    def __init__(self, q, m):
        self.q = q
        self.m = m

        self.x = np.zeros((3), dtype = float)
        self.v = np.zeros((3), dtype = float)
