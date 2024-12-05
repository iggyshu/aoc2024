from collections import defaultdict


def read_input():
    ordering_rules = defaultdict(set)
    updates = None
    with open('input.txt') as f:
        lines = f.readlines()

        i = 0
        while lines[i].strip() != '':
            key, value = lines[i].split('|')
            ordering_rules[int(key)].add(int(value))
            i += 1

        updates = lines[i+1:]
    
    for i, upd in enumerate(updates):
        updates[i] = [int(x) for x in upd.split(',')]

    return (ordering_rules, updates)


def is_update_valid(ord_rules, update):
    previous = []
    for page in update:
        if page not in ord_rules:
            # Maybe there are pages without rules,
            # who knows those elves
            continue
        must_be_after = ord_rules[page]
        for prev_page in previous:
            if prev_page in must_be_after:
                # rule violated, so update is invalid
                return False
        previous.append(page)
    return True


def mid_sum(updates):
    mid_sum = 0
    for upd in updates:
        mid_sum += upd[len(upd) // 2]
    return mid_sum



def task_one(ord_rules, updates):
    valid_updates = [ update for update in updates if is_update_valid(ord_rules, update)]
    return mid_sum(valid_updates)

def task_two(input):
    return 0


def main():
    ord_rules, updates = read_input()

    res = task_one(ord_rules, updates)
    print(f'Task one: {res}')
    # res = task_two(data)
    # print(f'Task two: {res}')


if __name__ == "__main__":
    main()

