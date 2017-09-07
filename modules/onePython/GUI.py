from tkinter import *
from Astar import Astar
from time import sleep

class GUI:
    def __init__(self):
        self.astar = Astar()
        self.solution = None
        self.gui = Tk()
        # for c in range(0, 6):
        #     for r in range(0, 6):
        #         Button(bg="#c0c3c6", state=DISABLED, padx=20, pady=15).grid(row=r, column=c, sticky='news')

        self.board = [[Button(bg="#c0c3c6", state=DISABLED, padx=20, pady=15) for c in range(6)] for r in range(6)]
        for r in range(6):
            for c in range(6):
                self.board[r][c].grid(row=r, column=c)
        Button(bg="#FFFFFF", state=DISABLED, padx=3, pady=15).grid(row=2, column=6, sticky='news')
        Button(bg="#118391", padx=30, pady=15, text="Solve:", command=self.findSolution).grid(row=0, column=8, sticky='news')
        self.gui.mainloop()

    def drawState(self, index):
        colors = ["#db1a1a", "#db811a", "#d8c81a", "#56d819", "#19d87e", "#14ccb3", "#1388cc", "#1215c9", "#7414ce",
                  "#c611ba", "#c60f6b", "#47557c", "#394f3f"]
        if(index < len(self.solution)):
            board = [["-" for c in range(6)] for r in range(6)]
            state = self.solution[index].getState()
            for i in range(len(state)):
                car = state[i]
                orientation = car[0]
                pieceSize = car[3]
                # x = 1 = col, y = 2 = row
                board[car[2]][car[1]] = str(i)
                if orientation == 0:  # horizontal = col
                    for size in range(pieceSize):
                        board[car[2]][car[1] + (size)] = str(i)
                elif orientation == 1:  # vertical = row
                    for size in range(pieceSize):
                        board[car[2] + (size)][car[1]] = str(i)
            # print the board
            for r in range(len(board)):
                row = board[r]
                for c in range(len(row)):
                    col = row[c]
                    if(str(col) == "-"):
                        self.board[r][c].configure(bg="#c0c3c6")
                    else:
                        self.board[r][c].configure(bg=colors[int(col)])
            self.gui.update()
            sleep(0.2)
            self.drawState(index + 1)

    def findSolution(self):
        self.solution = self.astar.solve()
        self.drawState(0)


if __name__ == "__main__":
    g = GUI()
