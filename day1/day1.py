def read_input():
    left, right = [], []
    with open('input.txt') as f:
        lines = f.readlines()

        for line in lines:
            parts = line.split('   ')
            left.append(int(parts[0]))
            right.append(int(parts[1]))
    return (left, right)


def calc_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()

    total_distance = 0

    for left_value, right_value in zip(left_list, right_list):
        total_distance += abs(left_value - right_value)

    return total_distance


print('Reading input.txt into two lists...')
left_list, right_list = read_input()

print('Calculating total distance between lists...')
total_distance = calc_total_distance(left_list, right_list)

print(f'Total distance between lists: {total_distance}')
