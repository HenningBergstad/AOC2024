def find_xmas(filename: str = 'input.txt') -> None:
    with open(filename) as filename:
        input = filename.read().splitlines()

    height = len(input)
    width = len(input[0])

    total_xmas = 0

    # Horizontal search
    for line in input:
        for i, character in enumerate(line):
            if line[i:i+4] == 'XMAS':
                total_xmas += 1
            elif line[i:i+4] == 'SAMX':
                total_xmas += 1

    # Vertical search
    for w in range(width):
        for h in range(height-3):
            word = input[h][w] + input[h+1][w] + input[h+2][w] + input[h+3][w]
            if word == 'XMAS' or word == "SAMX":
                total_xmas += 1

    # Diagonal search 1
    for w in range(width-3):
        for h in range(height-3):
            word = input[h+3][w] + input[h+2][w+1] + input[h+1][w+2] + input[h][w+3]
            if word == 'XMAS' or word == 'SAMX':
                total_xmas += 1

    # Diagonal search 2
    for w in range(width-3):
        for h in range(height-3):
            word = input[h][w] + input[h+1][w+1] + input[h+2][w+2] + input[h+3][w+3]
            if word == 'XMAS' or word == 'SAMX':
                total_xmas += 1

    print(total_xmas)

find_xmas()