from collections import deque

def read_input():
    with open('input.txt') as f:
        lines = f.readlines()

        return [list(x) for x in lines]



def count_horizontal(input, search_term):
    def count_hor(input, search_term, reverse):
        count = 0
        for line in input:
            curr_line = line[::-1] if reverse else line
            buffer = deque()

            for char in curr_line:
                buffer.append(char)

                if len(buffer) > len(search_term):
                    buffer.popleft()

                if len(buffer) == len (search_term) \
                    and ''.join(buffer) == search_term:
                    count += 1

        return count
    return count_hor(input, search_term, reverse=True) \
            + count_hor(input, search_term, reverse=False)


def count_vertical(input, search_term):
    columns = []

    for col in range(len(input[0])):
        column = []
        for row in range(len(input)):
            column.append(input[row][col])
        columns.append(column)

    return count_horizontal(columns, search_term)


def count_diagonal(input, search_term):
    lines = []

    for column in range(len(input[0])):
        col = column
        row = 0
        line = []
        while col < len(input[0]) and row < len(input):
            line.append(input[row][col])
            col += 1
            row += 1
        lines.append(line)

    for rw in range(1, len(input)):
        row = rw
        col = 0
        line = []
        while row < len(input) and col < len(input[0]):
            line.append(input[row][col])
            col += 1
            row += 1
        lines.append(line)

    for rw in range(len(input)):
        row = rw
        col = 0
        line = []
        while col < len(input[0]) and row >= 0:
            line.append(input[row][col])
            col += 1
            row -= 1
        lines.append(line)

    for column in range(1, len(input[0])):
        row = len(input) - 1
        col = column
        line = []
        while col < len(input[0]) and row >= 0:
            line.append(input[row][col])
            col += 1
            row -= 1
        lines.append(line)

    return count_horizontal(lines, search_term)


def task_one(input):
    search_term = 'XMAS'
    result = count_horizontal(input, search_term)
    result += count_vertical(input, search_term)
    result += count_diagonal(input, search_term)
    return result 


def task_two(input):
    def test_str(S):
        test = 'MAS'
        return S == test or S[::-1] == test


    D = input
    count = 0
    for row in range(1, len(D) - 1):
        for col in range(1, len(D[0]) - 1):
            backslash = D[row-1][col-1] + D[row][col] + D[row+1][col+1] 
            fwdslash = D[row+1][col-1] + D[row][col] + D[row-1][col+1] 
            if test_str(backslash) and test_str(fwdslash):
                count += 1

    return count



def main():
    print('Day 4')
    input = read_input()
    result = task_one(input)
    print(f'XMAS count: {result}')
    result = task_two(input)
    print(f'X-MAS count: {result}')


if __name__ == "__main__":
    main()

