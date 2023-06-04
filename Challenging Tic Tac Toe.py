# use Minimax, uitility function, see player1.py for it
# if it's X's chance, we need to maximize the cance of x to win
from player_1 import HumanPlayer, GenicomputerPlayer,RandomComputerPlayer
import time
class TicTacToe:
    #to create the board
    def __init__(self):
        self.board = [' ' for _ in range(9)]# we will use a single list to represent 3*3 board
        self.current_winner = None# to keep track of the winner initally no-one


    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        #0|1|2 gives which number to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            #['x','x','o'] --> [(0,'x'),(1,'x'),(2,'o')]
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in row anywhere, all possibilities
        row_ind = square // 3# how many times 3 is gettiung squared
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True # same letter 3 in a row
 # in column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
# now finally the diagonalsif thex's are in diagoanl values ie, (0,2,6,8,4)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game! or None wich is a tie
    if print_game:
        game.print_board_nums()

    letter = 'X'
     #starting letter
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        # let's  define function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
            return letter

        letter = 'O' if letter == 'X' else 'X'# to switch players
    #to dely, to read things properly
    time.sleep(1)
    if print_game:
        print("It's a tie!")

if __name__ == "__main__":
    x_wins = 0
    o_wins = 0
    ties = 0
    for x in range(1000):
        x_player = RandomComputerPlayer('X')
        o_player = GenicomputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties +=1
        print(f'after 1000 ittration we can see that number of \n "X" wins : {x_wins} \n "O" wins : {o_wins} \n "ties" : {ties}')
