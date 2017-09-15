import sys
# from RushHourNode import SearchNode
from RushHourBFS import RushHourBFS
# from NonogramBFS import NonogramBFS
from AstarClass import ASTAR
import time

# commandline parameters: initalStateFile, goalState, boardSize,


def rushHourSolver(problem, goal, task, algo):
    astar = ASTAR(problem, goal, task, algo)
    return astar




