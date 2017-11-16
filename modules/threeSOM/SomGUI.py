from tkinter import *
import numpy as np
import ast
from ClassifierClass import Classifier
from TSP import TSP


class SomGUI:
    def __init__(self):
        self.cases = self.loadData()
        self.classifier = None
        self.tsp = None

        self.gui = Tk()
        self.gui.minsize(width=1000, height=550)
        self.entryWidth = 15

        # self.frame1 = Frame(self.gui)
        # self.frame1.grid(row=0, column=1)
        # self.canvas = Canvas(self.frame1, width=100, height=900)
        self.canvas = Canvas(width=1000, height=900)
        self.canvas.grid(row=0, column=1, padx=20)

        self.infoText = Label(text='Epoc:    LR:     NBSize:  ')
        self.infoText.grid(row=1, column=1)
        self.infoText2 = Label(text='')
        self.infoText2.grid(row=2, column=1)

        self.frame2 = Frame(self.gui)
        self.frame2.grid(row=0, column=0)

        Label(self.frame2, text="# Training Cases").grid(row=1, column=0, sticky=E)
        self.trainingVar = StringVar()
        self.training = Entry(self.frame2, textvariable=self.trainingVar, width=self.entryWidth)
        self.training.grid(row=1, column=1, padx=20)

        Label(self.frame2, text="# Testing Cases").grid(row=2, column=0, sticky=E)
        self.testingVar = StringVar()
        self.testing = Entry(self.frame2, textvariable=self.testingVar, width=self.entryWidth)
        self.testing.grid(row=2, column=1)

        Label(self.frame2, text="# Neurons").grid(row=3, column=0, sticky=E)
        self.neuronsVar = StringVar()
        self.neurons = Entry(self.frame2, textvariable=self.neuronsVar, width=self.entryWidth)
        self.neurons.grid(row=3, column=1)

        Label(self.frame2, text="# Epochs").grid(row=4, column=0, sticky=E)
        self.epochsVar = StringVar()
        self.epochs = Entry(self.frame2, textvariable=self.epochsVar, width=self.entryWidth)
        self.epochs.grid(row=4, column=1)

        Label(self.frame2, text="View Int").grid(row=5, column=0, sticky=E)
        self.vintVar = StringVar()
        self.vint = Entry(self.frame2, textvariable=self.vintVar, width=self.entryWidth)
        self.vint.grid(row=5, column=1)

        Label(self.frame2, text="Classification Int").grid(row=6, column=0, sticky=E)
        self.cintVar= StringVar()
        self.cint = Entry(self.frame2, textvariable=self.cintVar, width=self.entryWidth)
        self.cint.grid(row=6, column=1)

        Label(self.frame2, text="InitNeighborhoodSize").grid(row=7, column=0, sticky=E)
        self.insVar= StringVar()
        self.ins = Entry(self.frame2, textvariable=self.insVar, width=self.entryWidth)
        self.ins.grid(row=7, column=1)

        Label(self.frame2, text="NeighborhoodConstant").grid(row=8, column=0, sticky=E)
        self.ncVar= StringVar()
        self.nc= Entry(self.frame2, textvariable=self.ncVar, width=self.entryWidth)
        self.nc.grid(row=8, column=1)

        Label(self.frame2, text="LearningConstant").grid(row=9, column=0, sticky=E)
        self.lcVar= StringVar()
        self.lc = Entry(self.frame2, textvariable=self.lcVar, width=self.entryWidth)
        self.lc.grid(row=9, column=1)

        Button(self.frame2, bg="#469683", highlightbackground="#469683", padx=33, pady=10, text="Run Mnist", command=lambda: self.runModule()).grid(row=10, column=0, columnspan=2, pady=10)
        Button(self.frame2, bg="#469683", highlightbackground="#469683", padx=33, pady=10, text="Plot Values", command=lambda: self.plotValues()).grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.frame2, text=" ").grid(row=11, column=0, sticky=E)

        Label(self.frame2, text="TSP filename").grid(row=12, column=0, sticky=E)
        self.filenameVar = StringVar()
        self.filename = Entry(self.frame2, textvariable=self.filenameVar, width=self.entryWidth)
        self.filename.grid(row=12, column=1)

        Label(self.frame2, text="Lrate").grid(row=13, column=0, sticky=E)
        self.lrateVar = StringVar()
        self.lrate = Entry(self.frame2, textvariable=self.lrateVar, width=self.entryWidth)
        self.lrate.grid(row=13, column=1)

        Label(self.frame2, text="Epochs").grid(row=14, column=0, sticky=E, )
        self.maxepochsVar = StringVar()
        self.maxepochs = Entry(self.frame2, textvariable=self.maxepochsVar, width=self.entryWidth)
        self.maxepochs.grid(row=14, column=1)

        Label(self.frame2, text="*Neurons").grid(row=15, column=0, sticky=E, )
        self.xneuronsVar = StringVar()
        self.xneurons = Entry(self.frame2, textvariable=self.xneuronsVar, width=self.entryWidth)
        self.xneurons.grid(row=15, column=1)

        Label(self.frame2, text="NeighbourhoodSize").grid(row=16, column=0, sticky=E, )
        self.nhsizeVar = StringVar()
        self.nhsize = Entry(self.frame2, textvariable=self.nhsizeVar, width=self.entryWidth)
        self.nhsize.grid(row=16, column=1)


        Button(self.frame2, bg="#469683", highlightbackground="#469683", padx=33, pady=10, text="Run TSP", command=lambda: self.runTSP()).grid(row=17, column=0, columnspan=2, pady=10)

        self.gui.mainloop()

    def runTSP(self):
        self.tsp = TSP(
            filename = self.filenameVar.get(),
            lrate = int(self.lrateVar.get()),
            maxepochs = int(self.maxepochsVar.get()),
            xneurons = int(self.xneuronsVar.get()),
            nhsize = int(self.nhsize.get())
        )

    def runModule(self):
        self.cases = self.loadData()
        self.infoText.config(text='Epoc:    LR:     NBSize:  ')
        self.infoText2.config(text=" ")
        self.classifier = Classifier(
            gui=self,
            cases=self.getTrainingAndTestCases(),
            numNeurons=int(self.neuronsVar.get()),
            maxEpochs=int(self.epochsVar.get()),
            vint=int(self.vintVar.get()),
            cint=int(self.cintVar.get()),
            ins=int(self.insVar.get()),
            nc=int(self.ncVar.get()),
            lc=int(self.lcVar.get()),)
        # self.training.delete(0, END)
        # self.testing.delete(0, END)
        # self.neurons.delete(0, END)
        # self.epochs.delete(0, END)
        # self.vint.delete(0, END)
        # self.cint.delete(0, END)

    def plotValues(self):
        self.training.insert(END, '1000')
        self.testing.insert(END, '100')
        self.neurons.insert(END, '200')
        self.epochs.insert(END, '50')
        self.vint.insert(END, '5')
        self.cint.insert(END, '10')
        self.ins.insert(END, '10')
        self.nc.insert(END, '10')
        self.lc.insert(END, '16')

    def loadData(self):
        ca = []
        with open("som_cases.txt") as FileObj:
            for caseline in FileObj:
                caseline = caseline.rstrip()  # remove newline character
                ca.append(ast.literal_eval(caseline))
        return ca

    def getTrainingAndTestCases(self):
        return [self.cases[: int(self.trainingVar.get())], self.cases[ int(self.trainingVar.get()): int(self.trainingVar.get()) +  int(self.testingVar.get())]]

    def draw(self, neurons):
        can = self.canvas

        # one neuron = one picture, one picture has 784 pixels / rectangles
        offsettRow = 0
        offsettCol = 0
        split = np.floor(np.sqrt(len(neurons)))
        i = 0
        for neuron in np.nditer(neurons, flags=["refs_ok"]):
            neuron = neuron.item()
            if i == split:
                offsettRow += 57
                offsettCol = 0
                i = 0
            elif i != 0:
                offsettCol += 57
            self.drawOneNeuron(can, neuron.weights, offsettRow, offsettCol)

            # can.update_idletasks()
            # can.update()

            i += 1
        can.update_idletasks()
        can.update()

    def drawOneNeuron(self, can, neuron, row, col):
        idx = 0
        row = row
        column = col
        pixelsize = 2
        for p in np.nditer(neuron):
            p = int(p * 255)
            colorval = '#%02x%02x%02x' % (p, p, p)
            if idx == 28:
                row += pixelsize
                column = col
                idx = 0
            can.create_rectangle(column, row, column + pixelsize, row + pixelsize, fill=colorval)
            idx += 1
            column += pixelsize

if __name__ == "__main__":
    g = SomGUI()

