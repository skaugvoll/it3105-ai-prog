import os
def converteDatasetTo2d(datapath):
    filepath = os.getcwd() + "/data/" + datapath

    cases2d = []
    with open(filepath) as FileObj:
        for caseline in FileObj:
            caseline = caseline.rstrip() # remove newline character

            c = caseline.split(";") # make a list out of line
            c = list(map(lambda x: float(x), c)) # make elements float

            l = c[-1:] # get label
            c = c[:-1] # remove label
            case = [c,l]

            # print("C: ", c)
            # print("L: ", l)
            # print("Case: ", case)

            cases2d.append(case)

    return cases2d

