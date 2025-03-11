def read_games(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def parse_sets(sets):
    game_sets = []
    for set_ in sets.strip().split(';'):
        game_set = {color: int(count) for count, color in [item.split() for item in set_.strip().split(', ')]}
        game_sets.append(game_set)
    return game_sets

def parse_game_data(lines):
    games = []
    for line in lines:
        game_id, sets = line.split(':')
        game_sets = parse_sets(sets)
        games.append((int(game_id.split()[1]), game_sets))
    return games

def game_possible(game, dices):
    for game_set in game:
        for color, count in game_set.items():
            if count > dices[color]:
                return False
    return True

def get_possible_games(games, dices):
    return [game_id for game_id, game_sets in games if game_possible(game_sets, dices)]

def main():
    lines = read_games('input_5.txt')
    games = parse_game_data(lines)
    dices = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = get_possible_games(games, dices)
    print("Possible games:", possible_games)
    print("Sum of indefigators of posssible games:", sum(possible_games))

if __name__ == "__main__":
    main()

# Possible games: [4, 8, 9, 17, 18, 20, 21, 23, 26, 27, 28, 29, 
# 31, 37, 41, 42, 45, 46, 47, 48, 50, 51, 53, 54, 57, 59, 60, 
# 63, 64, 66, 68, 69, 70, 75, 76, 77, 79, 80, 81, 84, 85, 87,
# 88, 89, 90, 91, 92, 94, 95, 96]

# Sum of indefigators of posssible games: 2810
