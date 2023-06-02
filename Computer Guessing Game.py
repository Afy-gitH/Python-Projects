import random
def computer_guess(num):
    low = 1
    high = num
    feedback = " "
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), toom low (L), or correct (C)").lower()
        if feedback == 'h':
            #the guess is too high , we need to udjust the upper bound
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'yay found your guess : {guess}')
computer_guess(int(input("what's the upper limit you are aiming for :")))
