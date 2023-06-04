#this code is part of Challenging Tic Tac Toe
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
            #we need to check if it ia valid entry. if it is not an integer...
            #or if the spot is not available on the board-> invalid
            try:
                val = int(sq)
                if val not in game.available_moves():
                    raise ValueError
                valid_sq = True
            except ValueError:
                print('Invalid square, try another input')
        return val

class GenicomputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            #to get the square based on Minimax algorithm
            squ = self.minimax(game, self.letter)['position']
        return squ

    def minimax(self, stage, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        # swich players

        #first we need to check if we already have a winner, the base case
        if stage.current_winner == other_player:
            #we return the score to keep track of the score -> helps the minimax
            return {"position": None, "score": 1 * (stage.num_empty_squares() + 1) if other_player == max_player else -1 * (stage.num_empty_squares() + 1)}
        elif not stage.empty_squares(): # no emty empty_squares
            return {'position' : None,'score' : 0} # each score should be maximised
        #initialising some dictnories
        if player == max_player:
            best = {'position' : None, 'score' : -math.inf } #each score should maximizeimise
        else:
            best = {'position' : None, 'score' : math.inf }#each score should minimise
        for possible_move in stage. available_moves():
            #step1 : make a move, try a spot
            stage.make_move(possible_move, player)
            #step 2 :recurse using Minimaxto stimulate a game after making that move
            simu_score = self.minimax(stage, other_player)# now , we alternate player
            #step 3 : undo the move
            stage.board[possible_move] =' '
            stage.current_winner = None
            simu_score['position'] =possible_move #other will get messed up
            #step 4 : update the dict if necessary
            if player == max_player: # maximizing the max_player
                if simu_score['score'] > best['score']:
                    best = simu_score # replace the best
            else: #minimizing the other_player
                if simu_score['score'] < best['score']:
                    best = simu_score # replace the best
        return best
