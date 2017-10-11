import os
import re



def convertStringToList(string):
    return list(map(lambda x: int(x), string.split(',')))



def converteLabelToBitVector(label, numberOfClasses):
    counter = 0
    bitVector = []
    for i in range(numberOfClasses):
        if(counter < label[0]):
            bitVector.append(1)
        else:
            bitVector.append(0)
        counter += 1
    return bitVector



def converteDatasetTo2d(datapath, numberOfClasses):
    filepath = os.getcwd() + "/data/" + datapath

    cases2d = []
    splitCharacters = ",|;"
    with open(filepath) as FileObj:
        for caseline in FileObj:
            caseline = caseline.rstrip() # remove newline character

            c = re.split(splitCharacters, caseline) # make a list out of line
            print(c)
            c = list(map(lambda x: float(x), c)) # make elements float

            l = c[-1:] # get label
            l = converteLabelToBitVector(l, numberOfClasses)
            print(l)
            c = c[:-1] # remove label
            case = [c,l]

            # print("C: ", c)
            # print("L: ", l)
            # print("Case: ", case)

            cases2d.append(case)

    return cases2d[:]


def getCostFunction(name=""):
    # lager learings operator.
    if name == "MSE": # mean squared error
        return "tf.reduce_mean(tf.square(self.target - self.output),name='MSE')"
    elif name == "SCE":  # sigmoid_cross_entropy
        return "tf.losses.sigmoid_cross_entropy(self.target, self.output)"
    elif name == "AD": # compute absolute distance
        return "tf.losses.absolute_difference(self.target, self.output)"
    return name






