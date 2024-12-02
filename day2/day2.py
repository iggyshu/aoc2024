
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


def main():
    reports = read_input()
    total_safe = count_safe(reports)
    print(f'Number of safe reports: {total_safe}')


if __name__ == "__main__":
    main()

