# ROCK PAPER SCISSORS GAME

import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0      # these variables keep track of the score
ties = 0


while True:     # main loop of the game
    print(f'%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit.')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # will quit the program

        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s, or q.')
    # display what the player chose
    if playerMove == 'r':
        playerMove = 'r'
        print('ROCK vs...')
    elif playerMove == 'p':
        playerMove = 'p'
        print('PAPER vs...')
    elif playerMove == 's':
        playerMove = 's'
        print('SCISSORS vs...')

    # display the computer choice
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

        # display result and the record
    if playerMove == computerMove:
        print("It's a tie.")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose.')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose.')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose.')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = losses + 1



