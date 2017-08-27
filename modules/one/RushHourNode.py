class SearchNode:
    def __init__(self, state=None, g=None, h=None, f=None, status=None, parent=None, kids=[]):
        self.state = state
        self.gValue = g
        self.hValue = h
        self.fValue = f
        self.status = status
        self.parent = parent
        self.kids = kids

    def __repr__(self):
        return "state: " + str(self.state) +  " g: " +  str(self.gValue) + " h: " + str(self.hValue) + " f: " + str(self.fValue)

    def getPlayerPiece(self):
        return self.state[0]

    def setGValue(self, value):
        self.gValue = value

    def calculateHValue(self, goal):
        # car that has to get to the goal is always the first in state representation
        value = None
        distanse = 0
        blocks = 0
        car = self.state[0]
        orientation = car[0]
        size = car[-1]
        if(orientation == 0 and (goal[1] == car[2])): # horizontal goal must be on same row
            if (goal[0] > car[1]): # car must drive right
                distanse = goal[0] - (car[1]+(size-1)) # 5 - (2 + (1)) = 5 - 3 = 2 steps, (2 + 1) = position or right side of car
            else:
                distanse = goal[0] - car[2] # 5 - (2 + (1)) = 5 - 3 = 2 steps

        # Find how many pieces blocks the road.
        for i in range(1,len(self.state)): # doent count the car we play
            # if the piece "touches" the same row as the goal, it's a obsticle
            playingPiece = self.state[i]
            # if the playingPiece starts / is on the same same row.
            if (playingPiece[2] == goal[1]):
                blocks += 1
            # if piece does not start on same row, but expands multiple rows (vertical orientation), and expands over the goal row
            elif(playingPiece[0] == 1 and (playingPiece[2]+(playingPiece[-1] - 1)) == goal[1]):
                blocks += 1

        self.hValue = distanse + blocks

        # elif(orientation == 1 and (goal[0] == car[1])): # vertical goal must be on same col
        #     pass
        # else:
        #     raise Exception("Cannot be solved, car and goal does not align")

    def getFValue(self):
        self.fValue = self.gValue + self.hValue
        return self.fValue
