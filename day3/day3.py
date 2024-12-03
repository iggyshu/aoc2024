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


def main():
    input = read_input()
    result = process(input)
    print(f'Result: {result}')


if __name__ == "__main__":
    main()

