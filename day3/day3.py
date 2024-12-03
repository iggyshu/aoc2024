import re

def read_input():
    with open('input.txt') as f:
        lines = f.readlines()

        # Example:
        # xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
        return ''.join(lines)


def mul(num1, num2):
    return num1 * num2 # call it cheating :D


def process(input):
    pattern = re.compile(r"mul\(\d+,\d+\)")
    matches = pattern.findall(input)

    result = 0
    for match in matches:
        result += eval(match)

    return result


def conditional_process(input):
    result = 0

    # partition input into 'do()' blocks first:
    parts = input.split('do()')

    for part in parts:
        # then split each part,
        # to ignore everything to the right of 'don't()' keyword:
        only_good_stuff = part.split("don't()")[0]
        result += process(only_good_stuff)

    return result


def main():
    input = read_input()
    result = process(input)
    result_with_conditions = conditional_process(input)
    print(f'Result: {result}')
    print(f'Result with extra conditions: {result_with_conditions}')


if __name__ == "__main__":
    main()

