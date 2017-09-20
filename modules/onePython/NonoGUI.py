from tkinter import *
from NonogramBFS import NonogramBFS
from time import sleep

class NonoGUI:
    def __init__(self):
        self.astar = None
        self.solution = None
        self.gui = Tk()

        self.frame = Frame(self.gui)
        self.frame.grid(row=4, column=2)
        self.first = True

        self.file = StringVar()
        self.board = None
        Label(text="", padx=10).grid(row=0, column=8)
        Label(text="Skriv inn filnavn på brett:", padx=10).grid(row=0, column=0)
        Entry(textvariable=self.file).grid(row=1, column=0)
        Button(bg="#469683", highlightbackground="#469683",padx=33, pady=5, text="Solve: ", command=lambda : self.findSolution()).grid(row=4, column=0)
        # self.infoText = Label(text="", padx=10)
        # self.infoText.grid(row=5, column=9)

        self.gui.mainloop()

    def drawState(self, rows, cols):
        for i in range(len(self.solution)):
            row = self.solution[i].domain
            for j in range(len(row[0])):
                if row[0][j] == 1:
                    Button(self.frame, highlightbackground="#394f3f", bg="#394f3f", padx=10, pady=5, state=DISABLED).grid(row=i, column=j+2)
                else:
                    Button(self.frame, highlightbackground="#c0c3c6", bg="#c0c3c6", padx=10, pady=5, state=DISABLED).grid(row=i, column=j+2)

        self.gui.update()

        # self.board = [[Button(highlightbackground="#c0c3c6", bg="#c0c3c6", wraplength=1, state=DISABLED, padx=20, pady=15) for c in range(rows)] for r in range(cols)]
        # for r in range(0, rows):
        #     for c in range(0, cols):
        #         Button(bg="#c0c3c6", state=DISABLED, padx=20, pady=15).grid(row=r, column=c)
        #         # self.board[r][c].grid(row=r, column=c)
        # colors = ["#db1a1a", "#db811a", "#d8c81a", "#56d819", "#19d87e", "#14ccb3", "#1388cc", "#1215c9", "#7414ce",
        #           "#c611ba", "#c60f6b", "#47557c", "#394f3f"]


        # if(index < len(self.solution)):
        #     board = [["-" for c in range(6)] for r in range(6)]
        #     state = self.solution[index].getState()
        #     for i in range(len(state)):
        #         car = state[i]
        #         orientation = car[0]
        #         pieceSize = car[3]
        #         # x = 1 = col, y = 2 = row
        #         board[car[2]][car[1]] = str(i)
        #         if orientation == 0:  # horizontal = col
        #             for size in range(pieceSize):
        #                 board[car[2]][car[1] + (size)] = str(i)
        #         elif orientation == 1:  # vertical = row
        #             for size in range(pieceSize):
        #                 board[car[2] + (size)][car[1]] = str(i)
        #     # print the board
        #     for r in range(len(board)):
        #         row = board[r]
        #         for c in range(len(row)):
        #             col = row[c]
        #             if(str(col) == "-"):
        #                 self.board[r][c].configure(highlightbackground="#c0c3c6", bg="#c0c3c6")
        #             else:
        #                 self.board[r][c].configure(highlightbackground=colors[int(col)], bg=colors[int(col)])
        #     self.gui.update()
        #     sleep(0.2)
        #     self.drawState(index + 1)


    def findSolution(self):
        if not self.first:
            self.frame.destroy()
            self.frame = Frame(self.gui)
            self.frame.grid(row=4, column=2)
        self.first = False
        # self.infoText.configure(text="")
        self.nono = NonogramBFS(task=self.file.get())
        self.solution = self.nono.solve()
        self.drawState(self.nono.numRows, self.nono.numColumns)
        # self.infoText.configure(text="Steps: " + str(len(self.solution)-1) + "\n Nodes generated: " + str(len(self.astar.states)))


if __name__ == "__main__":
    g = NonoGUI()
