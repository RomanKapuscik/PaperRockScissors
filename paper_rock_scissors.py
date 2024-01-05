import random
import json

options = ('paper', 'rock', 'scissors')

answer_to_win = {'paper': 'scissors',
                 'rock':'paper',
                 'scissors':'rock'}

#Players choices loaded form file
with open('results.json') as f:
    results = json.load(f)

rounning = True
score = 0
number_of_games = 0
min_number_of_games = 10 #befor riching minimum number of games app will chose answers randomly
last1, last2 = '', ''


def game_result(player: str, computer: str) -> int:
    if player == computer:
        return 0, 'tide'
    elif answer_to_win[player] == computer:
        return -1, 'lose'
    else:
        return 1, 'win'
    
def select_answer(player_answer: str) -> str:
    disp_results = results[player_answer]
    return max(disp_results, key=disp_results.get)

def calculate_number_of_games(results: dict) -> int:
    num = 0
    for keys in results:
        for key in results[keys]:
            num += results[keys][key]
    return num

while rounning:
    player = None
    
    while player not in options:
        player = input('Enter Your choice (paper, rock, scissors): ').lower()
        
    if calculate_number_of_games(results) < min_number_of_games:
        computer = random.choice(options)
    else:
        computer = answer_to_win[select_answer(player)]
    
    print(f'Players choice: {player}')
    print(f'Computers choice: {computer}')
    
    result = game_result(player, computer)
    print(f'You {result[1]}!')
    score += result[0]
    number_of_games += 1
    
    #Update choices of the player
    last1, last2 = player, last1
    if number_of_games > 1:
        results[last2][last1] += 1
    
    if input('Do You want to play again? (y/n)').lower() == 'n':
        rounning = False
        
print(f'Thanks for playting, You score is {score} points.')

#Save results to file
json_object = json.dumps(results, indent=4)

with open('results.json', 'w') as outfile:
    outfile.write(json_object)
