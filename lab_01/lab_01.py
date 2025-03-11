def remove_duplicates(a, b):
    a = list(set(a))
    b = list(set(b))
    return a, b

def calculate_total_distance(a, b):
    a, b = remove_duplicates(a, b)
    a.sort()
    b.sort()
    total_distance = 0
    for i in range(min(len(a), len(b))):
        total_distance += abs(a[i] - b[i])
    return total_distance

def read_lists_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    left_list = [int(x) for x in lines[0].split()]
    right_list = [int(x) for x in lines[1].split()]
    return left_list, right_list

file_path = 'input_1.txt'
left_list, right_list = read_lists_from_file(file_path)
print("Total distance:", calculate_total_distance(left_list, right_list))

# result = 64475
