from tkinter import *
import os
import numpy as np
import math
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



def draw(root, neurons, dim=10):
    can = Canvas(root, width=900, height=900)
    can.pack()

    # one neuron = one picture, one picture has 784 pixels / rectangles
    # print(neuron)
    # drawOneNeuron(can, neuron, 0, 0, "red")
    # drawOneNeuron(can, neuron, 84, 0, "red")
    # drawOneNeuron(can, neuron, 0, 0, "red")
    # drawOneNeuron(can, neuron, 0, 0, "red")
    offsettRow = 0
    offsettCol = 0
    for n in range(len(neurons)):
        neuron = neurons[n]
        if n % dim == 0:
            offsettRow += 84
            offsettCol = 0
        else:
            offsettCol += 84
        drawOneNeuron(can, neuron, offsettRow, offsettCol, "black")


def drawOneNeuron(can, neuron, row, col, color):
    idx = 0
    row = row
    column = col
    pixelsize = 2
    for p in neuron:
        pixelValue = str(int(p*255))*3 #Gives RGB p = 255, --> 2552555255
        if idx == 28:
            row += pixelsize  # + 1 gives spacing
            column = col
            idx = 0
        can.create_rectangle(column, row, column + pixelsize, row + pixelsize, fill="#"+pixelValue)
        idx += 1
        column += pixelsize  # + 1 gives spacing


def run():
    gui = Tk()
    # data = loadData() # input data
    # draw(gui, data)


    neurons = generateNeurons() # randomly initialize 100 neruons with 784 pixlers each.
    draw(gui, neurons)
    mainloop()





run()