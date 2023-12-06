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
real_game = [13, 12, 14]
valid_games = []
def check_game(real_game, full_game):
    for trial in full_game:
        if trial[0] > real_game[0] or trial[1] > real_game[1] or trial[2] > real_game[2]:
            return False
    return True

for index, game in enumerate(all_games):
    if check_game(real_game, game):
        valid_games.append(index + 1)
        
        
        
print(sum(valid_games))