from tutorialThree import Gann, autoex, Caseman
import helpers
import tflowtools as TFT

def runModule(dataset="mnist", epochs=100 ,lrate=0.175,showint=15,mbs=87,vfrac=0.1,tfrac=0.1,vint=80,sm=False):
    # size = 2**nbits I autoex, så gir denne 16, som er så mange elementer i hver liste / features

    numberOfFeatures = 784 # g = 9, w = 11, y = 8, autoencoder = 2**nbits == 2**4 == 16
    numberOfClasses = 10 # g = 7, w = 6, y = 10, autoencoder = 2**nbits == 2**4 == 16
    # wantedRunGrabvars = [[0, 'in'], [1, 'wgt'], [0, 'out'], [-1, 'out']]
    # wantedProbeGrabvars = [[0, 'wgt', ('hist', 'avg')], [1, 'wgt', ('hist', 'avg')]]

    mbs = mbs if mbs else 10
    # case_generator = (lambda : helpers.converteDatasetTo2d("winequality_red.txt", numberOfClasses))
    # case_generator = (lambda: helpers.converteDatasetTo2d("glass.txt", numberOfClasses))
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

    case_generator = eval(helpers.get_case_generator(dataset))

    cman = Caseman(cfunc=case_generator,vfrac=vfrac,tfrac=tfrac, cfrac=0.1)

    # dims = [features, hidden layer,...,hidden layer n-1, hidden layer n, labels]
    dims = [numberOfFeatures, 8, numberOfClasses]

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
        bounds=[-1, 1],
        lossFunction="MSE",
        mapBatchSize = 5,
        wantedMapGrabvars = [[0,'out'], [1,'out']],
        dendrogramLayers = [[2,'out']],
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