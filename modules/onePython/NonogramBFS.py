from BFSclass import BFS
from NonogramNode import NonogramNode

class NonogramBFS(BFS):
    def __init__(self):
        self.numColumns = 0
        self.numRows = 0
        self.rows = []
        self.columns = []
        pass

    def getInitalState(self, fileWithInitState):
        try:
            initialState = open(fileWithInitState, 'r')
            lineNumber = 0
            rows = []
            columns = []
            for line in initialState:
                line = list(map(int, line.split(" "))) #map returns an iterable whitch is converted to a list
                if(lineNumber == 0):
                    self.numColumns = line[0]
                    self.numRows = line[1]
                elif(lineNumber <= self.numRows):
                    rows.append(line)
                    self.rows.append(NonogramNode("row", self.numColumns, line))
                else:
                    columns.append(line)
                    self.columns.append(NonogramNode("column", self.numRows, line))

                lineNumber += 1
            print("Rows: " + str(rows))
            print("Columns:" + str(columns))
        except:
            raise Exception("Something went wrong when making inital state")



    def createBoard(self):
        board = None
        return board

    def drawBoard(self, state):
        self.board = self.createBoard()
        # place the pieces on a fresh board
        # print board.
        pass

    def calculateHValue(self, node, goal):
        pass

    def generateSuccessors(self, node):
        ''' Rember to check if moveing will be outside "board" (use self.boardSize) '''
        pass

    def addKid(self, node, kid):
        node.addKid(kid)

    def arc_cost(self, kid, node):
        pass

    def foundSolution(self, node, goalState):
        pass

    def generateNode(self, variable, dir):
        domain = []
        if(dir == "row"):
            domain = self.create_domain(self.numColumns, variable)
        else:
            domain = self.create_domain(self.numRows, variable)
        print("var = " + str(variable))
        print("dom = " + str(domain))
        print("\n")

    def makefunc(self, var_names, expression, envir=globals()):
        args = ",".join(var_names)
        print("args:" + str(args))
        return eval("(lambda " + args + ":" + expression + ")", envir)


    def orderConstraint(self, domain, segments): # domain = on of the row/columns permutations || segements are the variables involved [3,1] or [3,1,1]
        numberOfSegments = len(segments)

        constraint = ""

        if numberOfSegments <= 1:
            return domain

        for i in range(numberOfSegments):
            # stuff.append(chr(97 + i))
            if i != numberOfSegments - 1 :
                constraint += "domain.rfind(" + "str(" +str(i) + "))" + " < domain.find(" + "str(" + str(i+1) + ")) - 1 and "
            else: # if last variable, you are covered by the other variables. you just need to be after them
                constraint = constraint[:len(constraint)-4]

        # print("con:  " + constraint)
        # print("domain:  " + domain)

        if not eval(constraint):
            return False

        return True

    def reduceDomain(self, a, b):
        for key in a.common.keys():
            valid = True
            for x in b:
                print("Before reduce: " + str(len(x.domain)))
                print(x.domain)
                print(a.common)
                for d in x.domain:
                    # print("Dkey: " + str(d[key]))
                    # print("aCommonKey: " + str(a.common[key]))
                    if d[key] != a.common[key]:
                        valid = False
                        x.domain.remove(d)
                print("After reduce: " + str(len(x.domain)))
                print(x.domain)

def main():
    nono = NonogramBFS()
    nono.getInitalState("tasks/nono-cat.txt")
    for row in nono.rows:
        nono.reduceDomain(row, nono.columns)
        print(row)


    # for col in nono.columns:
    #     print(col)

    # nono.getInitalState("tasks/nono-chick.txt")
    # nono.getAllRowPermutations([5, 1, 3, 2])

    # nono.getInitalState("tasks/nono-cat.txt")
    # nono.getAllRowPermutations([3, 1])

    # nono.getInitalState("tasks/nono-fox.txt")
    # nono.getAllRowPermutations([1, 2, 1, 1, 1, 1, 1, 1, 2, 3])




    # nono.moveCurrentString()
    # print(nono.getAllRowPermutations([2, 2]))
    # print(nono.getAllColumnPermutations([2, 2]))
    # print(nono.orderConstraint('0-11-2-3-4-5-6-7-999--88', [1, 2, 1, 1, 1, 1, 1, 1, 2, 3]))
    # print(nono.orderConstraint('0-111', [1, 3]))
    # print(nono.drawString([3,1], 4))

main()
