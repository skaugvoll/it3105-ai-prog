import os
import random
import re
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
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
    slice = 2 * math.pi / (len(points) * 2);
    for i in range(len(points) * 2):
        angle = slice * i
        newX = 0.5 + (0.2 * math.cos(angle))
        newY = 0.5 + (0.2 * math.sin(angle))
        neurons.append([newX, newY])

    return neurons

# For each iteration, this funktion plots input points and neurons into matplotlib
def plotPoints(inputs, neurons):
    plt.clf()
    nx, ny = neurons.T
    plt.scatter(nx, ny, color="red")
    plt.plot(nx, ny, color="black")

    px, py = inputs.T
    plt.ylim([-0.02, 1.02])
    plt.xlim([-0.02, 1.02])
    plt.scatter(px, py)

    plt.draw()
    plt.pause(0.00000003)

# Finds the closest neuron with weuqlidian distance.
def findAndUpdateWinnerNeuron(inputPoint, neurons):
    winnerNeuronIndex = None
    lowestDist = math.inf
    for i in range(len(neurons)):
        dist = distance.euclidean(inputPoint, neurons[i])
        if dist < lowestDist:
            lowestDist = dist
            winnerNeuronIndex = i

    return updateNeuron(inputPoint, neurons, winnerNeuronIndex)

# updates the closest neuron and moves it towards the input point.
def updateNeuron(inputPoint, neurons, winnerIndex):
    lr = 0.3
    dirX = lr * (neurons[winnerIndex][0] - inputPoint[0])
    dirY = lr * (neurons[winnerIndex][1] - inputPoint[1])
    neurons[winnerIndex][0] -= dirX
    neurons[winnerIndex][1] -= dirY

    return neurons

def run():
    points = readFile()
    maxVal = np.amax(points)  # Find the biggest value in the array to use for scaling
    inputs = np.array(points) / maxVal  # Make np.array and scale the values (between 0 and 1)

    neurons = generateNeurons(points)
    neurons = np.array(neurons)

    plotPoints(inputs, neurons)

    for i in range(200):
        randInput = random.randint(0, len(points) - 1)
        neurons = findAndUpdateWinnerNeuron(inputs[randInput], neurons)
        plotPoints(inputs, neurons)

# TODO: oppdatere naboene til vinner-neuron og flytte disse mot input point som bli sjekket. Skal ikke flyttes like langt som vinner-neuron. Tror man kan regne ut naboer med euqlidian distance for å finne de to nærmeste
# Litt usikker på hva mer som må gjøres. Sjekk link jeg sendte deg på messenger

run()