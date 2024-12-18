from typing import List, Tuple
from collections import deque
from copy import deepcopy


class Solution:
    def __init__(
        self, filename: str = "input.txt", size: int = 71, simulate: int = 1024
    ) -> None:
        self._grid = []
        for _ in range(size):
            row = ["."] * size
            self._grid.append(row)

        with open(filename) as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if i == simulate:
                    break
                X, Y = [int(i) for i in line.rstrip("\n").split(",")]
                self._grid[Y][X] = "#"

    def print_grid(self, path: List[Tuple[int, int]]):
        grid = deepcopy(self._grid)

        if path is not None:
            for pos in path:
                Y, X = pos
                grid[Y][X] = "O"

        print()
        for row in grid:
            print("".join(row))
        print()

    def shortest_path(self) -> List[Tuple[int, int]]:
        def not_corrupt(pos: Tuple[int, int]) -> bool:
            Y, X = pos
            return self._grid[Y][X] != "#"

        def in_bounds(pos: Tuple[int, int]) -> bool:
            Y, X = pos
            return Y >= 0 and X >= 0 and Y < len(self._grid) and X < len(self._grid[0])

        frontier = deque([((0, 0), [])])
        visited = set()
        goal = (len(self._grid) - 1, len(self._grid[0]) - 1)

        while len(frontier) > 0:
            pos, path = frontier.popleft()
            print(f"pos: {pos}")

            path.append(pos)
            visited.add(pos)

            if pos == goal:
                return path

            Y, X = pos
            adjacent = [
                (Y, X - 1),
                (Y, X + 1),
                (Y - 1, X),
                (Y + 1, X),
            ]

            for adj in adjacent:
                if (
                    in_bounds(adj) and not_corrupt(adj) and adj not in visited
                    # and adj not in frontier
                ):
                    visited.add(adj)
                    frontier.append((adj, list(path)))

            print(f"frontier size: {len(frontier)}")
            # print(f"visited: {visited}")
            # print(f"frontier: {frontier}")
            print()

        raise Exception("Could not find any path to goal!")


def main():
    solution = Solution(filename="input.txt", size=71, simulate=1024)
    solution.print_grid([])
    path = solution.shortest_path()
    solution.print_grid(path)

    print("PATH:")
    print(path)
    print(f"Shortest path length: {len(path) - 1}")


if __name__ == "__main__":
    main()
