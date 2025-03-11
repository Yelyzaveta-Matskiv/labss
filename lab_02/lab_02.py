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

def count_safe_reports(reports):
    return sum(is_report_safe(report) for report in reports)

file_path = 'input_2.txt'  
reports = read_reports_from_file(file_path)
safe_reports_count = count_safe_reports(reports)

for i, report in enumerate(reports):
    safety_status = "is safe" if is_report_safe(report) else "is not safe"
    print(f"Report {i + 1} is {safety_status}.")

print(f'Total number of safe reports: {safe_reports_count}')

# Total number of safe reports: 261


        
