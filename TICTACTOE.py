class TTT:
    gamestate = [-1]*9
    marks = ["-"]*9
    win = False

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
        win = False
        winner = {}
        
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
                    win = True
                    winner = set(r)
        #check diag
        diag = []
        for i in 0, 1, 2:
            diag.append(temp[i][i])
        if set(diag) != {-1}:
            print(len(set(diag)))
            if len(set(diag)) == 1:
                win = True
                winner = set(diag)
        paths.append(diag)#########################
        #rotate and check "across" (down up)
        #temp = list(zip(*temp[::-1]))
        #rotate and turn 
        temp = list(list(a) for a in zip(*temp[::-1]))
        for r in temp:
            paths.append(r)
            if set(r) != {-1}:
                print(len(set(r)))
                if len(set(r)) == 1:
                    win = True
                    winner = set(r)
        #check diag
        diag = []
        for i in 0, 1, 2:
            diag.append(temp[i][i])
        if set(diag) != {-1}:
            print(len(set(diag)))
            if len(set(diag)) == 1:
                win = True
                winner = set(diag)
        paths.append(diag)#########################
        print(paths)
        self.win = win
        return win, winner, paths

    def check_contained(self, container, path):
        for p in container:
            if path in container:
                return True
        return False
    
    def check_path(self, paths):
        paths = list(paths)
        temp = []
        hold = []
        for i in range(0, len(paths)):
            if len(set(paths[i])) > 1:
                for j in range(0, 2):
                    if(paths[i][j] == paths[i][j+1] or paths[i][j] == paths[i][j-1]):
                        if(self.check_contained(temp, paths[i]) == False):
                            temp.append(paths[i])
        return temp

    def convert(self, value):
        if value == 1:
            return "X"
        if value == 0:
            return "O"
        if value == -1:
            return "-"
        if value == "X":
            return 1
        if value == "O":
            return 0
        if value == "-":
            return -1
        
    def check(self, input):
        if input != ("X" or "O"):
            return False
        
    def run(self):
        choice = ""
        while choice != "q" and self.win is False:
            print("Enter position and value:")
            print("\n example: 1 X")
            print(" example: 9 O")
            print(self)
            choice = input("input:")

            choice = choice.split()
            choice_pos = int(choice[0]) - 1
            choice_val = choice[1]

            self.marks[choice_pos] = choice_val
            self.to_state()

            calc_win = self.calculate_win()
            paths = calc_win[2]
            print(self.check_path(paths))

"""             if calc_win[0]:
                print(self.convert(list(calc_win[1])[0])) """

ttt = TTT([1, 1, 0, 0, 0, 0, -1, -1, -1])
ttt.run()