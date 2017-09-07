from tkinter import *
from Astar import Astar
from time import sleep

class GUI:
    def __init__(self):
        self.astar = Astar("tasks/easy.txt")
        self.solution = None
        gui = Tk()
        for c in range(0, 6):
            for r in range(0, 6):
                Button(bg="#c0c3c6", state=DISABLED, padx=20, pady=15).grid(row=r, column=c, sticky='news')
        Button(bg="#448391", state=DISABLED, padx=3, pady=15).grid(row=2, column=6, sticky='news')
        Button(bg="#118391", padx=30, pady=15, text="Solve:", command=self.findSolution).grid(row=0, column=8, sticky='news')
        gui.mainloop()

    def findSolution(self):
        self.solution = self.astar.solve()
        colors = ["#db1a1a", "#db811a", "#d8c81a", "#56d819", "#19d87e", "#14ccb3", "#1388cc", "#1215c9", "#7414ce",
                  "#c611ba", "#c60f6b", "#47557c", "#394f3f"]
        for step in self.solution:
            # time.sleep(2)
            # self.clearBoard()
            state = step.getState()
            for i in range(len(state)):
                car = state[i]
                orientation = car[0]
                pieceSize = car[3]

                # x = 1 = col, y = 2 = row
                if orientation == 0:  # horizontal = col
                    for size in range(pieceSize):
                        Button(bg=colors[i], state=DISABLED, padx=20, pady=15).grid(row=car[2], column=car[1] + size,
                                                                                    sticky='news')
                # self.board[playingPiece[2]][playingPiece[1]+(pieceSize-1)] = "x"
                elif orientation == 1:  # vertical = row
                    for size in range(pieceSize):
                        Button(bg=colors[i], state=DISABLED, padx=20, pady=15).grid(row=car[2] + size, column=car[1],
                                                                                    sticky='news')
if __name__ == "__main__":
    g = GUI()

