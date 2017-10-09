from tutorialThree import Gann, autoex, Caseman
import helpers


def runModule():
    dims = None #Layer-sizes [features, hl1,....hln, outputs]
    caseMan = None
    lrate = None #Learning rate
    showint  = None # show interval
    mbs = None # mini batch size
    vint = None # validation history
    softmax = None # softmax_0utputs # this is a regression / learning algorthm thingy thang


def test():
    # dataset = "winequality_red.txt"
    # data = converteDatasetTo2d(dataset)
    # print(data)

    autoex()

# test()


def gannTesting(epochs=50,nbits=4,lrate=0.03,showint=100,mbs=None,vfrac=0.1,tfrac=0.1,vint=100,sm=False):
    # size = 2**nbits I autoex, så gir denne 16, som er så mange elementer i hver liste / features


    mbs = mbs if mbs else 11

    case_generator = (lambda : helpers.converteDatasetTo2d("winequality_red.txt"))


    cman = Caseman(cfunc=case_generator,vfrac=vfrac,tfrac=tfrac)

    # dims = [features, hidden layer,...,hidden layer n-1, hiden layer n, labels]
    dims = [11, nbits,4,4, 1]

    ann = Gann(dims=dims,cman=cman,lrate=lrate,showint=showint,mbs=mbs,vint=vint,softmax=sm)

    ann.gen_probe(0,'wgt',('hist','avg'))  # Plot a histogram and avg of the incoming weights to module 0.
    ann.gen_probe(-1,'out',('avg','max'))  # Plot average and max value of module 1's output vector

    ann.add_grabvar(0,'wgt') # Add a grabvar (to be displayed in its own matplotlib window).

    ann.run(epochs)
    ann.runmore(epochs*2)


    return ann

# gannTesting()