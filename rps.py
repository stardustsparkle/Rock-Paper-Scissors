
import random
moves = ['rock', 'paper', 'scissors']


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        h = input("Rock, paper, scissors? >").lower()
        while h not in moves:
            h = input("Rock, paper, scissors? >").lower()
        return h


class ReflectPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        return my_move, their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.my_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        return my_move, their_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            if self.my_move == "rock":
                return "paper"
            elif self.my_move == "paper":
                return "scissors"
            elif self.my_move == "scissors":
                return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0
        self.gameround = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            print("** PLAYER ONE WINS **")
            self.p1score += 1
            self.gameround += 1
            print(f"Score: P1 {self.p1score}, P2 {self.p2score}")
        elif beats(move2, move1) is True:
            print("** PLAYER TWO WINS **")
            self.p2score += 1
            self.gameround += 1
            print(f"Score: P1 {self.p1score}, P2 {self.p2score}")
        else:
            print("** DRAW GAME **")
            self.gameround += 1
            print(f"Score: P1 {self.p1score}, P2 {self.p2score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        if self.p1score > self.p2score:
            print(f"P1: {self.p1score} ... P2: {self.p2score}")
            print("PLAYER ONE WINS!")
        elif self.p2score > self.p1score:
            print(f"P1: {self.p1score} ... P2: {self.p2score}")
            print("PLAYER TWO WINS!")
        else:
            print(f"P1: {self.p1score} ... P2: {self.p2score}")
            print("DRAW GAME")


if __name__ == '__main__':
    rng = random.randint(1, 4)
    if rng == 1:
        game = Game(HumanPlayer(), Player())
    elif rng == 2:
        game = Game(HumanPlayer(), CyclePlayer())
    elif rng == 3:
        game = Game(HumanPlayer(), ReflectPlayer())
    else:
        game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
