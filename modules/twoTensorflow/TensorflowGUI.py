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
        # " "*20 is to make the width of dropdown, nice. If not 20 characters it looks so tiny.
        self.dataset = self.createDropDown("Dataset", " "*20, "glass", "winequality_red", "yeast", "one-hot-vector", "hackers-choice", row=3, column=0)
        self.haf= self.createDropDown("Hidden Activation Func", "sigmoid", "sigmoid", "softmax", "relu", "relu6", row=3, column=1)
        self.oaf = self.createDropDown("Output Activation Func", "sigmoid", "sigmoid", "softmax", "relu", "relu6", row=3, column=2)
        self.costfunc= self.createDropDown("Cost function", "MSE", "MSE", "SCE", "AD", row=3, column=3)
        self.weightrange= self.createEntry("Weight Range", 3,4)
        self.epochs= self.createEntry("Epochs", 3,5)
        self.softmax = self.createDropDown("Softmax", "False", "True", "False", row=3, column=6)

        Label(text="").grid(row=5, column=0)
        self.rungrabvars= self.createEntry("Run Grabvars", 6,0)
        self.proberabvars= self.createEntry("Probe Grabvars", 6,1)


        Label(text="").grid(row=8, column=0)
        self.mapThatShit = self.createDropDown("Mapping?", "False", "True", "False", row=9, column=0)
        self.mapbatchsize= self.createEntry("MapBatch Sixze", 9,1)
        self.mapgrabvars= self.createEntry("Map Grabvars", 9,2)
        self.mapplot= self.createEntry("Map Plot", 9,3)




    def createEntry(self, name, row, column):
        temp = StringVar()
        Label(text=name).grid(row=row, column=column)
        Entry(textvariable=temp, width=self.entryWidth).grid(padx=10, row=row+1, column=column)
        return temp

    def createDropDown(self,name, defaultValue, *options, row, column):
        temp = StringVar(self.gui)
        temp.set(defaultValue)  # default value

        Label(text=name).grid(row=row, column=column)
        OptionMenu(self.gui, temp, *options).grid(padx=10, row=row+1, column=column)

        return temp


    def show(self):
        self.gui.mainloop()

if __name__ == "__main__":
    g = TensorflowGUI()
    g.show()
