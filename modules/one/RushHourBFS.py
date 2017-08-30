from RushHourNode import SearchNode

class RushHourBFS:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.board = self.createBoard()
        self.available = self.createBoard()


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
            elif(playingPiece[0] == 1 and playingPiece[1] > car[1] and playingPiece[2] <= goal[1] and (playingPiece[2]+(playingPiece[-1] -1)) > goal[1]):
                blocks += 1

            # Check if middel of a size 3 car is in the way of goal

        return distanse + blocks

        # elif(orientation == 1 and (goal[0] == car[1])): # vertical goal must be on same col
        #     pass
        # else:
        #     raise Exception("Cannot be solved, car and goal does not align")


    ''' Rember to check if moveing will be outside "board" (use self.boardSize) '''
    def generateSuccessors(self, node):
        ''' each piece can move 2 directions, 2 directions * number of pieces === numPiexes ^2 successors at most '''
        successors = []
        return successors
        # a new successor is when we make a legal move on a playing piece. so if one piece can move both one position left or right, one new state is moving left, and one new state is moving right
        # first we need to know what direction we can move the piece
        for pieceNumber in range(len(node.getState())):
            car = node.getCarNumber(pieceNumber)
            direction = car[0]
                # if direction = 0 : right side of car, or if direction = 1, downSide
            expandedSide = car[1] + (car[-1] - 1) # car 0 = dir, 1 = col, 2 = row, 3 = size

            if(direction == 0): # horisontal direction (we can move left or right)
                pass
                # check IF right is blocked, if not, new state
                for direction in ["l","r"]:
                    move = self.checkIfMoveIsPossible(car, direction, node.getState())
                    if(move):
                        successors.append(move)
            else: # vertical, move up or down
                for direction in ["u","d"]:
                    move = self.checkIfMoveIsPossible(car, direction, node.getState())
                    if(move):
                        successors.append(move)




    def checkIfMoveIsPossible(self, car, direction, state):
        col = car[1]
        row = car[2]
        moveIsPossible = True
 
        # if no other cars are on position car[1] - 1 --> new state
        for playingPiece in state:
            if (direction == "l" or direction == "r"):
                # check if the playing piece tries to move outside the board
                hDiff = 0
                pDiff = 0
                
                if(direction == "l"):
                    if(col ==  0 ):
                        return False
                    hDiff = -1
                    pDiff = playingPiece[-1] -1
                elif (direction == "r"):
                    if(col + (car[-1] - 1)  ==  self.boardSize -1):
                        return False
                    hDiff = car[-1]
                # if piece is on same row as playing piece, and we want to go left, check that piece ends just left of playing piece, or if right, that it starts just right for playing piece. diff controls this.
                if (playingPiece[2] == row and (playingPiece[1] + pDiff  == col + hDiff)):
                    moveIsPossible = False
                # if piece does not start on same row, but expands multiple rows (vertical orientation), and expands over the goal row
                elif(playingPiece[0] == 1 and playingPiece[1] == col + hDiff and playingPiece[2] <= row and (playingPiece[2]+(playingPiece[-1] -1)) >= row):
                    moveIsPossible = False
            elif (direction == "u" or direction == "d"):
                vDiff = 0
                pDiff = 0
                if (direction == "u"):
                    if(row == 0):
                        return False
                    vDiff = -1
                    pDiff = playingPiece[-1] -1
                elif (direction == "d"):
                    if(row + (car[-1] -1) ==  self.board -1):
                        return False
                    vDiff = car[-1]
                # if piece is horisontically alligned over our current playing piece.
                if (playingPiece[0] == 0 and playingPiece[2] == row + vDiff  and (playingPiece[1] <= col) and (playingPiece[1] + (playingPiece[-1] -1) >=  col)):
                    moveIsPossible = False
                # if piece is vertically alligend over our current playing piece.
                elif (playingPiece[0] == 1 and (playingPiece[2] + pDiff == row + vDiff)  and (playingPiece[1] == col)):
                    moveIsPossible = False
        # retrun if move is possible
        return moveIsPossible        

        






