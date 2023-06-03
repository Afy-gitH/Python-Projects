import random

def play():
    user = input("What is your choice: \n 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    if user not in ['r', 'p', 's']:
        print("Oops! Wrong choice. Please enter a valid option.")
        user = input("What is your choice: \n 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print(f'Your choice {user}, computer choice {computer}')
        print("It's a tie")
    elif winner(user, computer):
        print(f'Your choice {user}, computer choice {computer}')
        print('You won!')
    else:
        print(f'Your choice {user}, computer choice {computer}')
        print('You lost!')

def winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

play()
