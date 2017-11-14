import numpy as np

class Neuron:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.weights = np.random.rand(1, 784)[0]
        self.winnerlabels = np.zeros((1,10))[0] # index 0 = tallet 0, index 1 = tallet 1, etc.
        self.currentLabel = None
        self.nn = None
        self.ns = None
        self.ne = None
        self.nw = None
