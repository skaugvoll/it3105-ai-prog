from tkinter import *
import numpy as np

class SomGUI:
    def __init__(self):
        self.gui = Tk()
        self.entryWidth = 15

        self.frame1 = Frame(self.gui)
        self.frame1.grid(row=0, column=1)
        canvas = Canvas(self.frame1, background="black", width=900, height=900)
        canvas.pack()

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

        Button(self.frame2, bg="#469683", highlightbackground="#469683", padx=33, pady=10, text="Run Mnist", command=lambda: self.runModule()).grid(row=7, column=0, columnspan=2, pady=10)
        Button(self.frame2, bg="#469683", highlightbackground="#469683", padx=33, pady=10, text="Plot Values", command=lambda: self.plotValues()).grid(row=0, column=0, columnspan=2, pady=10)

        self.gui.mainloop()

    def runModule(self):
        self.training.delete(0, END)
        self.testing.delete(0, END)
        self.neurons.delete(0, END)
        self.epochs.delete(0, END)
        self.vint.delete(0, END)
        self.cint.delete(0, END)

    def plotValues(self):
        self.training.insert(END, '1000')
        self.testing.insert(END, '100')
        self.neurons.insert(END, '200')
        self.epochs.insert(END, '50')
        self.vint.insert(END, '5')
        self.cint.insert(END, '10')


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


if __name__ == "__main__":
    g = SomGUI()

