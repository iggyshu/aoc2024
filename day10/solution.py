from typing import List, Tuple
from collections import defaultdict


def read_grid(filename: str = "input.txt") -> List[List[str]]:
    grid = []
    with open(filename) as f:
        lines = f.readlines()
        grid = [list(line.rstrip("\n")) for line in lines]
    return grid


def print_grid(grid):
    for row in grid:
        print(row)


def find_trailheads(grid: List[List[str]]) -> List[Tuple[int, int]]:
    trailhead = "0"
    trailheads = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == trailhead:
                trailheads.append((i, j))
    return trailheads


def main():
    grid = read_grid()


if __name__ == "__main__":
    main()
