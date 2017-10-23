from distutils.util import strtobool
from tkinter import *
from tutorialThree import Gann, Caseman
import helpers
import tflowtools as TFT

class TensorflowGUI:
    def __init__(self):
        self.gui = Tk()
        self.ann = None
        self.probeList = []
        self.grabvarList = []
        self.mapgrabvarList = []
        self.dendrogrammapgrabvarList = []

        self.entryWidth = 15

        self.gui.minsize(width=1000, height=550)

        self.dataset = self.createDropDown("Dataset", "autoencoder", "glass", "wine", "yeast", "one-hot-vector", "breast_cancer", "autoencoder", "parity", "dense", "bit", "segment", "mnist", row=0, column=0)
        self.nbits = self.createEntry("nBits", row=0, column=1)
        self.size = self.createEntry("Size", row=0, column=2)
        self.density= self.createEntry("Density", row=0, column=3) # TODO: Should be touple

        Label(text="").grid(row=2, column=0)
        self.minseg = self.createEntry("MinSeg", row=3, column=0)
        self.maxseg = self.createEntry("MaxSeg", row=3, column=1)
        self.poptarg = self.createDropDown("PopTarg", "True", "True", "False", row=3, column=2)
        self.double = self.createDropDown("Double", "True", "True", "False", row=3, column=3)
        self.random = self.createDropDown("Random", "True", "True", "False", row=3, column=4)

        Label(text="").grid(row=5, column=0)
        self.dims = self.createEntry("Dims", 6, 0)
        self.epochs = self.createEntry("Epochs", 6, 1)
        self.lrate = self.createEntry("Learning Rate", 6, 2)
        self.mbs = self.createEntry("Minibatch Size", 6, 3)
        self.weightrange = self.createEntry("Weight Range", 6, 4)

        Label(text="").grid(row=8, column=0)
        self.cfrac = self.createEntry("Case Fraction", 9, 0)
        self.vfrac = self.createEntry("Validation Fraction", 9, 1)
        self.tfrac = self.createEntry("Test Fraction", 9, 2)
        self.vint = self.createEntry("Validation interval", 9, 3)
        self.showint = self.createEntry("Show interval", 9, 4)

        Label(text="").grid(row=11, column=0)
        self.haf = self.createDropDown("Hidden Activation Func", "sigmoid", "sigmoid", "tanh", "softmax", "relu",
                                       "relu6", row=12, column=0)
        self.oaf = self.createDropDown("Output Activation Func", "sigmoid", "sigmoid", "tanh", "softmax", "relu",
                                       "relu6", row=12, column=1)
        self.costfunc = self.createDropDown("Cost function", "MSE", "MSE", "SCE", "AD", row=12, column=2)
        self.softmax = self.createDropDown("Softmax", "False", "True", "False", row=12, column=3)
        self.bestk = self.createDropDown("Bestk", "Off", "Off", "On", row=12, column=4)

        Label(text="").grid(row=14, column=0)
        self.rungrabvars = self.createEntry("Run Grabvars", 15, 0)
        Button(bg="#469683", highlightbackground="#469683", padx=5, text="+",
               command=lambda: self.addToGrabvarList(self.rungrabvars.get())).grid(row=16, column=1, sticky=W)
        # self.probegrabvars= self.createEntry("Probe Grabvars", 9,1)
        # Button(bg="#469683", highlightbackground="#469683", padx=10, pady=5, text="+",
        #        command=lambda: self.addToProbeList(self.probegrabvars.get())).grid(row=10, column=2)
        self.showWgtmatrix = self.createDropDown("Weight Matrix?", "False", "True", "False", row=15, column=1)


        Label(text="").grid(row=17, column=0)
        self.mapThatShit = self.createDropDown("Mapping?", "False", "True", "False", row=18, column=0)
        self.mapbatchsize= self.createEntry("MapBatch Size", 18,1)
        self.mapplot= self.createEntry("Map Plot", 18,2)
        self.mapgrabvars= self.createEntry("Map Grabvars", 18,3)
        Button(bg="#469683", highlightbackground="#469683", padx=5, text="+",
               command=lambda: self.addToMapGrabvarList(self.mapgrabvars.get())).grid(row=20, column=3)
        self.dendrogrammapgrabvars = self.createEntry("DendrogramMap Grabvars", 18, 4)
        Button(bg="#469683", highlightbackground="#469683", padx=5, text="+",
               command=lambda: self.addToDendroGrabvarList(self.dendrogrammapgrabvars.get())).grid(row=20, column=4)


        Label(text="       ").grid(row=0, column=5)
        Button(bg="#469683", highlightbackground="#469683", padx=33, pady=5, text="Run",
               command=lambda: self.runModule(
                   dataset=self.dataset.get(),
                   dims=helpers.convertStringToIntList(self.dims.get()),
                   epochs=self.castToInt(self.epochs.get()),
                   lrate=self.castToFloat(self.lrate.get().replace(",", ".")),
                   mbs=int(self.mbs.get()),
                   cfrac=self.castToFloat(self.cfrac.get().replace(",", ".")),
                   vfrac=self.castToFloat(self.vfrac.get().replace(",", ".")),
                   tfrac=self.castToFloat(self.tfrac.get().replace(",", ".")),
                   vint=int(self.vint.get()),
                   showint=self.castToInt(self.showint.get()),
                   haf=self.haf.get(),
                   oaf=self.oaf.get(),
                   costfunc=self.costfunc.get(),
                   sm=self.stringToBool(self.softmax.get()),
                   bounds=helpers.convertStringToFloatList(self.weightrange.get()),
                   mapThatShit=self.stringToBool(self.mapThatShit.get()),
                   mapBatchSize= self.castToInt(self.mapbatchsize.get()),
                   bestk=self.getCorrectBestKValue(self.bestk.get())
               )).grid(row=13, column=6)

        Button(bg="#469683", highlightbackground="#469683", padx=33, pady=5, text="Run more",
               command=lambda: self.runModuleMore(self.castToInt(self.epochs.get()))).grid(row=13, column=7)

        self.datasetText = Label(text="", padx=10, font=("Courier", 20))
        self.datasetText.grid(row=4, column=6, columnspan=2)

        self.correctText = Label(text="Correct", padx=10, font=("Courier", 20))
        self.correctText.grid(row=7, column=6)
        self.correctInfoText = Label(text="", padx=10, font=("Courier", 20))
        self.correctInfoText.grid(row=8, column=6)

        self.errorText = Label(text="Error", padx=10, font=("Courier", 20))
        self.errorText.grid(row=7, column=7)
        self.errorInfoText = Label(text="", padx=10, font=("Courier", 20))
        self.errorInfoText.grid(row=8, column=7)


    def stringToBool(self, strng):
        if strng:
            return bool(strtobool(strng))
        return None

    def castToInt(self, value):
        if value:
            return int(value)
        return None

    def castToFloat(self, value):
        if value:
            return float(value)
        return None

    def convertStringToIntTuple(self,string):
        if string:
            return eval("("+string+")")
        return None


    def getCorrectBestKValue(self, bestk):
        if bestk == "Off": return None
        if bestk == "On": return 1
        return None

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

    def addToMapGrabvarList(self, listString):
        x = listString.split(",")
        module = int(x[0])
        type = str(x[1])
        listString = [module, type]
        self.mapgrabvarList.append(listString)

    def addToDendroGrabvarList(self, listString):
        x = listString.split(",")
        module = int(x[0])
        type = str(x[1])
        listString = [module, type]
        self.dendrogrammapgrabvarList.append(listString)


    def runModule(self, dataset="autoencoder", dims=None, epochs=500, lrate=None, mbs=None, cfrac=None, vfrac=None, tfrac=None, vint=None, showint=None,
                  haf=None, oaf=None, costfunc=None, sm=False, bounds=None, mapThatShit=None, mapBatchSize=0, bestk=None):

        set = dataset.upper()
        self.datasetText.configure(text=str(set))
        self.correctInfoText.configure(text="running..")
        self.errorInfoText.configure(text="running..")
        self.gui.update()
        # size = 2**nbits I autoex, så gir denne 16, som er så mange elementer i hver liste / features
        # numberOfFeatures = 8 # g = 9, w = 11, y = 8, autoencoder = 2**nbits (2**4 = 16)
        # numberOfClasses = 10  # g = 7, w = 6, y = 10, autoencoder = 2**nbits (2**4 = 16)
        # wantedRunGrabvars = [[0, 'in'], [1, 'wgt'], [0, 'out'], [-1, 'out']]
        # wantedProbeGrabvars = [[0, 'wgt', ('hist', 'avg')], [1, 'wgt', ('hist', 'avg')]]

        mbs = mbs if mbs else 10

        case_generator = eval(helpers.get_case_generator(
            data_name=dataset,
            # TODO IMPLEMENT :: numberOfCases=self.castToInt(self.numberOfCases),
            nbits=self.castToInt(self.nbits.get()),
            size=self.castToInt(self.size.get()),
            density=self.convertStringToIntTuple(self.density.get()),
            double=self.stringToBool(self.double.get()),
            random=self.stringToBool(self.random.get()),
            minsegs=self.castToInt(self.minseg.get()),
            maxsegs=self.castToInt(self.maxseg.get()),
        ))



        cman = Caseman(cfunc=case_generator, vfrac=vfrac, tfrac=tfrac, cfrac=cfrac)


        self.ann = Gann(
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
            mapBatchSize=mapBatchSize,
            wantedMapGrabvars=self.mapgrabvarList,
            dendrogramLayers=self.dendrogrammapgrabvarList,
            mapplot=self.mapplot.get(),
            wgtMatrix=self.stringToBool(self.showWgtmatrix.get())
        )

        # self.ann.add_grabvar(0,'in') # Add a grabvar (to be displayed in its own matplotlib window). # grab second hidden layer ?
        # self.ann.add_grabvar(-1,'wgt') # Add a grabvar (to be displayed in its own matplotlib window). # grab second hidden layer ?
        # self.ann.add_grabvar(-1,'bias') # Add a grabvar (to be displayed in its own matplotlib window). # grab second hidden layer ?


        # helpers.add_prob_grabvars(ann,self.probeList)  # add PROB_vars
        helpers.add_grabvars(self.ann, self.grabvarList)  # add GRAB_vars

        self.ann.run(epochs, mapThatShit=mapThatShit, bestk=bestk) # bestk = nonetype or 1 int
        self.ann.runmore(epochs * 2, bestk=bestk)

        errorres = self.ann.testres
        correctres = (1 - self.ann.testres) * 100
        self.correctInfoText.configure(text="%.3f" % (correctres) + "%")
        self.errorInfoText.configure(text="%.4f" % (errorres) + "%")

        if(self.mapThatShit.get()):
            self.ann.do_mapping(msg="Mapping", bestk=self.getCorrectBestKValue(self.bestk.get()))

        # clear the lists that hold vars to be grabed, so that the next run does not include the same grabvars, without beeing explicitly stated
        self.grabvarList.clear()
        self.mapgrabvarList.clear()
        self.dendrogrammapgrabvarList.clear()

        return self.ann


    def runModuleMore(self, epochs):
        self.ann.runmore(epochs * 2)

    def show(self):
        self.gui.mainloop()





if __name__ == "__main__":
    g = TensorflowGUI()
    g.show()
