import sys
# from RushHourNode import SearchNode
from RushHourBFS import RushHourBFS
from AstarClass import ASTAR
import time

# commandline parameters: initalStateFile, goalState, boardSize,


class Astar(ASTAR):
    def __init__(self, initStateFile, algo):
        self.bfs = RushHourBFS(6) # should be a sys arg.
        self.CLOSED = [] # visited and expanded
        self.OPEN = [] # found and to be expanded
        self.states = [] # the inital state filename.
        self.goalState = (5, 2) # sys.argv[2]
        self.isGen = ()
        self.moves = 0
        self.initState = self.bfs.getInitalState("tasks/" + initStateFile + ".txt")
        self.algo = algo

    def _nodeIsSolution(self, node):
        car = node.getPlayerPiece()
        # for our specific problem, check if right side of playing - car is on goal state
        # if the playing piece is on same row as goal and the right side of the car is on the same column as the goal
        if self.goalState[1] == car[2] and (car[1] + (car[-1] - 1) == self.goalState[0]):
            print(time.time() - self.startTime)
            return True # we found a solution!
        # if not solution
        return False

#
# def main():
#     algo = Astar()
#     # algo.getCurrentState()
#     algo.solve()

# main()
