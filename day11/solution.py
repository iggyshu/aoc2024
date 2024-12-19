from typing import List
from functools import cache
from collections import defaultdict


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


def blink(stones: List[int], times: int) -> int:
    prev = {}

    for stone in stones:
        prev[stone] = 1

    curr = prev

    for _ in range(times):
        prev = defaultdict(int)
        for stone, count in curr.items():
            transition = process_stone(stone)
            for T in transition:
                prev[T] += count
        curr = prev

    return sum(curr.values())


def main():
    res = 0
    stones = read_input()
    res = blink(stones, 75)
    print(res)


if __name__ == "__main__":
    main()
