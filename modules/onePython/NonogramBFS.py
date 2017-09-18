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
                else:
                    columns.append(line)
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


    def getAllPermutations(self, elementString):
        # all permutations # contains duplicates... (1,2) and (2,1) == duplicates.
        perms = set([''.join(p) for p in permutations(elementString, r=self.numRows)])
        print("perms: " + str(perms))

        # remove all illegal permutaitons with regards to domain constraints.





def main():
    nono = NonogramBFS()
    nono.getInitalState("tasks/nono-cat.txt")

main()