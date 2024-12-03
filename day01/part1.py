def make_lists(filename: str) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []
    with open(filename) as listfile:
        for line in listfile.read().splitlines():
            item1, item2 = line.split()
            list1.append(int(item1))
            list2.append(int(item2))

    list1.sort()
    list2.sort()

    return list1, list2


def total(filename: str = 'input.txt') -> int:
    total_diff = 0
    list1, list2 = make_lists(filename)

    for item1, item2 in zip(list1, list2):
        total_diff += abs(item1 - item2)

    return total_diff

print(total())