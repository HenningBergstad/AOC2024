def report_counter(filename: str = 'input.txt') -> int:
    safe_reports = 0
    with open(filename) as reports:
        for report in reports.read().splitlines():
            if safe_check(report):
                safe_reports += 1
    return safe_reports


def safe_check(report: str) -> bool:
    levels = [int(level) for level in report.split()]
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