from tkinter import *


class TensorflowGUI:
    def __init__(self):
        self.gui = Tk()

        self.entryWidth = 15

        self.gui.minsize(width=1000, height=400)

        self.dims = self.createEntry("Dims", 0,0)
        self.lrate = self.createEntry("Learning Rate", 0,1)
        self.mbs = self.createEntry("Minibatch Size", 0,2)
        self.showint = self.createEntry("Show interval", 0,3)
        self.cfrac = self.createEntry("Case Fraction", 0,4)
        self.vfrac = self.createEntry("Validation Fraction", 0,5)
        self.tfrac = self.createEntry("Test Fraction", 0,6)
        self.vint = self.createEntry("Validation interval", 0,7)

        Label(text="").grid(row=2, column=0)

        self.dataset = self.createEntry("Dataset", 3,0)
        self.haf= self.createEntry("Hidden Activation Func", 3,1)
        self.oaf= self.createEntry("Output Activation Func", 3,2)
        self.costfunc= self.createEntry("Cost Function", 3,3)
        self.weightrange= self.createEntry("Weight Range", 3,4)
        self.epochs= self.createEntry("Epochs", 3,5)


    def createEntry(self, name, row, column):
        temp = StringVar()
        Label(text=name).grid(row=row, column=column)
        Entry(textvariable=temp, width=self.entryWidth).grid(padx=10, row=row+1, column=column)
        return temp

    def show(self):
        self.gui.mainloop()

if __name__ == "__main__":
    g = TensorflowGUI()
    g.show()