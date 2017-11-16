import os
import random
import re
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from time import sleep
import matplotlib.animation as animation

class TSP:

    def __init__(self, filename, lrate, maxepochs, xneurons, nhsize):
        self.filename = filename
        self.lrate = lrate
        self.maxepochs = maxepochs
        self.xneurons = xneurons
        self.nhsize = nhsize
        self.optimalDist = self.findOptimalDist(filename)
        self.numLowChange = 0
        self.run()

    # Read all input points from file and makes a 2d array. [[x,y], [x,y]]
    def readFile(self):
        filepath = os.getcwd() + "/Data/"+self.filename+".txt"

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

    def findOptimalDist(self, filename):
        filepath = os.getcwd() + "/Data/optimal.txt"

        with open(filepath) as FileObj:
            for caseline in FileObj:
                caseline = caseline.rstrip()  # remove newline character

                c = re.split(": ", caseline)  # make a list out of line
                if c[0] == filename:
                    return int(c[1])

    # Generates a circle of neurons in the middle of the plot.
    def generateNeurons(self, points, circleX, circleY):
        neurons = []
        slice =  2 * math.pi / (points * self.xneurons)
        for i in range(points * self.xneurons):
            angle = slice * i
            # newX = 0.5 + (0.4 * math.cos(angle))
            # newY = 0.2 + (0.4 * math.sin(angle))
            newX = circleX + ((circleX/2) * math.cos(angle))
            newY = circleY + ((circleY/2) * math.sin(angle))
            neurons.append([newX, newY])

        return neurons

    # For each iteration, this function plots input points and neurons into matplotlib
    def plotPoints(self, inputs, neurons, epoch='',step='', lr=0.5, nbhd=10):
        plt.clf()
        nx, ny = neurons.T
        connectionX = [neurons[0][0], neurons[-1][0]]
        connectionY = [neurons[0][1], neurons[-1][1]]
        plt.scatter(nx, ny, color='red')
        plt.plot(nx, ny, color="black")
        plt.plot(connectionX, connectionY, color="green")

        px, py = inputs.T
        # plt.ylim([-0.02, 1.02])
        # plt.xlim([-0.02, 1.02])
        plt.scatter(px, py)

        plt.figtext(0.02, 0.02, "Epoch: {:d}  LR: {:.2f}    Nbhd: {:.2f}".format(epoch, lr, nbhd))
        plt.draw()
        plt.pause(0.00000003)

    # Finds the closest neuron with euclidean distance.
    def findWinnerNeuron(self, inputPoint, neurons):
        winnerNeuronIndex = None
        lowestDist = math.inf
        for i in range(len(neurons)):
            dist = np.linalg.norm(inputPoint - neurons[i])
            # dist = distance.euclidean(inputPoint, neurons[i])
            if dist < lowestDist:
                lowestDist = dist
                winnerNeuronIndex = i
        if lowestDist < 0.00001:
            self.numLowChange += 1
        return winnerNeuronIndex

    # updates the closest neuron and moves it towards the input point.
    def updateNeuron(self, inputPoint, neurons, winnerIndex, neighborhoodShip=None, lr=0.3, decay=1):
        dirX = lr * (inputPoint[0] - neurons[winnerIndex][0]) * decay
        dirY = lr * (inputPoint[1] - neurons[winnerIndex][1]) * decay

        neurons[winnerIndex][0] -= dirX
        neurons[winnerIndex][1] -= dirY

        return neurons


    def run(self, ):
        points = self.readFile()
        maxVal = np.amax(points)  # Find the biggest value in the array to use for scaling
        inputs = np.array(points) / maxVal  # Make np.array and scale the values (between 0 and 1)

        ix, iy = inputs.T
        circleX = np.average(ix)
        circleY = np.average(iy)

        neurons = self.generateNeurons(len(points) * 1, circleX, circleY)
        neurons = np.array(neurons)

        self.plotPoints(inputs, neurons, epoch=0, step=0)

        # sleep(10)

        i = 1
        viewInterval = 1
        neighborhoodSize = 20
        converged = False
        while i < self.maxepochs and not converged:
            learningRate = 1 / (i ** (1 / self.lrate))
            # learningRate = np.exp(-1 / 100)

            if i == 1:
                neighborhoodSize = self.nhsize
            else:
                # neighborhoodSize = 10 * (np.exp(-i / 100))
                neighborhoodSize = neighborhoodSize * (1 - 0.01 * i)

            for c in range(len(inputs)):
                # randInput = random.randint(0, len(points) - 1)
                winnerIndex = self.findWinnerNeuron(inputs[c], neurons)
                if self.numLowChange > 10:
                    converged = True


                for idx in range(len(neurons)):
                    #### Wrapper for å finne korteste vei i sirkelen (type wraparound list)
                    distClockwise = np.abs(idx - winnerIndex)
                    distCounterClockwise = np.abs(len(neurons)  - distClockwise)
                    dist = np.minimum(distClockwise, distCounterClockwise)
                    ####
                    neighborhoodMembership = np.exp(-dist ** 2 / neighborhoodSize ** 2)
                    neurons[idx][0] = np.add(neurons[idx][0], np.prod([learningRate,neighborhoodMembership,(inputs[c][0] - neurons[idx][0])]))
                    neurons[idx][1] = np.add(neurons[idx][1], np.prod([learningRate,neighborhoodMembership,(inputs[c][1] - neurons[idx][1])]))


            if i % viewInterval == 0:
                self.plotPoints(inputs, neurons, epoch=i, step=c, lr=learningRate, nbhd=neighborhoodSize)

            # TODO: fix at den sjekker om vi har funent convergens


            i += 1


        paths = {}
        for city in range(len(inputs)):
            nearestNeuron = self.findWinnerNeuron(inputs[city], neurons)
            paths[str(nearestNeuron)] = city

        dist = 0
        previousCity = None
        firstCity = None
        for n in range(len(neurons)):
           if str(n) in paths:
               city = paths[str(n)]
               if previousCity == None:
                   firstCity = city
                   previousCity = city
               else:
                   dist += distance.euclidean(inputs[city], inputs[previousCity]) * maxVal
                   previousCity = city

        dist += distance.euclidean(inputs[firstCity], inputs[previousCity])

        print('Path dist: {:.2f}km\nOptimal dist: {:.2f}km\n= {:.2f}%'.format(dist, self.optimalDist, (dist/self.optimalDist)))
        sleep(3)

if __name__ == "__main__":
    g = TSP("8")