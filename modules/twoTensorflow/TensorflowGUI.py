from distutils.util import strtobool
from tkinter import *
from tutorialThree import Gann, Caseman
import helpers
import tflowtools as TFT

class TensorflowGUI:
    def __init__(self):
        self.gui = Tk()
        self.probeList = []
        self.grabvarList = []

        self.entryWidth = 15

        self.gui.minsize(width=1000, height=400)

        self.dataset = self.createDropDown("Dataset", " "*20, "glass", "winequality_red", "yeast", "one-hot-vector", "hackers-choice", row=0, column=0)
        self.dims = self.createEntry("Dims", 0,1)
        self.epochs = self.createEntry("Epochs", 0,2)
        self.lrate = self.createEntry("Learning Rate", 0,3)
        self.mbs = self.createEntry("Minibatch Size", 0,4)


        Label(text="").grid(row=2, column=0)
        self.cfrac = self.createEntry("Case Fraction", 3,0)
        self.vfrac = self.createEntry("Validation Fraction", 3,1)
        self.tfrac = self.createEntry("Test Fraction", 3,2)
        self.vint = self.createEntry("Validation interval", 3,3)
        self.showint = self.createEntry("Show interval", 3,4)


        Label(text="").grid(row=5, column=0)
        # " "*20 is to make the width of dropdown, nice. If not 20 characters it looks so tiny.
        self.haf= self.createDropDown("Hidden Activation Func", "sigmoid", "sigmoid", "tanh", "softmax", "relu", "relu6", row=6, column=0)
        self.oaf= self.createDropDown("Output Activation Func", "sigmoid", "sigmoid", "tanh", "softmax", "relu", "relu6", row=6, column=1)
        self.costfunc= self.createDropDown("Cost function", "MSE", "MSE", "SCE", "AD", row=6, column=2)
        self.softmax = self.createDropDown("Softmax", "False", "True", "False", row=6, column=3)
        self.weightrange= self.createEntry("Weight Range", 6,4)

        Label(text="", padx=33).grid(row=6, column=7)
        Button(bg="#469683", highlightbackground="#469683", padx=33, pady=5, text="Run",
               command=lambda: self.runModule(
                   dims=helpers.convertStringToIntList(self.dims.get()),
                   epochs=int(self.epochs.get()),
                   lrate=float(self.lrate.get().replace(",",".")),
                   mbs=int(self.mbs.get()),
                   cfrac=float(self.cfrac.get().replace(",",".")),
                   vfrac=float(self.vfrac.get().replace(",",".")),
                   tfrac=float(self.tfrac.get().replace(",",".")),
                   vint=int(self.vint.get()),
                   showint=int(self.showint.get()),
                   haf=self.haf.get(),
                   oaf=self.oaf.get(),
                   costfunc=self.costfunc.get(),
                   sm=self.stringToBool(self.softmax.get()),
                   bounds=helpers.convertStringToFloatList(self.weightrange.get()),
                   mapThatShit=self.stringToBool(self.mapThatShit.get()),
               )).grid(row=6, column=8)

        Label(text="").grid(row=8, column=0)
        self.rungrabvars= self.createEntry("Run Grabvars", 9,0)
        Button(bg="#469683", highlightbackground="#469683", padx=10, pady=5, text="+",
               command=lambda: self.addToGrabvarList(self.rungrabvars.get())).grid(row=10, column=1)
        # self.probegrabvars= self.createEntry("Probe Grabvars", 9,1)
        # Button(bg="#469683", highlightbackground="#469683", padx=10, pady=5, text="+",
        #        command=lambda: self.addToProbeList(self.probegrabvars.get())).grid(row=10, column=2)


        Label(text="").grid(row=11, column=0)
        self.mapThatShit = self.createDropDown("Mapping?", "False", "True", "False", row=12, column=0)
        self.mapbatchsize= self.createEntry("MapBatch Sixze", 12,1)
        self.mapgrabvars= self.createEntry("Map Grabvars", 12,2)
        self.mapplot= self.createEntry("Map Plot", 12,3)

    def stringToBool(self, strng):
        return bool(strtobool(strng))

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

    def addToProbeList(self, listString):
        listString = listString.replace(' ', '')
        x = listString.split(",")
        index = int(x[0])
        type = str(x[1].replace(" ", ''))
        tup = (str(x[2].replace("(", '')), str(x[3].replace(")", "")))
        listString = [index, type, tup]
        self.probeList.append(listString)

    def addToGrabvarList(self, listString):
        x = listString.split(",")
        module = int(x[0])
        type = str(x[1])
        listString = [module, type]
        self.grabvarList.append(listString)


    def runModule(self, dims=None, epochs=500, lrate=None, mbs=None, cfrac=None, vfrac=None, tfrac=None, vint=None, showint=None,
                  haf=None, oaf=None, costfunc=None, sm=False, bounds=None, mapThatShit=None):
        # size = 2**nbits I autoex, så gir denne 16, som er så mange elementer i hver liste / features

        numberOfFeatures = 8  # g = 9, w = 11, y = 8
        numberOfClasses = 10  # g = 7, w = 6, y = 10
        wantedRunGrabvars = [[0, 'in'], [1, 'wgt'], [0, 'out'], [-1, 'out']]
        wantedProbeGrabvars = [[0, 'wgt', ('hist', 'avg')], [1, 'wgt', ('hist', 'avg')]]

        mbs = mbs if mbs else 10

        # case_generator = (lambda : helpers.converteDatasetTo2d("winequality_red.txt", numberOfClasses))
        case_generator = (lambda: helpers.converteDatasetTo2d("yeast.txt", numberOfClasses))
        # case_generator = (lambda: helpers.converteDatasetTo2d("yeast.txt", numberOfClasses))
        # case_generator = (lambda: TFT.gen_all_one_hot_cases(2 ** nbits))


        # parity cases
        # case_generator = (lambda: TFT.gen_all_parity_cases())
        # autoencoder
        # gen_all_one hot_cases

        # case_generator = (lambda: TFT.gen_all_one_hot_cases(2 ** nbits))
        # gen_dense_autoencoder_cases

        # Bit counter
        # case_generator = (lambda: TFT.gen_vector_count_cases())

        # Segment counter
        # case_generator = (lambda: TFT.gen_segment_vector_cases())

        # MNIST
        # --> import mnist_basics.py, gives access to several simple functions for generating standard data sets, such ass load_all)flat)cases
        # --> should probably scale all pixel values to numbers in the range [0,1] BEFORE feeding them into the input of your network

        cman = Caseman(cfunc=case_generator, vfrac=vfrac, tfrac=tfrac, cfrac=cfrac)


        ann = Gann(
            # dims = [features, hidden layer,...,hidden layer n-1, hidden layer n, labels]
            cman=cman,
            dims=dims,
            lrate=lrate,
            mbs=mbs,
            vint=vint,
            showint=showint,
            hiddenLayerActivationFunction=haf,
            outputActivationFunction=oaf,
            lossFunction=costfunc,
            softmax=sm,
            bounds=bounds,
            mapBatchSize=15,
            wantedMapGrabvars=[[0, 'in'], [0, 'out']]
        )

        # helpers.add_prob_grabvars(ann,self.probeList)
        # ann.gen_probe(0,'wgt',('hist','avg'))  # Plot a histogram and avg of the incoming weights to module 0. : first hidden layer ?
        # ann.gen_probe(1,'wgt',('hist','avg'))  # Plot average and max value of module 1's output vector : second hidden layer

        helpers.add_grabvars(ann,self.grabvarList)
        # ann.add_grabvar(0,'in') # Add a grabvar (to be displayed in its own matplotlib window). # grab second hidden layer ?
        # ann.add_grabvar(1, 'wgt')  # Add a grabvar (to be displayed in its own matplotlib window). # grab second hidden layer ?
        # ann.add_grabvar(0, 'out')  # Add a grabvar (to be displayed in its own matplotlib window). # grab second hidden layer ?

        # ann.add_grabvar(-1, 'out')  # Add a grabvar (to be displayed in its own matplotlib window). # get the last module / layer in the network. this is the output layer

        ann.run(epochs, mapThatShit=mapThatShit)
        ann.runmore(epochs * 2)

        self.grabvarList.clear()

        return ann



    def show(self):
        self.gui.mainloop()


if __name__ == "__main__":
    g = TensorflowGUI()
    g.show()
