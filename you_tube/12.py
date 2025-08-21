#Tosh qaychi qog'oz
import random
options = ('paper', 'rock', 'scissors')
running=True
while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('Enter paper or rock or scissors: ')
    print(f'Player choose: {player}')
    print(f'Computer choose:{computer}')
    if player == computer:
        print('Draw')
    elif player == 'paper' and computer == 'rock':
        print('You win!')
    elif player == 'rock' and computer == 'scissors':
        print('You win!')
    elif player == 'scissors' and computer == 'paper':
        print('You win!')
    else:
        print('You lose!')
    if not input('Play again? (y/n): ').lower().startswith('y'):
        running=False
print('Thank you for playing!')