from collections import defaultdict

def make_dicts(filename: str = 'input.txt') -> tuple[dict[int, int], dict[int, int]]:
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)

    with open(filename) as listfile:
        for line in listfile.read().splitlines():
            item1, item2 = line.split()

            dict1[int(item1)] += 1
            dict2[int(item2)] += 1

    return dict1, dict2


def total(filename: str = 'input.txt') -> int:
    similarity_score = 0

    dict1, dict2 = make_dicts(filename)
    for item in dict1:
        similarity_score += item * dict1[item] * dict2[item]

    return similarity_score


print(total('input.txt'))