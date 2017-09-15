from BFSclass import BFS

class nonogramsBFS(BFS):
    def __init__(self):
        pass

    def createBoard(self):
        board = [["-" for c in range(self.boardSize)] for r in range(self.boardSize)]
        return board


    def drawBoard(self, state):
        self.board = self.createBoard()
        # place the pieces on the board
        # print(states)
        for i in range(len(state)):
            playingPiece = state[i]
            orientation = playingPiece[0]
            pieceSize = playingPiece[3]
            # x = 1 = col, y = 2 = row
            self.board[playingPiece[2]][playingPiece[1]] = str(i)
            if orientation == 0: # horizontal = col
                for size in range(pieceSize):
                    self.board[playingPiece[2]][playingPiece[1]+(size)] = str(i)

                # self.board[playingPiece[2]][playingPiece[1]+(pieceSize-1)] = "x"
            elif orientation == 1: # vertical = row
                for size in range(pieceSize):
                    self.board[playingPiece[2]+(size)][playingPiece[1]] = str(i)

        # print the board
        for row in self.board:
            string = ""
            for column in row:
                string += str(column)
            print(string)

    def getInitalState(self, fileWithInitState):
        state = []
        try:
            initialState = open(fileWithInitState, 'r')
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
