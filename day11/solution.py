from typing import List


def read_input(filename: str = "input.txt") -> List[int]:
    with open(filename) as f:
        lines = f.readlines()
        return [int(x) for x in lines[0].rstrip("\n").split(" ")]


def blink(stones: List[int], times: int) -> List[int]:
    S = list(stones)

    for i in range(times):
        new_stones = []
        for j in range(len(S)):
            if S[j] == 0:
                S[j] = 1
            elif len(str(S[j])) % 2 == 0:
                left = right = str(S[j])
                left = int(left[: len(left) // 2])
                right = int(right[len(right) // 2 :])
                S[j] = left
                new_stones.append(right)
            else:
                S[j] *= 2024
        for ns in new_stones:
            S.append(ns)

    return S


def main():
    stones = read_input()
    stones = blink(stones, 25)
    print(len(stones))


if __name__ == "__main__":
    main()
