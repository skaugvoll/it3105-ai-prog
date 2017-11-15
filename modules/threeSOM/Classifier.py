from tkinter import *
import os
import numpy as np
import math
import time
from Neuron import Neuron
from scipy.spatial import distance

cwd = os.getcwd()
sys.path.append(cwd + "/mnist/")

import mnist_basics as MNIST

def converteFlatMnistTo2D():
    cases2D = []
    cases = MNIST.load_all_flat_cases() # returns [ [cases] , [targets] ] --> cases = [ [features...] ]

    for f, t in zip(cases[0], cases[1]):
        f = [feature / 255 for feature in f]
        case = [f,t]
        cases2D.append(case)
    return cases2D

def loadData(numTrain, numTest):
    ca = converteFlatMnistTo2D()
    np.random.shuffle(ca)
    return [ca[:numTrain], ca[numTrain:numTrain+numTest]]

def generateNeurons(numberOfNeurons=100, numberOfPixels=784, numberOfClasses=10):
    neurons = []
    split = np.floor(np.sqrt(numberOfNeurons))
    i = 1
    row = 0
    column = 0
    while i <= numberOfNeurons:
        if i % split == 0:
            row += 1
            column = 0
        neurons.append(Neuron(x=column, y=row, numberOfPixels=numberOfPixels, numberOfClasses=numberOfClasses))
        column += 1
        i += 1
    return neurons


def draw(canvas, neurons, dim=100):
    can = canvas

    # one neuron = one picture, one picture has 784 pixels / rectangles
    offsettRow = 0
    offsettCol = 0
    split = np.floor(np.sqrt(dim))
    i = 0
    for neuron in np.nditer(neurons, flags=["refs_ok"]):
        neuron = neuron.item()
        if i == split:
            offsettRow += 42
            offsettCol = 0
            i = 0
        elif i != 0:
            offsettCol += 42
        drawOneNeuron(can, neuron.weights, offsettRow, offsettCol)

        # can.update_idletasks()
        # can.update()

        i += 1
    can.update_idletasks()
    can.update()

def drawOneNeuron(can, neuron, row, col):
    idx = 0
    row = row
    column = col
    pixelsize = 1.5
    for p in np.nditer(neuron):
        # pixelValue = str(int(p*255))*3 #Gives RGB p = 255, --> 2552555255
        colorval = "#%02x%02x%02x" % (math.floor(p*255), math.floor(p*255), math.floor(p*255))
        if idx == 28:
            row += pixelsize  # + 1 gives spacing
            column = col
            idx = 0
        can.create_rectangle(column, row, column + pixelsize, row + pixelsize, fill=colorval)
        idx += 1
        column += pixelsize  # + 1 gives spacing

def findWinnerNeuron(case, neurons):
    winnerNeuron = None
    lowestDist = math.inf
    # for neuron in neurons:
    for neuron in np.nditer(neurons, flags=["refs_ok"]):
        neuron = neuron.item()
        dist = np.linalg.norm(case - neuron.weights)
        if dist < lowestDist:
            lowestDist = dist
            winnerNeuron = neuron
    return winnerNeuron


