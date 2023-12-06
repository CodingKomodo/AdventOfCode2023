with open('Day2/input.txt') as file:
    all_games = []
    while True:
        line = file.readline()
        if not line:
            break
        game_and_val = line.split(':')
        trials = game_and_val[1].split(';')
        full_game = []
        for trial in trials:
            # [green, red, blue]
            one_round = [0,0,0]
            vals = trial.split(',')
            for val in vals:
                stuff = val.strip().split()
                if stuff[1] == 'green':
                    one_round[0] = int(stuff[0])
                if stuff[1] == 'red':
                    one_round[1] = int(stuff[0])
                if stuff[1] == 'blue':
                    one_round[2] = int(stuff[0])
            full_game.append(one_round)
        all_games.append(full_game)
game_powers = []
def find_power(full_game):
    min_vals = [0, 0, 0]
    for trial in full_game:
        if trial[0] > min_vals[0]:
            min_vals[0] = trial[0]
        if trial[1] > min_vals[1]:
            min_vals[1] = trial[1]
        if trial[2] > min_vals[2]:
            min_vals[2] = trial[2]
    return min_vals[0] * min_vals[1] * min_vals[2]
        

for game in all_games:
    game_powers.append(find_power(game))
        
        
print(sum(game_powers))