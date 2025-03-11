def calibration_value(input_str):
    total = 0
    for char in input_str:
        if char.isdigit(): 
            total += int(char)  
    return total

def calculate_calibration_sum(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  
            total_sum += calibration_value(line)
    return total_sum

file_path = 'input_3.txt'
result = calculate_calibration_sum(file_path)
print(f"Total sum of all integers in the file: {result}")

# Total sum of all integers in the file: 11250