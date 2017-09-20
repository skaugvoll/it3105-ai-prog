from BFSclass import BFS
from NonogramVariable import NonogramVariable
import pip
from copy import deepcopy
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
                    self.rows.append(NonogramVariable("row", self.numColumns, line))
                else:
                    columns.append(line)
                    self.columns.append(NonogramVariable("column", self.numRows, line))

                lineNumber += 1

            return NonogramNode([self.rows, self.columns])
        except:
            raise Exception("Something went wrong when making inital state")



    def createBoard(self):
        board = None
        return board

    def drawBoard(self, state):
        color = True

        try:
            print("trying...")
            import termcolor
            print("imported: termcolor")
        except ImportError as e:
            print("NO IMPORT...")
            # pip.main(['install', termcolor])
            color = False

        nono = state
        print("NONO:")
        print(nono)
        for row in nono[0]:
            for d in row.domain:
                s = ""
                for ch in d:
                    if (color):
                        if (ch == 0):
                            s += termcolor.colored(ch, "blue")
                        else:
                            s += termcolor.colored(ch, "white")
                    else:
                        s += str(ch)
            print(s)
        pass

    def calculateHValue(self, node, goal):
        domainSum = 0
        for row in node.rows:
            domainSum += len(row.domain)-1
        for col in node.columns:
            domainSum += len(col.domain)-1
        return domainSum

    def generateSuccessors(self, node):
        ''' Rember to check if moveing will be outside "board" (use self.boardSize) '''
        orgNode = deepcopy(node)
        kids = []
        for idx in range(len(orgNode.rows)): # gives a variable
            tempNode = deepcopy(orgNode)
            var = tempNode.rows[idx]
            tempVar = deepcopy(var)
            if (len(var.domain) <= 1):
                continue
            for domainIdx in range(len(var.domain)):
                var.setDomain([tempVar.domain[domainIdx]])
                kids.append(NonogramNode(state=[tempNode.rows, tempNode.columns]))

        for idx in range(len(orgNode.columns)): # gives a variable
            tempNode = deepcopy(orgNode)
            var = tempNode.columns[idx]
            tempVar = deepcopy(var)
            if (len(var.domain) <= 1):
                continue
            for domainIdx in range(len(var.domain)):
                var.setDomain([tempVar.domain[domainIdx]])
                kids.append(NonogramNode(state=[tempNode.rows, tempNode.columns]))


        return kids

    def addKid(self, node, kid):
        node.addKid(kid)

    def arc_cost(self, kid, node):
        return 1

    def foundSolution(self, node, goalState):
        try:
            node.solve()
            return node.hasFoundSolution
        except Exception as e:
            return False