def run():
    gui = Tk()
    canvas = Canvas(gui, width=900, height=900)
    canvas.grid(row=0, column=0)
    infoText = Label(text='Epoc:     Step:    LR:    NBSize:  ')
    infoText.grid(row=1, column=0)

    numberOfTraningCases = 1000
    numberOfTestingCases = 100

    data = loadData(numberOfTraningCases, numberOfTestingCases) #input data only. no labels. Labels can be found in rawData
    testData = data[1]
    data = data[0]

    numberOfNeurons = 200
    numberOfPixels = 784
    numberOfClasses = 10
    neurons = np.array(generateNeurons(numberOfNeurons=numberOfNeurons, numberOfPixels=numberOfPixels, numberOfClasses=numberOfClasses)) # randomly initialize 100 neruons with 784 pixlers each.
    draw(canvas, neurons, dim=numberOfNeurons)

    maxEpoc = 30
    converged = False
    epoc = 1
    viewInterval = 5
    classificationInterval = 10
    initneighborhoodSize = 10
    ###  TRAINING EPOCS
    s1 = time.time()

    # while epoc < maxEpoc and not converged:
    for epoc in range(1,maxEpoc+1):
        # learningRate = 1 / (epoc ** (1 / 4))
        learningRate = np.exp(-epoc / 16)
        if epoc == 1:
            neighborhoodSize = initneighborhoodSize
        else:
            # neighborhoodSize = neighborhoodSize * (1 - 0.01 * epoc)
            neighborhoodSize = initneighborhoodSize * np.exp(-epoc / 10) # 10 = constant

        ### STEPS
        for case in data:
            winnerNeuron = findWinnerNeuron(case[0], neurons)

            if epoc % classificationInterval == 0:
                label = case[1]
                winnerNeuron.winnerlabels[label] += 1

            ## UPDATE ALL NEURONS ? or update Winner and some Neighbours
            for neuron in np.nditer(neurons, flags=["refs_ok"]):
                neuron = neuron.item()
                #distance = distansen i grid og ikke bilder. så x og y kordinater i grid.
                # dist = distance.euclidean(winnerCoordinates, neuronCoord)
                dist = abs(neuron.x - winnerNeuron.x) + abs(neuron.y - winnerNeuron.y)

                neighborhoodMembership = np.exp(-dist ** 2 / neighborhoodSize ** 2)
                neuron.weights = np.add(neuron.weights, np.prod([np.array([learningRate]), np.array([neighborhoodMembership]), np.subtract(case[0], neuron.weights)]))
            # infoText.config(text='Epoc: {:d}   Step: {:d}  LR: {:.2f}  NBSize: {:.2f}'.format(epoc, case, learningRate, neighborhoodSize))
            # infoText.update()
        
        if epoc % classificationInterval == 0:
            # print('########### Kth Epoc')
            for neuron in np.nditer(neurons, flags=["refs_ok"]):
                neuron = neuron.item()
                neuron.currentLabel = np.where(neuron.winnerlabels == neuron.winnerlabels.max())[0][0]
                # print("Neuron x:{:d},y:{:d} = {:d} number".format(neuron.x, neuron.y, neuron.currentLabel))

        if epoc % viewInterval == 0:
            draw(canvas, neurons, dim=numberOfNeurons)

        # epoc += 1

    ### TODO: Look for convergens : if we under training had 60 % correct, and now we still have 60%, then convergence... ?? --> da må vi sjekke hvor mange vi har rette

    s2 = time.time()
    s3 = time.time()

    ### TODO: CLASSIFY IMAGES / TESTING --> Turn of learning, see if the winenr neuron is the same "class" as the image / input target

    correct = 0
    for case in range(numberOfTestingCases):
        winnerNeuron = findWinnerNeuron(testData[case][0], neurons)
        correctLabel = testData[case][1]
        predictedLabel = winnerNeuron.currentLabel
        if correctLabel == predictedLabel: correct += 1

    s4 = time.time()
    print('Number of test cases: {:d}\nNumber of correct classifications: {:d}\n= {:.5f}% correct '.format(numberOfTestingCases, correct, correct/numberOfTestingCases))
    s5 = time.time()
    correct = 0
    for case in range(numberOfTestingCases):
        winnerNeuron = findWinnerNeuron(data[case][0], neurons)
        correctLabel = data[case][1]
        predictedLabel = winnerNeuron.currentLabel
        if correctLabel == predictedLabel: correct += 1

    s6 = time.time()
    print('\nNumber of seen training cases: {:d}\nNumber of correct classifications: {:d}\n= {:.5f}% correct '.format(numberOfTestingCases,correct,correct / numberOfTestingCases))

    print()
    print(s2-s1, ' seconds -->', (s2-s1)/60,'minutes')
    print(s4 - s3)
    print(s6-s5)

    dump = False
    if dump:
        with open('weights.txt','w') as file:
            file.write(str(numberOfNeurons) + " " + str(numberOfPixels)+'\n')
            for neuron in np.nditer(neurons, flags=["refs_ok"]):
                neuron = neuron.item().weights
                file.write(str(neuron)+'\n')


run()

