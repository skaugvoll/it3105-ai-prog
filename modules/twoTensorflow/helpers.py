import os
import re

def converteDatasetTo2d(datapath):
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
            c = c[:-1] # remove label
            case = [c,l]

            # print("C: ", c)
            # print("L: ", l)
            # print("Case: ", case)

            cases2d.append(case)

    return cases2d


converteDatasetTo2d("winequality_red.txt")
