from itertools import permutations
from BFSclass import BFS

class NonogramBFS(BFS):
    def __init__(self):
        self.numColumns = 0
        self.numRows = 0
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
                    self.generateNode(line, "row")
                else:
                    columns.append(line)
                    self.generateNode(line, "column")

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
            domain = self.getAllRowPermutations(variable)
        else:
            domain = self.getAllColumnPermutations(variable)
        # print("var = " + str(variable))
        # print("dom = " + str(domain))
        # print("\n")


    def getAllRowPermutations(self, elementArray):
        elementString = ""
        for i in range(len(elementArray)):
            if(elementArray[i] == self.numColumns):
                elementString = str(i) * self.numColumns
            else:
                elementString += str(i) * elementArray[i]
            if(i == len(elementArray)-1):
                elementString += "-" * (self.numColumns - len(elementString))
        # all permutations # contains duplicates... (1,2) and (2,1) == duplicates.
        perms = list(set([''.join(p) for p in permutations(elementString)]))
        legalRowPerms = []
        for l in range(len(perms)):
            for k in range(len(elementArray)):
                legal = True
                if(str(perms[l]).find(str(k) * int(elementArray[k])) == -1):
                    legal = False
                    break
            if(legal):
                legalRowPerms.append(perms[l])
        return legalRowPerms

    def getAllColumnPermutations(self, elementArray):
        elementString = ""
        for i in range(len(elementArray)):
            if (elementArray[i] == self.numRows):
                elementString = str(i) * self.numRows
            else:
                elementString += str(i) * elementArray[i]
            if (i == len(elementArray)-1):
                elementString += "-" * (self.numRows - len(elementString))
        # all permutations # contains duplicates... (1,2) and (2,1) == duplicates.
        perms = list(set([''.join(p) for p in permutations(elementString)]))
        legalColumnPerms = []
        for l in range(len(perms)):
            for k in range(len(elementArray)):
                legal = True
                if (str(perms[l]).find(str(k) * int(elementArray[k])) == -1):
                    legal = False
                    break
            if (legal):
                legalColumnPerms.append(perms[l])
        return legalColumnPerms


def main():
    nono = NonogramBFS()
    nono.getInitalState("tasks/nono-cat.txt")
    # nono.getAllRowPermutations([3, 1])
    # print(nono.getAllRowPermutations([2, 2]))
    # print(nono.getAllColumnPermutations([2, 2]))

main()