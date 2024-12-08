from typing import List
from collections import defaultdict


def read_grid(filename: str = "input.txt") -> List[List[str]]:
    grid = []
    with open(filename) as f:
        lines = f.readlines()
        grid = [list(line.rstrip("\n")) for line in lines]
    return grid


def print_grid(grid: List[List[str]]):
    for row in grid:
        print(row)


def in_bounds(grid: List[List[str]], node: (int, int)) -> bool:
    M, N = len(grid), len(grid[0])
    row, col = node

    return row >= 0 and row < M and col >= 0 and col < N


def count_antinodes(grid: List[List[str]]) -> int:
    nodes_by_value = defaultdict(list)  # {'a': [(0, 1), ('2, 4')]}
    antinodes = set()  # {(10, 11), (5, 6)}

    M, N = len(grid), len(grid[0])

    for row in range(M):
        for col in range(N):
            value = grid[row][col]
            if value == ".":
                continue  # this is not a node

            if value in nodes_by_value:
                # find antinode locations
                for node in nodes_by_value[value]:
                    row_1, col_1 = node
                    row_dist = abs(row_1 - row)
                    col_dist = abs(col_1 - col)
                    an_row_1, an_col_1 = row + row_dist, col + col_dist
                    an_row_2, an_col_2 = row_1 - row_dist, col_1 - col_dist
                    if col < col_1:
                        # edge case when current node is to the left
                        # of previously encountered node
                        an_col_1 = col - col_dist
                        an_col_2 = col_1 + col_dist
                    antinode_1 = (an_row_1, an_col_1)
                    antinode_2 = (an_row_2, an_col_2)

                    if in_bounds(grid, antinode_1):
                        antinodes.add(antinode_1)
                    if in_bounds(grid, antinode_2):
                        antinodes.add(antinode_2)

            nodes_by_value[value].append((row, col))

    return len(antinodes)


def main():
    grid = read_grid()
    count = count_antinodes(grid)
    print(f"Found {count} antinodes.")


if __name__ == "__main__":
    main()
