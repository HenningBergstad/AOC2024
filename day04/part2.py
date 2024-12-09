def find_xmas(filename: str = 'input.txt') -> None:
    with open(filename) as filename:
        input = filename.read().splitlines()

    height = len(input)
    width = len(input[0])

    total_mas = 0

    for h in range(height-2):
        for w in range(width-2):
            word_1 = input[h][w]+input[h+1][w+1]+input[h+2][w+2]
            word_2 = input[h][w+2]+input[h+1][w+1]+input[h+2][w]
            if word_1 == 'MAS' or word_1 == 'SAM':
                if  word_2 == 'MAS' or word_2 == 'SAM':
                    print(f"Checking grid at ({h},{w}):")
                    print(f"{input[h][w:w + 3]}")
                    print(f"{input[h + 1][w:w + 3]}")
                    print(f"{input[h + 2][w:w + 3]}")
                    total_mas += 1
    print(total_mas)

find_xmas()