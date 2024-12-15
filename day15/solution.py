from typing import List, Tuple


def read_input(filename: str) -> Tuple[List[List[str]], List[str]]:
    grid = []
    moves = []
    with open(filename) as f:
        lines = f.readlines()

        i = 0
        while lines[i].rstrip("\n") != "":
            grid.append(list(lines[i].rstrip("\n")))
            i += 1

        i += 1

        commands = ""
        for j in range(i, len(lines)):
            commands += lines[j].rstrip("\n")
        moves = list(commands)

    return grid, moves


def find_robot(grid: List[List[str]]):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "@":
                return y, x
    raise Exception("What happened to the robot!?")


def main():
    pass


if __name__ == "__main__":
    main()
