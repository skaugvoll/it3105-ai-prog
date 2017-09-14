from abc import ABC, abstractmethod

class BFS(ABC):
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.board = self.createBoard()
        self.available = self.createBoard()

    @abstractmethod
    def createBoard(self):
        board = None
        return board

    @abstractmethod
    def drawBoard(self, state):
        self.board = self.createBoard()
        # place the pieces on a fresh board
        # print board.
        pass

    @abstractmethod
    def getInitalState(self, fileWithInitState):
        # create representation of first state.
        # e.g read in from file, create a searchNode for the state,
        # return searchNode - init state
        pass

    @abstractmethod
    def calculateHValue(self, node, goal):
        pass

    @abstractmethod
    def generateSuccessors(self, node):
        ''' Rember to check if moveing will be outside "board" (use self.boardSize) '''
        pass

    @abstractmethod
    def addKid(self, node, kid):
        node.addKid(kid)

    @abstractmethod
    def arc_cost(self, kid, node):
        pass

