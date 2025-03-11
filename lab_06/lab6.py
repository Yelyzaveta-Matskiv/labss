def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def count_points(move):
    points = 0
    if move == 'X':  
        points += 1
    elif move == 'Y': 
        points += 2
    elif move == 'Z':  
        points += 3
    return points

def count_result(opponent, your_move):
    if (opponent == 'A' and your_move == 'Y') or (opponent == 'B' and your_move == 'Z') or (opponent == 'C' and your_move == 'X'):
        return 6 
    elif (opponent == 'A' and your_move == 'X') or (opponent == 'B' and your_move == 'Y') or (opponent == 'C' and your_move == 'Z'):
        return 3  
    else:
        return 0 

def calculate_total_points(file_path):
    lines = read_file(file_path)
    total_points = 0
    for line in lines:
        opponent, your_move = line.split()
        total_points += count_points(your_move)
        total_points += count_result(opponent, your_move)
    return total_points

total_score = calculate_total_points('input_6.txt')
print("Total amount of points:", total_score)

# Total amount of points: 8933
