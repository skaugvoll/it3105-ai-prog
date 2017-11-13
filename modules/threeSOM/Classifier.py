from tkinter import *
import os
import numpy as np
import math
from time import sleep
from Neuron import Neuron
from scipy.spatial import distance

cwd = os.getcwd()
sys.path.append(cwd + "/mnist/")

import mnist_basics as MNIST

def converteFlatMnistTo2D():
    cases2D = []
    cases = MNIST.load_all_flat_cases() # returns [ [cases] , [targets] ] --> cases = [ [features...] ]

    for f, t in zip(cases[0], cases[1]):
        # f = [feature / 255 for feature in f]
        case = [f,t]
        cases2D.append(case)
    return cases2D

def loadData():
    ca = converteFlatMnistTo2D()
    np.random.shuffle(ca)
    return ca[:500]

def generateNeurons(numberOfNeurons=100, pixler=784):
    return np.random.rand(numberOfNeurons, pixler)



def draw(canvas, neurons, dim=100):
    can = canvas

    # one neuron = one picture, one picture has 784 pixels / rectangles

    offsettRow = 0
    offsettCol = 0
    split = np.floor(np.sqrt(dim))
    i = 1
    for n in range(len(neurons)):
        neuron = neurons[n]
        if i == split:
            offsettRow += 84
            offsettCol = 0
            i = 1
        elif i != 1:
            offsettCol += 84
        drawOneNeuron(can, neuron, offsettRow, offsettCol)

        can.update_idletasks()
        can.update()

        i += 1


def drawOneNeuron(can, neuron, row, col):
    idx = 0
    row = row
    column = col
    pixelsize = 2
    for p in neuron:
        # pixelValue = str(int(p*255))*3 #Gives RGB p = 255, --> 2552555255
        colorval = "#%02x%02x%02x" % (math.floor(p*255), math.floor(p*255), math.floor(p*255))
        if idx == 28:
            row += pixelsize +1  # + 1 gives spacing
            column = col
            idx = 0
        can.create_rectangle(column, row, column + pixelsize, row + pixelsize, fill=colorval)
        idx += 1
        column += pixelsize + 1  # + 1 gives spacing

def findWinnerNeuron(case, neurons):
    winnerNeuronIndex = None
    lowestDist = math.inf
    for i in range(len(neurons)):
        dist = np.linalg.norm(case - neurons[i])
        if dist < lowestDist:
            lowestDist = dist
            winnerNeuronIndex = i
    return winnerNeuronIndex


def getCoordinates(idx):
    if idx < 10:
        return [0, idx]
    else:
        num = str(idx)
        return [int(num[:1]), int(num[1:])]


def run():
    gui = Tk()
    canvas = Canvas(gui, width=900, height=900)
    canvas.pack()
    rawData = loadData()
    data = rawData[0] #input data only. no labels. Labels can be found in rawData
    print(rawData)

    neurons = generateNeurons() # randomly initialize 100 neruons with 784 pixlers each.
    draw(canvas, neurons)


    maxEpoc = 100
    converged = False
    epoc = 1
    viewInterval = 10
    classificationInterval = 10
    neighborhoodSize = 10
    ###  TRAINING EPOCS
    while epoc < maxEpoc and not converged:
        learningRate = 1 / (epoc ** (1 / 4))

        if epoc == 1:
            neighborhoodSize = 10
        else:
            neighborhoodSize = neighborhoodSize * (1 - 0.01 * epoc)

        ### STEPS
        for case in range(len(data)):
            winnerNeuron = findWinnerNeuron(data[case], neurons)
            winnerCoordinates = getCoordinates(winnerNeuron)

            ## UPDATE ALL NEURONS ? or update Winner and some Neighbours
            for idx in range(len(neurons)):
                #distance = distansen i grid og ikke bilder. så x og y kordinater i grid.
                neuronCoord = getCoordinates(idx)
                dist = distance.euclidean(winnerCoordinates, neuronCoord)

                neighborhoodMembership = np.exp(-dist ** 2 / neighborhoodSize ** 2)
                neurons[idx] = np.add(neurons[idx], (learningRate * neighborhoodMembership * np.subtract(data[case], neurons[idx])))

        if epoc % viewInterval == 0:
            draw(canvas, neurons)

        epoc += 1

    ### TODO: CLASSIFY EACH FUCKING NEURON


    ### TODO: CLASSIFY IMAGES


run()