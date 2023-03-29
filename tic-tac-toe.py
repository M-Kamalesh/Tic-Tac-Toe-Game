import numpy as np

class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def symbol(self):
        while True:
            try:
                self._symbol = input("\n{name}, select a symbol 'X' or 'O': ".format(name=self.name))
            except ValueError:
                print("\t\tOops!!! Enter a valid symbol \N{thinking face}")
                continue
            if self._symbol == 'X' or self._symbol == 'O':
                break
            else:
                print("\t\tOops!!! Enter a valid symbol \N{thinking face}")
    def choose(self, selected_values):
         
         while True:
            try:
                self.choice = input("\n{name}, select the position: ".format(name=self.name))
                value = int(self.choice)
            except ValueError:
                print("\t\tOops!!! Enter a valid symbol \N{thinking face}")
                continue
            if value >= 1 and value <= 9 and value not in selected_values:
                selected_values.append(value)
                break
            else:
                print("\t\tOops!!! Enter a valid symbol \N{thinking face}")
    def incrementPoint(self):
        self.points += 1
        
class GameRound:
    def __init__(self, p1, p2):
        count = 1
        selected_values = []
        box = np.array([
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ])
        self.display(box)
        while True:
            p1.choose(selected_values)
            box[np.where(box==p1.choice)] = p1._symbol
            self.display(box)
            result = self.check(box)
            if result != None or count == 9:
                break
            count += 1
            p2.choose(selected_values)
            box[np.where(box==p2.choice)] = p2._symbol
            self.display(box)
            result = self.check(box)
            if result != None or count == 9:
                break
            count += 1
        if result == p1._symbol:
            print("\nRound resulted as favour to {name} \N{hugging face}.".format(name=p1.name))
            p1.incrementPoint()
        elif result == p2._symbol:
            p2.incrementPoint()
            print("\nRound resulted as favour to {name} \N{hugging face}.".format(name=p2.name))
        else: 
            print("No points for anybody \N{neutral face}.")
    def check(self, box):
        for i in range(2):
            if box[i][0] == box[i][1] == box[i][2]:
                return box[i][0]
        for i in range(2):
            if box[0][i] == box[1][i] == box[2][i]:
                return box[0][i]
        if box[0][0] == box[1][1] == box[2][2]:
            return box[1][1]
        if box[0][2] == box[1][1] == box[2][0]:
            return box[1][1]
    def display(self, box):
        print("\n\n ",box[0][0],' |', box[0][1], ' |', box[0][2],
            '\n',"____|____|____", '\n',"",box[1][0],' |', box[1][1], ' |', box[1][2],
            '\n',"____|____|____",'\n',"",box[2][0],' |', box[2][1], ' |', box[2][2],
            '\n',"    |    |")    
class Game:
    def __init__(self, name1, name2):
        self.endGame = False
        self.participant_1 = Participant(name1)
        self.participant_2 = Participant(name2)
        self.participant_1.symbol()
        self.participant_2.symbol()
    def start(self):
        while not self.endGame:
            GameRound(self.participant_1, self.participant_2)
            self.checkEndCondition()
    def checkEndCondition(self):
        answer = input("\nContinue game y/n: ")
        if answer == 'y':
            GameRound(self.participant_1, self.participant_2)
            self.checkEndCondition()
        else:
            print("\nGame ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name=self.participant_1.name, p1points=self.participant_1.points, p2name=self.participant_2.name, p2points=self.participant_2.points))
            self.determineWinner()
            self.endGame = True
    def determineWinner(self):
        resultString = "\nIt's a Draw"
        if self.participant_1.points > self.participant_2.points:
            resultString = "\nWinner is {name} \N{smiling face with halo}".format(name=self.participant_1.name)
        elif self.participant_1.points < self.participant_2.points:
            resultString = "\nWinner is {name} \N{smiling face with halo}".format(name=self.participant_2.name)
        print(resultString)

print('\n-----$$$$$ WELCOME TO PLAY TIC - TAC - TOE $$$$$-----')
name1 = input('\nEnter player 1 name: ')
name2 = input('\nEnter player 2 name: ')
game = Game(name1, name2)
game.start()
