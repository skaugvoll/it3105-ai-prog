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
    can = Canvas(root, width=560, height=560)
    can.pack()

    neuron = neurons[0]
    # one neuron = one picture, one picture has 784 pixels / rectangles
    # print(neuron)
    for neuron in neurons:
        drawOneNeuron(can, neuron)

def drawOneNeuron(can, neuron):
    idx = 0
    row = 0
    column = 0
    pixelsize = 2
    for p in neuron:
        if idx == 28:
            row += pixelsize + 1  # + 1 gives spacing
            column = 0
            idx = 0
        can.create_rectangle(column, row, column + pixelsize, row + pixelsize, fill="#FFF")
        idx += 1
        column += pixelsize + 1  # + 1 gives spacing


def run():
    gui = Tk()
    # data = loadData() # input data
    # draw(gui, data)


    neurons = generateNeurons() # randomly initialize 100 neruons with 784 pixlers each.
    draw(gui, neurons)
    mainloop()





run()