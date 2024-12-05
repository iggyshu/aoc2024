from collections import defaultdict


def read_input(filename='input.txt'):
    ordering_rules = defaultdict(set)
    updates = None
    with open(filename) as f:
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


def direct_sort(ord_rules, update):
    swaps = float('inf')
    while swaps != 0:
        swaps = 0
        i = 0
        while i < len(update) - 1:
            must_be_after = ord_rules[update[i+1]]
            if update[i] in must_be_after:
                swaps += 1
                update[i], update[i+1] = update[i+1], update[i]
            i += 1

    return update


def main():
    ord_rules, updates = read_input()

    valid_updates = []
    invalid_updates = []
    for upd in updates:
        if is_update_valid(ord_rules, upd):
            valid_updates.append(upd)
        else:
            invalid_updates.append(upd)

    mid_sum_of_valid = mid_sum(valid_updates)

    fixed_updates = [direct_sort(ord_rules, upd) for upd in invalid_updates]
    mid_sum_of_fixed = mid_sum(fixed_updates)

    print(f'Task one (mid sum of valid): {mid_sum_of_valid}')
    print(f'Task two (mid sum of fixed): {mid_sum_of_fixed}')


if __name__ == "__main__":
    main()

