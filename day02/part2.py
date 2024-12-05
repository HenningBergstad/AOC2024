def report_counter(filename: str = 'input.txt') -> int:
    safe_reports = 0
    with open(filename) as reports:
        for report in reports.read().splitlines():
            levels = [int(level) for level in report.split()]
            if safe_check(levels) or dampen_check(levels):
                safe_reports += 1
    return safe_reports


def safe_check(levels: list) -> bool:
    if len(levels) <= 1:
        return True

    if levels[0] == levels[1]:
        return False

    increasing = levels[0] < levels[1]

    for i in range(len(levels)-1):
        a = levels[i]
        b = levels[i+1]
        if increasing:
            if a >= b:
                return False
        else:
            if a <= b:
                return False
        if abs(a - b) > 3:
            return False

    return True

def dampen_check(levels: list) -> bool:
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1:]
        if safe_check(new_levels):
            return True
    return False

print(report_counter())