import matplotlib.pyplot as plt
import math
import numpy as np

def sigmoid(a):
    # e = math.exp() # e ≈ 2.7
    e = 2.7
    return (1 / (1 + e**(-a)))



def showGraph():
    sigmoidValues = []
    for i in range(-10,10):
        sigmoidValues.append(sigmoid(i))

    print("Sigmoid values [-10,10]: " + str(sigmoidValues))

    xAxis = np.arange(-10, 10) # make a list from (-10 to 10) with a step of one
    yAxis = sigmoidValues


    plt.ylabel("hmm...")
    plt.xlabel("what are these numbers?")

    plt.plot(xAxis, yAxis)
    plt.show()



showGraph()

