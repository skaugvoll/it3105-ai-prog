import os
import re



def convertStringToIntList(string):
    return list(map(lambda x: int(x), string.split(',')))

def convertStringToFloatList(string):
    return list(map(lambda x: float(x), string.split(',')))

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
            # print(c)
            c = list(map(lambda x: float(x), c)) # make elements float

            l = c[-1:] # get label
            l = converteLabelToBitVector(l, numberOfClasses)
            # print(l)
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


def add_grabvars(ann, newGrabvars):
    for grabvar in newGrabvars:
        ann.add_grabvar(grabvar[0], grabvar[1])


def add_prob_grabvars(ann, newGrabvars):
    '''
    Function to add a list of vars to be probed in a neural network.

    :param ann: the network that holds the grabvars
    :param newGrabvars: 2D list with, each elemetn having module-index, type, tuple(diagram, measure)
    :return: nothing
    '''
    for grabvar in newGrabvars:
        print(grabvar)
        # ann.gen_probe(0, 'wgt', ('hist', 'avg'))
        print(type(grabvar[0]))
        print(type(grabvar[1]))
        print(type(grabvar[2]))
        ann.gen_probe(grabvar[0], grabvar[1], grabvar[2])


def get_case_generator(
        data_name="autoencoder",
        numberOfClasses=None,
        nbits=4,
        size= None,
        density = (0,1),
        double=True,
        random = True,
        poptarg=True,
        minsegs=1,
        maxsegs=10
    ):
    if data_name == 'yeast': return "(lambda: helpers.converteDatasetTo2d('yeast.txt', 10))"
    if data_name == 'glass': return "(lambda: helpers.converteDatasetTo2d('glass.txt', 7))"
    if data_name == 'wine': return "(lambda : helpers.converteDatasetTo2d('winequality_red.txt', 6))"
    if data_name == 'autoencoder': return "(lambda: TFT.gen_all_one_hot_cases(2 ** "+ str(nbits) +"))"
    if data_name == 'parity': return "(lambda: TFT.gen_all_parity_cases("+ str(nbits) +","+ str(double) +"))"
    if data_name == 'dense': return "(lambda: TFT.gen_dense_autoencoder_cases("+ str(nbits) +","+ str(size) +","+ str(density) +"))"
    if data_name == 'bit': return "(lambda: TFT.gen_vector_count_cases("+ str(nbits) +","+ str(size) +","+ str(density) +","+ str(random) +","+ str(poptarg) +"))"
    if data_name == 'segment': return "(lambda: TFT.gen_segmented_vector_cases("+ str(nbits) +","+ str(size) +","+ str(minsegs) +","+ str(maxsegs) +","+ str(poptarg) +"))"
    if data_name == 'mnist': return "(lambda: MNIST.load_all_flat_cases())"
    # if non of above, must have typed in another one or chosen hackers_choice
    return "(lambda: helpers.converteDatasetTo2d("+data_name+", "+ str(numberOfClasses) +"))"


