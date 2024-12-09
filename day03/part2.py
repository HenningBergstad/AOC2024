def find_muls(filename: str = 'input.txt') -> list[str]:
    with open(filename) as instructions:
        string = instructions.read()

    total = 0
    enabled = True

    for i, char in enumerate(string):
        if enabled:
            if char == 'm':
                if string[i + 1:i + 4] == 'ul(':
                    y = i + 4
                    first_number = '0'
                    second_number = '0'
                    while string[y].isnumeric():
                        first_number += string[y]
                        y += 1
                    if string[y] == ',':
                        y += 1
                        while string[y].isnumeric():
                            second_number += string[y]
                            y += 1
                    if string[y] == ')':
                        total += int(first_number) * int(second_number)
            if char == 'd':
                if string[i + 1:i + 7] == 'on\'t()':
                    enabled = False
        else:
            if char == 'd':
                if string[i + 1:i + 4] == 'o()':
                    enabled = True

    print(total)

find_muls()