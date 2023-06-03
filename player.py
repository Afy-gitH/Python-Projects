#this code is part of Tic-Tac-Toe.py
import math
import random
# can be between humans vs humans, humans vs computer
# let's make 2 diffrent classes for each, we can assingn O player and X player
class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # we are going to check that this is a correct values by trying to cast, continuew if its an integer
        valid_sq = False
        val = None
        while not valid_sq:
            sq = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(sq)
                if val not in game.available_moves():
                    raise ValueError
                valid_sq = True
            except ValueError:
                print('Invalid square, try another input')
        return val
