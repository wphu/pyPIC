import numpy as np

class ElectroMagn:
    def __init__(self, dims, cell_length):
        self.dims = dims + (3,)
        self.cell_length = cell_length

        self.E = np.zeros(self.dims, dtype = float)
        self.B = np.zeros(self.dims, dtype = float)
