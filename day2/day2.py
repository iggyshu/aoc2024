
def read_input():
    reports = []
    with open('input.txt') as f:
        lines = f.readlines()

        for line in lines:
            reports.append([int(x) for x in line.split(' ')])
    return reports


def is_safe(report):
    increasing = (report[0] - report[1]) < 0
    for i in range(len(report) - 1):
        curr = report[i]
        nxt = report[i + 1]

        if not all_inc_or_all_dec(curr, nxt, increasing) \
            or not at_least_one_and_at_most_three(curr, nxt):
            return False

    return True


def is_safe_with_dampener(report):
    increasing = (report[0] - report[1]) < 0
    safe = is_safe(report)

    if safe:
        return safe

    damped_reports = []
    for i in range(len(report)):
        damped_report = []
        for j, level in enumerate(report):
            if i != j:
                damped_report.append(level)
        damped_reports.append(damped_report)

    return any([is_safe(x) for x in damped_reports])


def all_inc_or_all_dec(curr, nxt, increasing):
    if increasing: 
        if curr > nxt:
            return False
    elif curr < nxt: # decreasing =)
        return False
    return True


def at_least_one_and_at_most_three(curr, nxt):
    diff = abs(curr - nxt)
    if diff < 1 or diff > 3:
        return False
    return True



def count_safe(reports):
    total_safe = 0
    for report in reports:
        if is_safe(report):
            total_safe += 1
    return total_safe


def count_safe_with_dampener(reports):
    total_safe = 0
    for report in reports:
        if is_safe_with_dampener(report):
            total_safe += 1
    return total_safe


def main():
    reports = read_input()
    total_safe = count_safe(reports)
    total_safe_with_dampener = count_safe_with_dampener(reports)
    print(f'Number of safe reports: {total_safe}')
    print(f'Number of safe reports with dampener: {total_safe_with_dampener}')


if __name__ == "__main__":
    main()

