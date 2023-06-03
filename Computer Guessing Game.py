import random
def computer_guess(num):
    low = 1
    high = num
    feedback = " "
     while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # or high, since they are the same
        feedback = input(f"Is {guess} too high (H), toom low (L), or correct (C)").lower()
        if feedback == 'h':
            #the guess is too high , we need to udjust the upper bound
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'yay found your guess : {guess}')
computer_guess(int(input("what's the upper limit you are aiming for :")))
