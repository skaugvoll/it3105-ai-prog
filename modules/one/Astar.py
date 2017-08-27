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
        return self.OPEN.pop(0) # return the first element from the agenda / open list. (the node / state with lowest f-value)

    def _pushToAgenda(self, node):
        self.OPEN.append(node)
        self._sortAgenda()
        # where we should use insertion sort, should speed up the process,
        # instead of sorting the whole list, every time. or possibly a binary seach, since its going to be "sorted"

    def _pushToDone(self, node):
        self.CLOSED.append(node)

    def _nodeIsSolution(self, node):
        car = node.getPlayerPiece()

    def _getSolution(self, node):
        pass




    #should return the path, or failure.
    def solve(self):
        # do the inital work. (much is done in the initialization of Astar)
        # pop the inital state
        node = self.getCurrentState()
        # set g value to 0,
        node.setGValue(0)
        # set h value to estimation.
        node.calculateHValue(self.goalState)
        
        #push initial node to the agenda (open-list)
        self.OPEN.append(node)
        #Agenda loop starts here. While no solution found do:
        while(len(self.OPEN)):
            searchNode = self._popFromAgenda()
            self._pushToDone(searchNode)
            # check if the new node is the goal
            if(self._nodeIsSolution(searchNode)):
                return self._getSolution(SearchNode) # if solution return the path.

            # if not solution, generate all successors / children of seachNode (all possible moves) in this state. (move each piece one step, in both available orientation direction (left/right, or up/down))
                # for each successor do
                # check if the successor has been created before
                # push the successor to the searchNode kids list.

        # if the while loop could not find a solution
        return False



def main():
    algo = Astar()
    # algo.getCurrentState()
    algo.solve()

main()
