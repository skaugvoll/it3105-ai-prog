import numpy as np

class Neuron:
    def __init__(self, x=None, y=None, weights=None):
        self.x = x,
        self.y = y,
        self.weights = np.random.rand(1, 784),
        self.nn = None
        self.ns = None
        self.ne = None
        self.nw = None
