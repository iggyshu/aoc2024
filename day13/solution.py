import numpy as np
from typing import List


def parse_params(line: str) -> (int, int):
    right_side = line.split(": ")[-1]
    params = right_side.split(", ")
    return int(params[0].split("+")[-1]), int(params[1].split("+")[-1])


def parse_res(line: str) -> (int, int):
    right_side = line.split(": ")[-1]
    params = right_side.split(", ")
    return int(params[0].split("=")[-1]), int(params[1].split("=")[-1])


def read_equations(filename: str = "input.txt") -> List[List[str]]:
    equations = []

    with open(filename) as f:
        lines = f.readlines()
        for i in range(0, len(lines), 4):
            A_x, A_y = parse_params(lines[i])
            B_x, B_y = parse_params(lines[i + 1])
            X, Y = parse_res(lines[i + 2])
            equations.append(
                (
                    [[A_x, B_x], [A_y, B_y]],
                    [X, Y],
                )
            )

    return equations


def main():
    pass


if __name__ == "__main__":
    main()
