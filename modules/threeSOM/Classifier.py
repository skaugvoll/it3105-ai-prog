from tkinter import *
import os
import numpy as np

cwd = os.getcwd()
sys.path.append(cwd + "/mnist/")

import mnist_basics as MNIST

def run():
    gui = Tk()



def loadData():
    ca = np.array(MNIST.load_all_flat_cases()[0])
    np.random.shuffle(ca)
    ca = ca[:500]

loadData()