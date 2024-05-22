class TTT:
    gamestate = [-1]*9
    marks = ["-"]*9

    def to_state(self):
        gamestate = []
        for m in self.marks:
            if m == "-":
                gamestate.append(-1)
            if m == "O":
                gamestate.append(0)
            if m == "X":
                gamestate.append(1)
        self.gamestate = gamestate
        return gamestate
    
    def to_marks(self):
        marks = []
        for s in self.gamestate:
            if s == -1:
                marks.append("-")
            if s == 0:
                marks.append("O")
            if s == 1:
                marks.append("X")
        self.marks = marks
        return marks

    def __len__(self):
        c = 0
        for s in self.gamestate:
            if s != 0:
                c += 1
        return c

    def __str__(self):
        printout = "\n"
        for i in 0, 3, 6:
            for j in 0, 1, 2:
                printout += " " + self.marks[i+j] + " "
            printout += "\n"
        return printout

    def __init__(self, gamestate:list[int]):
        self.gamestate = gamestate
        self.marks = self.to_marks()

    @classmethod
    def from_str(cls, str):
        gamestate = []
        for c in str:
            if c.isnumeric():
                gamestate.append(int(c))
        return cls(gamestate)
    
    #way too hardcoded
    def calculate_win(self):
        paths = []
        temp = []
        win = 0
        #convert into 3x3
        for i in 0, 3, 6:
            temp.append(self.gamestate[i:i + 3])
        print(temp)

        #check across
        for r in temp:
            paths.append(r)######################
            if set(r) != {-1}:
                print(len(set(r)))
                if len(set(r)) == 1:
                    win += 1
        #check diag
        diag = []
        for i in 0, 1, 2:
            diag.append(temp[i][i])
        if set(diag) != {-1}:
            print(len(set(diag)))
        paths.append(diag)#########################
        #rotate and check "across" (down up)
        #temp = list(zip(*temp[::-1]))
        #rotate and turn 
        temp = list(list(a) for a in zip(*temp[::-1]))
        for r in temp:
            paths.append(r)
            if set(r) != {-1}:
                print(len(set(r)))
        #check diag
        diag = []
        for i in 0, 1, 2:
            diag.append(temp[i][i])
        if set(diag) != {-1}:
            print(len(set(diag)))
        paths.append(diag)#########################
        print(paths)
        print(win)

    def run(self):
        choice = ""
        while choice != "q":
            print(self)

            choice = input("input:")

            choice = choice.split()
            choice_pos = int(choice[0]) - 1
            choice_val = choice[1]

            self.marks[choice_pos] = choice_val
            self.to_state()
#ttt.run()            


#gamestate = [-1]*9
#print(ttt.gamestate)
#print(len(ttt))
#print(ttt.to_marks())
#print(ttt)

#ttt = TTT.from_str("")


#print(ttt)
#print(ttt.to_marks())
#print(TTT.marks)


""" ttt = TTT.from_str("0 0 0 0 0 0 0 0 0")
print(ttt.gamestate)
print(ttt.marks)

ttt = TTT([-1]*9)
print(ttt.gamestate)
print(ttt.marks) """

ttt = TTT([1, 1, 0, 0, 0, 0, -1, -1, -1])
#ttt.run()
print(ttt)


#print(len(set(ttt.gamestate)))


#matrix = [[i + j for i in range(1, 4)] for j in range(0, 9, 3)] 
#matrix = [[ttt.gamestate[i] for i in range(0, 3)] for j in range(0, 3)] 
#print(matrix)

ttt.run()