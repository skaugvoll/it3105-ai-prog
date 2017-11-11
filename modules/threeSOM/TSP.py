import os
import random
import re
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from time import sleep
import matplotlib.animation as animation


# Read all input points from file and makes a 2d array. [[x,y], [x,y]]
def readFile():
    filepath = os.getcwd() + "/Data/1.txt"

    points = []

    with open(filepath) as FileObj:
        for caseline in FileObj:
            caseline = caseline.rstrip()  # remove newline character

            c = re.split(" ", caseline)  # make a list out of line
            if c[0].isdigit():
                c = c[1:]
                c = list(map(lambda x: float(x), c))  # make elements float
                points.append(c)

    return points

# Generates a circle of neurons in the middle og the plot.
def generateNeurons(points):
    neurons = []
    slice =  2 * math.pi / (len(points) * 2)
    for i in range(len(points) * 2):
        angle = slice * i
        newX = 0.5 + (0.2 * math.cos(angle))
        newY = 0.5 + (0.2 * math.sin(angle))
        neurons.append([newX, newY])

    return neurons

# For each iteration, this function plots input points and neurons into matplotlib
def plotPoints(inputs, neurons, step=''):
    plt.clf()
    nx, ny = neurons.T
    plt.scatter(nx, ny, color='red')
    plt.plot(nx, ny, color="black")

    px, py = inputs.T
    plt.ylim([-0.02, 1.02])
    plt.xlim([-0.02, 1.02])
    plt.scatter(px, py)

    plt.figtext(0.02, 0.02, "Step: " + str(step))
    plt.draw()
    plt.pause(0.00000003)

# Finds the closest neuron with euclidean distance.
def findWinnerNeuron(inputPoint, neurons):
    winnerNeuronIndex = None
    lowestDist = math.inf
    for i in range(len(neurons)):
        dist = distance.euclidean(inputPoint, neurons[i])
        if dist < lowestDist:
            lowestDist = dist
            winnerNeuronIndex = i
    return winnerNeuronIndex

# updates the closest neuron and moves it towards the input point.
def updateNeuron(inputPoint, neurons, winnerIndex, neighborhoodShip=None, lr=0.3, decay=1):
    dirX = lr * (neurons[winnerIndex][0] - inputPoint[0]) * decay
    dirY = lr * (neurons[winnerIndex][1] - inputPoint[1]) * decay
    # dirX = neurons(winnerIndex)[0] + lr * neighborhoodShip * (inputPoint[0] - neurons[winnerIndex][0])
    # dirY = neurons(winnerIndex)[1] + lr * neighborhoodShip * (inputPoint[1] - neurons[winnerIndex][1])
    neurons[winnerIndex][0] -= dirX
    neurons[winnerIndex][1] -= dirY

    return neurons


def run():
    points = readFile()
    maxVal = np.amax(points)  # Find the biggest value in the array to use for scaling
    inputs = np.array(points) / maxVal  # Make np.array and scale the values (between 0 and 1)

    neurons = generateNeurons(points * 2)
    neurons = np.array(neurons)

    plotPoints(inputs, neurons)

    i = 1
    viewInterval = 250
    neighborhoodSize = 10
    learningRate = 0.5
    converged = False
    while i < 5000 and not converged:
        for c in inputs:
            randInput = random.randint(0, len(points) - 1)
            winnerIndex = findWinnerNeuron(inputs[randInput], neurons)
            neurons = updateNeuron(inputs[randInput], neurons, winnerIndex, lr=learningRate)

            # find neighbours
            learningRate = 1 / i ** (1 / 4)

            if i == 1:
                neighborhoodSize = 10
            else:
                neighborhoodSize = max(int(neighborhoodSize * (1 - 0.01 * i)), 2)

            neighborhood = []
            for n in range(1, neighborhoodSize+1):
                if winnerIndex == 0:
                    neighborhood.append(len(neurons) - n)
                elif winnerIndex == len(neurons) - n:
                    neighborhood.append(winnerIndex - n)
                    neighborhood.append(0)
                else:
                    neighborhood.append(winnerIndex - n)
                    neighborhood.append(winnerIndex + n)


            for neighborIndex in neighborhood:
                # update their weights
                neurons = updateNeuron(inputs[randInput], neurons, neighborIndex, decay=0.5, lr=learningRate)

                if i % viewInterval == 0:
                    plotPoints(inputs, neurons, step=i)

        i += 1
        # TODO: fix at den sjekker om vi har funent convergens

    # TODO : Gå gjennom alle byer, og finn nærmeste neuron. Så må vi mappe det på en måte, slik at vi får neuron: by, Så gå gjennom neuronene i den ringrekkefølgen de ligger i, og sjekker om de har en by, isåfall legg til avstanden mellom dette nehronet og neste neuron
    paths = {}
    dist = 0
    for city in inputs:
        paths[str(city)] = findWinnerNeuron(city, neurons)
        dist += distance.euclidean(city, paths[str(city)])

    print('Path dist: {:.2f}km\nOptimal dist: {:.2f}km\n= {:.2f}%'.format(dist, 7542, (dist/7542)))
    sleep(10)



run()