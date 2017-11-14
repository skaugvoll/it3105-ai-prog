import numpy as np

class Neuron:
    def __init__(self, x=None, y=None, numberOfPixels=784, numberOfClasses=10):
        self.x = x
        self.y = y
        self.weights = np.random.rand(1, numberOfPixels)[0]
        self.winnerlabels = np.zeros((1,numberOfClasses))[0] # index 0 = tallet 0, index 1 = tallet 1, etc.
        self.currentLabel = None
