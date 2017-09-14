
class RushHourBFS:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.board = self.createBoard()
        self.available = self.createBoard()


    def createBoard(self):
        board = None
        return board


    def drawBoard(self, state):
        self.board = self.createBoard()
        # place the pieces on a fresh board
        # print board.
        pass

    def getInitalState(self, fileWithInitState):
        # create representation of first state.
        # e.g read in from file, create a searchNode for the state,
        # return searchNode - init state
        pass


    def calculateHValue(self, node, goal):
        pass


    ''' Rember to check if moveing will be outside "board" (use self.boardSize) '''
    def generateSuccessors(self, node):
        pass


    def addKid(self, node, kid):
        node.addKid(kid)

    def arc_cost(self, kid, node):
        pass