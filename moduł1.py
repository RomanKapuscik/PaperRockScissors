
results = {'paper': {'paper': 1, 'scissors': 0, 'rock': 0},
          'scissors': {'paper': 1, 'scissors': 0, 'rock': 0},
          'rock': {'paper': 0, 'scissors': 0, 'rock': 0}}



def calculate_number_of_games(results: dict) -> int:
    num = 0
    for keys in results:
        for key in results[keys]:
            num += results[keys][key]
    return num


print(calculate_number_of_games(results))
