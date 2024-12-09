def find_muls(filename: str = 'input.txt') -> list[str]:
    with open(filename) as instructions:
        string = instructions.read()

    total = 0
    for i, char in enumerate(string):
        if char == 'm':
            if string[i + 1:i + 4] == 'ul(':
                y = i + 4
                first_number = '0'
                second_number = '0'
                while string[y].isnumeric():
                    first_number += string[y]
                    y += 1
                if string[y] != ',':
                    continue
                y += 1
                while string[y].isnumeric():
                    second_number += string[y]
                    y += 1
                if string[y] == ')':
                    total += int(first_number) * int(second_number)
    print(total)



find_muls()