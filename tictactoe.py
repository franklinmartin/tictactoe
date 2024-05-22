class tictactoe:
    running = False
    gamestate = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    def __len__(self):
        c = 0
        for s in self.gamestate:
            if s != "-":
                c += 1
        return c
    @classmethod
    def set_base_state(self):
        self.gamestate = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

    def set_state(self, gamestate):
        self.gamestate = gamestate
        
    def get_state(self):
        return self.gamestate

    def __init__(self, gamestate):
        self.set_state(gamestate)
    def __init__(self):
        pass

    def print(self):
        printout = "\n"
        for i in range(0, len(self.gamestate)):
            if (i + 1) % 3 == 0:
                printout += self.gamestate[i] + "\n"
            else:
                printout += self.gamestate[i] + " "
        print(printout + "board.")

    def print_loc(self):
        printout = ""
        for i in range(0, len(self.gamestate)):
            if (i + 1) % 3 == 0:
                printout += str(i + 1) + "\n"
            else:
                printout += str(i + 1) + " "
        print(printout + "position.")

    def print_test(self, list):
        for i in 0, 3, 6:
            print("\n")
            for j in 0, 1, 2:
                print(list[i+j], end= ' ')
        print()

    def bot(self):
        for i in self.gamestate:
            print(self.gamestate[slice(3)])

    def run(self):
        self.running = True
        choice = ""
        while choice != "4":
            print("+++++++++++++++++++++++++++++++++++++")
            #self.print_test(self.gamestate)
            print("Enter input as i.e. 2x")
            #self.print_loc()
            self.print()
            choice = input("Your turn:")
            choice = choice.split()
            #choice = choice[:1]
            choice_pos = int(choice[0]) - 1
            choice_val = choice[1]
            self.gamestate[choice_pos] = choice_val
            print("-------------------------------------")
        


tictactoe = tictactoe()
tictactoe.run()




