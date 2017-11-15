from tkinter import *
import os
import numpy as np
import math
import time
from Neuron import Neuron

cwd = os.getcwd()
sys.path.append(cwd + "/mnist/")

import mnist_basics as MNIST

class Classifier:

    def __init__(self, gui, cases, numNeurons, maxEpochs, vint, cint, ins, nc, lc):
        self.gui = gui
        self.cases = cases
        self.numNeurons = numNeurons
        self.maxEpochs = maxEpochs
        self.vint = vint
        self.cint = cint
        self.ins = ins
        self.nc = nc
        self.lc = lc
        self.run()


    def converteFlatMnistTo2D(self):
        cases2D = []
        cases = MNIST.load_all_flat_cases()  # returns [ [cases] , [targets] ] --> cases = [ [features...] ]

        for f, t in zip(cases[0], cases[1]):
            f = [feature / 255 for feature in f]
            case = [f, t]
            cases2D.append(case)
        return cases2D

    def writeCasesToFile(self):
        ca = self.converteFlatMnistTo2D(self)
        np.random.shuffle(ca)
        ca = ca[:3000]

        with open("som_cases.txt", 'w') as file_handler:
            for case in ca[:-1]:
                file_handler.write("{}\n".format(case))
            file_handler.write("{}".format(ca[-1]))


    def generateNeurons(self, numberOfNeurons, numberOfPixels=784, numberOfClasses=10):
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

    def findWinnerNeuron(self,case, neurons):
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

    def run(self):
        # infoText = Label(text='Epoc:     Step:    LR:    NBSize:  ')
        # infoText.grid(row=1, column=0)

        data = self.cases
        testData = data[1]
        data = data[0]

        numberOfPixels = 784
        numberOfClasses = 10
        neurons = np.array(self.generateNeurons(numberOfNeurons=self.numNeurons, numberOfPixels=numberOfPixels,
                                           numberOfClasses=numberOfClasses))  # randomly initialize 100 neruons with 784 pixlers each.
        self.gui.draw(neurons)

        converged = False
        ###  TRAINING EPOCS
        s1 = time.time()

        # while epoc < maxEpoc and not converged:
        for epoc in range(1, self.maxEpochs + 1):
            learningRate = np.exp(-epoc / self.lc)
            if epoc == 1:
                neighborhoodSize = self.ins
            else:
                neighborhoodSize = self.ins * np.exp(-epoc / self.nc)  # 10 = constant

            ### STEPS
            for case in data:
                winnerNeuron = self.findWinnerNeuron(case[0], neurons)

                if epoc % self.cint == 0:
                    label = case[1]
                    winnerNeuron.winnerlabels[label] += 1

                ## UPDATE ALL NEURONS ? or update Winner and some Neighbours
                tempNeighborhoodSize = np.ceil(neighborhoodSize)
                for neuron in np.nditer(neurons, flags=["refs_ok"]):
                    neuron = neuron.item()
                    dist = np.abs(neuron.x - winnerNeuron.x) + np.abs(neuron.y - winnerNeuron.y)

                    if (dist <= tempNeighborhoodSize):
                        neighborhoodMembership = np.exp(-dist ** 2 / neighborhoodSize ** 2)
                        neuron.weights = np.add(neuron.weights, np.prod(
                            [np.array([learningRate]), np.array([neighborhoodMembership]),
                             np.subtract(case[0], neuron.weights)]))

                        # infoText.config(text='Epoc: {:d}   Step: {:d}  LR: {:.2f}  NBSize: {:.2f}'.format(epoc, case, learningRate, neighborhoodSize))
                    # infoText.update()

            if epoc % self.cint == 0:
                for neuron in np.nditer(neurons, flags=["refs_ok"]):
                    neuron = neuron.item()
                    neuron.currentLabel = np.where(neuron.winnerlabels == neuron.winnerlabels.max())[0][0]
                    neuron.winnerlabels = np.zeros((1, numberOfClasses))[0]

            if epoc % self.vint == 0:
                self.gui.draw(neurons)

        ### TODO: Look for convergens : if we under training had 60 % correct, and now we still have 60%, then convergence... ?? --> da må vi sjekke hvor mange vi har rette

        s2 = time.time()
        s3 = time.time()

        ### TODO: CLASSIFY IMAGES / TESTING --> Turn of learning, see if the winenr neuron is the same "class" as the image / input target

        correct = 0
        for case in range(int(self.gui.testingVar.get())):
            winnerNeuron = self.findWinnerNeuron(testData[case][0], neurons)
            correctLabel = testData[case][1]
            predictedLabel = winnerNeuron.currentLabel
            if correctLabel == predictedLabel: correct += 1

        s4 = time.time()
        print('Number of test cases: {:d}\nNumber of correct classifications: {:d}\n= {:.5f}% correct '.format(
            int(self.gui.testingVar.get()), correct, correct / int(self.gui.testingVar.get())))
        s5 = time.time()
        correct = 0
        for case in range(int(self.gui.testingVar.get())):
            winnerNeuron = self.findWinnerNeuron(data[case][0], neurons)
            correctLabel = data[case][1]
            predictedLabel = winnerNeuron.currentLabel
            if correctLabel == predictedLabel: correct += 1

        s6 = time.time()
        print(
            '\nNumber of seen training cases: {:d}\nNumber of correct classifications: {:d}\n= {:.5f}% correct '.format(
                int(self.gui.testingVar.get()), correct, correct / int(self.gui.testingVar.get())))

        print()
        print(s2 - s1, ' seconds -->', (s2 - s1) / 60, 'minutes')
        print(s4 - s3)
        print(s6 - s5)

        dump = False
        if dump:
            with open('weights.txt', 'w') as file:
                file.write(str(self.numNeurons) + " " + str(numberOfPixels) + '\n')
                for neuron in np.nditer(neurons, flags=["refs_ok"]):
                    neuron = neuron.item().weights
                    file.write(str(neuron) + '\n')