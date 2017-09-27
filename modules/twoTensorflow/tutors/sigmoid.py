import matplotlib.pyplot as plt
import math
import numpy as np

def sigmoid(a):
    '''
    Basically a threshold function, but since it's not on/off [0,1], we call it an activation function (since we want values between 0 and 1) that gives us <0,1>.
    When the input a --> -inf, sigmoid --> 0
    When the input a --> inf, sigmoid --> 1

    e is an mathematical constant approximately 2.7

    :param a: input value to transform / map to sigmoid
    :return: sigmoid-ified value
    '''

    e = 2.7 # e = math.exp() # e ≈ 2.7
    return (1 / (1 + e**(-a)))


def derivitedSigmoid(a):
    derivitedSigmoidNumber = None
    sigA = sigmoid(a)

    # the derivited sigmoid can be written as: derivited sigmoid = (sigmoid(a) * (1 - sigmoid(a))
    derivitedSigmoidNumber = sigA * (1 - sigA)
    return derivitedSigmoidNumber



def showSigmoidGraph():
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


def showDerivitedSigmoidGraph():
    derivitedSigmoidValues = []
    for i in range(-10,10):
        derivitedSigmoidValues.append(derivitedSigmoid(i))

    print("Derivited Sigmoid values [-10,10]: " + str(derivitedSigmoidValues))

    xAxis = np.arange(-10, 10) # make a list from (-10 to 10) with a step of one
    yAxis = derivitedSigmoidValues


    plt.ylabel("hmm...")
    plt.xlabel("what are these numbers?")

    plt.plot(xAxis, yAxis)
    plt.show()



showSigmoidGraph()
showDerivitedSigmoidGraph()

