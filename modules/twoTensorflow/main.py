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


def runModule(epochs=30,lrate=.8,showint=30,mbs=None,vfrac=0.1,tfrac=0.1,vint=10,sm=True):
    # size = 2**nbits I autoex, så gir denne 16, som er så mange elementer i hver liste / features

    numberOfClasses = 6

    mbs = mbs if mbs else 50

    case_generator = (lambda : helpers.converteDatasetTo2d("winequality_red.txt", numberOfClasses))


    cman = Caseman(cfunc=case_generator,vfrac=vfrac,tfrac=tfrac, cfrac=1)

    # dims = [features, hidden layer,...,hidden layer n-1, hidden layer n, labels]
    dims = [11, 1, 2, numberOfClasses]

    ann = Gann(
        dims=dims,
        cman=cman,
        lrate=lrate,
        showint=showint,
        mbs=mbs,
        vint=vint,
        softmax=sm,
        hiddenLayerActivationFunction="softmax",
        outputActivationFunction="softmax",
        bounds=[-1, 1],
        lossFunction="MSE",
        mapBatchSize = 10,
        wantedMapGrabvars = [[1,'wgt'], [-1,'out']]
    )

    ann.gen_probe(0,'wgt',('hist','avg'))  # Plot a histogram and avg of the incoming weights to module 0. : first hidden layer ?
    ann.gen_probe(1,'wgt',('hist','avg'))  # Plot average and max value of module 1's output vector : second hidden layer

    # ann.add_grabvar(1,'wgt') # Add a grabvar (to be displayed in its own matplotlib window). # grab second hidden layer ?
    # ann.add_grabvar(-1, 'out')  # Add a grabvar (to be displayed in its own matplotlib window). # get the last module / layer in the network. this is the output layer

    ann.run(epochs, mapThatShit=True)
    ann.runmore(epochs*2)



    return ann

runModule()