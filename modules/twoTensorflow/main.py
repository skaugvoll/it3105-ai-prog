import os
from tutorialThree import Gann, autoex, Caseman
from helpers import converteDatasetTo2d

def runModule():
    dims = None #Layer-sizes
    caseMan = None
    lrate = None #Learning rate
    showint  = None # show interval
    mbs = None # mini batch size
    vint = None # validation history
    softmax = None # softmax_0utputs # this is a regression / learning algorthm thingy thang

def test():
    # dataset = "winequality_red.txt"
    # datapath = os.getcwd()+"/data/"+dataset
    # data = converteDatasetTo2d(datapath)
    # print(data)

    autoex()

test()