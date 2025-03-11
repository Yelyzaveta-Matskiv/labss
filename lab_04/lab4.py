def read_terminal_output(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def change_directory(path, current_path):
    if path == '/':
        return ['/']
    elif path == '..':
        return current_path[:-1]
    else:
        return current_path + [path]

def list_directory(content, file_system, current_path):
    for item in content:
        if item.startswith('dir'):
            file_system.setdefault(tuple(current_path), {})[item.split()[1]] = {}
        else:
            size, name = item.split()
            file_system.setdefault(tuple(current_path), {})[name] = int(size)

def calculate_size(directory):
    total_size = 0
    for value in directory.values():
        if isinstance(value, dict):
            total_size += calculate_size(value)
        else:
            total_size += value
    return total_size

def find_dirs_under_size(file_system, max_size):
    total_size = 0
    for dir_path, contents in file_system.items():
        size = calculate_size(contents)
        if size <= max_size:
            total_size += size
    return total_size

def main():
    file_system = {}
    current_path = ['/']
    terminal_output = read_terminal_output('input_4.txt')

    i = 0
    while i < len(terminal_output):
        line = terminal_output[i]
        if line.startswith('$ cd '):
            directory = line.split(' ')[2]
            current_path = change_directory(directory, current_path)
        elif line.startswith('$ ls'):
            i += 1
            content = []
            while i < len(terminal_output) and not terminal_output[i].startswith('$'):
                content.append(terminal_output[i])
                i += 1
            list_directory(content, file_system, current_path)
            continue
        i += 1

    total_size = find_dirs_under_size(file_system, 100000)
    print(f'Sum of total directory sizes that do not exceed 100,000: {total_size}')

if __name__ == '__main__':
    main()

# Sum = 1482845