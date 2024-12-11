from typing import List
from functools import cache


def read_input(filename: str = "input.txt") -> List[int]:
    with open(filename) as f:
        lines = f.readlines()
        return [int(x) for x in lines[0].rstrip("\n").split(" ")]


@cache
def process_stone(value: int) -> List[int]:
    if value == 0:
        return [1]
    elif len(str(value)) % 2 == 0:
        length = len(str(value))
        divisor = 10 ** (length // 2)
        left = value // divisor
        right = value % divisor
        return [left, right]
    else:
        return [value * 2024]


def blink(stones: List[int], times: int) -> List[int]:
    S = stones
    for i in range(times):
        print(f"blink: {i}, stones: {len(S)}")
        new_stones = []
        for value in S:
            new_stones.extend(process_stone(value))
        S = new_stones
    return S


def main():
    stones = read_input()
    stones = blink(stones, 25)
    print(len(stones))


if __name__ == "__main__":
    main()
