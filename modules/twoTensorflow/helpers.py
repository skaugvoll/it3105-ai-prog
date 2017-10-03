import os

def converteDatasetTo2d(datapath):
    filepath = os.getcwd() + "/data/" + datapath

    cases2d = []
    with open(filepath) as FileObj:
        for caseline in FileObj:
            caseline = caseline.rstrip()

            c = caseline.split(";")
            c = list(map(lambda x: float(x), c))

            l = c[-1:]

            case = [c,l]
            cases2d.append(case)

    return cases2d

