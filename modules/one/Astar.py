import sys
from RushHourNode import SearchNode

# commandline parameters: initalStateFile, goalState, boardSize,
class Astar:
    def __init__(self):
        self.CLOSED = [] # visited and expanded
        self.OPEN = [] # found and to be expanded
        self.boardSize = 6 # should be a sys arg.
        self.states = [self._getInitalState(sys.argv[1])] # the inital state filename.
        self.goalState = (5,2) # sys.argv[2]
        self.board = self._createBoard()
        self.drawBoard()

    def _getInitalState(self, file):
        state = []
        try:
            initialState = open(file, 'r')
            for line in initialState: # for each playing piece
                line = line.replace('\n','') # remove unvalid character
                line = line.split(',') # create a list of coordinates / meta data
                line = map(lambda x: int(x), line) # change type from string to int
                state.append(tuple(line))
            # print(initialState)
            searchNode = SearchNode(state=state) # crate a state-node, with a state-tuple representing the entire state and append to state
            initialState.close()
            return searchNode
        except:
            raise Exception("Something went wrong when making inital state")

    def getCurrentState(self):
        return self.states[-1]

    def _createBoard(self):
        board = [ [ "-" for c in range(self.boardSize) ] for r in range(self.boardSize) ]
        return board

    def drawBoard(self):
        # place the pieces on the board
        print(self.states)
        for playingPiece in self.states[-1].state:
            orientation = playingPiece[0]
            pieceSize = playingPiece[3]
            # x = 1 = col, y = 2 = row
            self.board[playingPiece[2]][playingPiece[1]] = "x"
            if(orientation == 0): # horizontal = col
                for size in range(pieceSize):
                    self.board[playingPiece[2]][playingPiece[1]+(size)] = "x"

                # self.board[playingPiece[2]][playingPiece[1]+(pieceSize-1)] = "x"
            elif(orientation == 1): # vertical = row
                for size in range(pieceSize):
                    self.board[playingPiece[2]+(size)][playingPiece[1]] = "x"

        # print the board
        for row in self.board:
            string = ""
            for column in row:
                string += str(column)
            print(string)


    def _sortBasedOnFValue(self, x, y):
        return x.getFValue() - y.getFValue()

    def _sortAgenda(self):
        self.OPEN.sort(self._sortBasedOnFValue(x,y))

    def _popFromAgenda(self):
        self._sortAgenda()
        return self.OPEN.pop(0) # return the first element from the agenda / open list. (the node / state with lowest f-value)





    def solve(self):
        pass
        # do the inital work.
        # pop the inital state
        node = self.getCurrentState()
        # set g value to 0,
        node.setGValue(0)
        # set h value to estimation.
        node.calculateHValue(self.goalState)
        print(node)




def main():
    algo = Astar()
    # algo.getCurrentState()
    algo.solve()

main()
