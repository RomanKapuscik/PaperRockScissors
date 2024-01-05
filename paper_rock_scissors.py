import random

options = ('paper', 'rock', 'scissors')

answer_to_win = {'paper': 'scissors',
                 'rock':'paper',
                 'scissors':'rock'}

rounning = True
score = 0


def game_result(player: str, computer: str) -> int:
    if player == computer:
        return 0, 'tide'
    elif answer_to_win[player] == computer:
        return -1, 'lose'
    else:
        return 1, 'win'

while rounning:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input('Enter Your choice (paper, rock, scissors): ').lower()
    
    print(f'Players choice: {player}')
    print(f'Computers choice: {computer}')
    
    result = game_result(player, computer)
    print(f'You {result[1]}!')
    score += result[0]
    
    if input('Do You want to play again? (y/n)').lower() != 'y':
        rounning = False
        
print(f'Thanks for playting, You score is {score} points.')
