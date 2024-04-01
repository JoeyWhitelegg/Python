# A guess the number game.

import random
secretNumber = random.randint(1, 20)
guessAmount = 0

print("I'm thinking of a number between 1 and 20. You may have six guesses to find out the answer.")

for guessTaken in range(1, 7):
    print('Take a guess.')
    guessTaken = int(input())
    if guessTaken < secretNumber:
        print('Your guess is too low.')
        guessAmount += 1
    elif guessTaken > secretNumber:
        print('Your guess is too high.')
        guessAmount += 1
    if guessTaken == secretNumber:
        guessAmount += 1
        print('Great job! You have guessed my number in ' + str(guessAmount) + ' guesses.')
if guessTaken != secretNumber:
        print("Nope, you're an idiot of the worst kind. My number was " + str(secretNumber) + '.')
