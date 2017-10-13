from tutorialThree import Gann, autoex, Caseman
import helpers
import tflowtools as TFT


# def whatIsThis(dims):
#     dims = helpers.converteDimsToList(dims) #Layer-sizes [features, hl1,....hln, NumberOfOutputClasses]
#     caseMan = None
#     lrate = None #Learning rate
#     showint  = None # show interval
#     mbs = None # mini batch size
#     vint = None # validation history
#     softmax = None # softmax_0utputs # this is a regression / learning algorthm thingy thang



def test():
    dataset = "winequality_red.txt"
    data = helpers.converteDatasetTo2d(dataset, 6)
    # print(data)

    # autoex()

# test()


def runModule(epochs=2500 ,lrate=0.175,showint=15,mbs=87,vfrac=0.2,tfrac=0.1,vint=80,sm=False):
    # size = 2**nbits I autoex, så gir denne 16, som er så mange elementer i hver liste / features

    numberOfFeatures = 8 # g = 9, w = 11, y = 8
    numberOfClasses = 10 # g = 7, w = 6, y = 10

    mbs = mbs if mbs else 10

    # case_generator = (lambda : helpers.converteDatasetTo2d("winequality_red.txt", numberOfClasses))
    case_generator = (lambda: helpers.converteDatasetTo2d("yeast.txt", numberOfClasses))
    # case_generator = (lambda: helpers.converteDatasetTo2d("yeast.txt", numberOfClasses))


    cman = Caseman(cfunc=case_generator,vfrac=vfrac,tfrac=tfrac, cfrac=1)

    # dims = [features, hidden layer,...,hidden layer n-1, hidden layer n, labels]
    dims = [numberOfFeatures, 133,  numberOfClasses]

    ann = Gann(
        dims=dims,
        cman=cman,
        lrate=lrate,
        showint=showint,
        mbs=mbs,
        vint=vint,
        softmax=sm,
        hiddenLayerActivationFunction="sigmoid",
        outputActivationFunction="sigmoid",
        bounds=[-0.5, 0.5],
        lossFunction="MSE",
        mapBatchSize = 15,
        wantedMapGrabvars = [[2,'in'], [2,'out']]
    )

    # ann.gen_probe(0,'wgt',('hist','avg'))  # Plot a histogram and avg of the incoming weights to module 0. : first hidden layer ?
    # ann.gen_probe(1,'wgt',('hist','avg'))  # Plot average and max value of module 1's output vector : second hidden layer

    # ann.add_grabvar(0,'in') # Add a grabvar (to be displayed in its own matplotlib window). # grab second hidden layer ?
    # ann.add_grabvar(1, 'wgt')  # Add a grabvar (to be displayed in its own matplotlib window). # grab second hidden layer ?
    # ann.add_grabvar(0, 'out')  # Add a grabvar (to be displayed in its own matplotlib window). # grab second hidden layer ?

    # ann.add_grabvar(-1, 'out')  # Add a grabvar (to be displayed in its own matplotlib window). # get the last module / layer in the network. this is the output layer

    ann.run(epochs, mapThatShit=False)
    ann.runmore(epochs*2)



    return ann

runModule()