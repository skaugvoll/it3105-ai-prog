from RushHourNode import SearchNode

class RushHourBFS:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.board = self.createBoard()


    def createBoard(self):
        board = [ [ "-" for c in range(self.boardSize) ] for r in range(self.boardSize) ]
        return board

    def drawBoard(self, states):
        # place the pieces on the board
        print(states)
        for playingPiece in states[-1].state:
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


    def getInitalState(self, file):
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


    def calculateHValue(self, node, goal):
        # car that has to get to the goal is always the first in state representation
        value = None
        distanse = 0
        blocks = 0
        car = node.state[0]
        orientation = car[0]
        size = car[-1]
        if(orientation == 0 and (goal[1] == car[2])): # horizontal goal must be on same row
            if (goal[0] > car[1]): # car must drive right
                distanse = goal[0] - (car[1]+(size-1)) # 5 - (2 + (1)) = 5 - 3 = 2 steps, (2 + 1) = position or right side of car
            else:
                distanse = goal[0] - car[2] # 5 - (2 + (1)) = 5 - 3 = 2 steps

        # Find how many pieces blocks the road.
        for i in range(1,len(node.state)): # doent count the car we play
            # if the piece "touches" the same row as the goal, it's a obsticle
            playingPiece = node.state[i]
            # if the playingPiece starts / is on the same same row.
            if (playingPiece[2] == goal[1]):
                blocks += 1
            # if piece does not start on same row, but expands multiple rows (vertical orientation), and expands over the goal row
            elif(playingPiece[0] == 1 and (playingPiece[2]+(playingPiece[-1] - 1)) == goal[1]):
                blocks += 1

        return distanse + blocks

        # elif(orientation == 1 and (goal[0] == car[1])): # vertical goal must be on same col
        #     pass
        # else:
        #     raise Exception("Cannot be solved, car and goal does not align")
