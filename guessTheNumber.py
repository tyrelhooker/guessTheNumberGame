# Guess the Number Game
import random

randomNumber = random.randint(1, 5)

while True:
    userNumber = input('Please enter a number between 1 and 5:  ')
    try:
        val = int(userNumber)
        print('You have chosen the number: ', val)

        if val in range(1, 6):
            if val == randomNumber:
                print('You have correctly guessed the number.')
                break
            else:
                print('You have not correctly guessed the number. Please try '
                      'again.')
        else:
            print('number out of range')
            # continue
    except ValueError:
        print('Not a number')
