def is_increasing_or_decreasing(levels):
    for i in range(len(levels) - 1):
        if levels[i] >= levels[i + 1] or levels[i] <= levels[i + 1]:
            return True
    return False

def are_adjacent_levels_valid(levels):
    for i in range(len(levels) - 1):
        if not (1 <= abs(levels[i] - levels[i + 1]) <= 3):
            return False
    return True

def is_report_safe(levels):
    return is_increasing_or_decreasing(levels) and are_adjacent_levels_valid(levels)

def read_reports_from_file(file_path):
    with open(file_path, 'r') as file:
        data = [list(map(int, line.split())) for line in file]
    return data

file_path = 'input_2.txt'  
reports = read_reports_from_file(file_path)

for i, report in enumerate(reports):
    if is_report_safe(report):
        print(f"Report {i + 1} is safe.")
    else:
        print(f"Report {i + 1} is not safe.")


        
