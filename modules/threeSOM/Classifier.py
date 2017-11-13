from tkinter import *
import os
import numpy as np
import time
from Neuron import Neuron

cwd = os.getcwd()
sys.path.append(cwd + "/mnist/")

import mnist_basics as MNIST



def loadData():
    ca = np.array(MNIST.load_all_flat_cases()[0])
    np.random.shuffle(ca)
    return ca[:500]

def generateNeurons(numberOfNeurons=100, pixler=784):
    return np.random.rand(numberOfNeurons, pixler)



def draw(root, neurons):
    w = Canvas(root, width=560, height=560)
    w.pack()

    # one neuron = one picture, one picture has 784 pixels / rectangles
    pixelSize = 20
    for n in range(len(neurons)):
        neuron = neurons[n]
        for pixel in range(len(neuron)):
            pixelValue = neuron[pixel]
            row = 0
            column = 0
            if pixel % 28 == 0:
                row += 1
                column = 0
            w.create_rectangle(row, column, row + pixelSize, column + pixelSize, fill='#606060')
            column += pixelSize
            row += pixelSize


def run():
    gui = Tk()
    # data = loadData() # input data

    neurons = generateNeurons() # randomly initialize 100 neruons with 784 pixlers each.
    draw(gui, neurons)
    mainloop()





run()