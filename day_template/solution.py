
def read_input():
    with open('input.txt') as f:
        lines = f.readlines()

        return lines



def task_one(input):
    return 0


def task_two(input):
    return 0



def main():
    input = read_input()
    result = task_one(input)
    print(f': {result}')
    result = task_two(input)
    print(f': {result}')


if __name__ == "__main__":
    main()

