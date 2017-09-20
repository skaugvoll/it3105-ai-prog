from tkinter import *
from NonogramBFS import NonogramBFS
from NonogramNode import NonogramNode
from NonogramVariable import NonogramVariable
from time import sleep
from AstarClass import ASTAR

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

    def drawState(self, rows):
        for i in range(len(rows)):
            row = rows[i].domain
            for j in range(len(row[0])):
                if row[0][j] == 1:
                    Button(self.frame, highlightbackground="#394f3f", bg="#394f3f", padx=10, pady=5, state=DISABLED).grid(row=i, column=j+2)
                else:
                    Button(self.frame, highlightbackground="#c0c3c6", bg="#c0c3c6", padx=10, pady=5, state=DISABLED).grid(row=i, column=j+2)

        self.gui.update()


    def findSolution(self):
        if not self.first:
            self.frame.destroy()
            self.frame = Frame(self.gui)
            self.frame.grid(row=4, column=2)
        self.first = False
        # self.infoText.configure(text="")
        # self.nono = NonogramBFS(task=self.file.get())
        # self.solution = self.nono.solve()
        fil = "nono-"
        fil += self.file.get()
        self.astar = ASTAR(problem=NonogramBFS(), goal=0, initStateFile=fil, algo="Astar")
        self.solution = self.astar.solve()

        self.drawState(self.solution[-1].getSolution())
        # self.infoText.configure(text="Steps: " + str(len(self.solution)-1) + "\n Nodes generated: " + str(len(self.astar.states)))


if __name__ == "__main__":
    g = NonoGUI()
