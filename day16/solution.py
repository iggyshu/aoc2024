from typing import List, Tuple
from collections import deque


class Solution:
    def __init__(self, filename: str = "input.txt"):
        self._grid = []
        self._deer = (0, 0)
        self._end = (0, 0)

        with open(filename) as f:
            lines = f.readlines()

            for line in lines:
                self._grid.append(list(line.rstrip("\n")))

        for y, row in enumerate(self._grid):
            for x, cell in enumerate(row):
                if cell == "S":
                    self._deer = (y, x)
                elif cell == "E":
                    self._end = (y, x)

    def print_grid(self):
        print()
        for row in self._grid:
            print("".join(row))

    def lowest_score(self) -> int:
        def is_wall(pos):
            y, x = pos
            return self._grid[y][x] == "#"

        def is_end(pos):
            return pos == self._end

        def keep_score(path):
            if len(path) < 3:
                return 1
            y, x = path[-3]
            y_c, x_c = path[-1]

            if abs(y_c - y) == 1 and abs(x_c - x) == 1:
                return 1001  # this is a turn
            else:
                return 1

        def search(pos, path, score) -> int:
            score += keep_score(path)

            if is_end(pos):
                print("REACHED END")
                print(path)
                print(score)
                return score
            else:
                y, x = pos
                left = (y, x - 1)
                right = (y, x + 1)
                up = (y - 1, x)
                down = (y + 1, x)

                scores = [float("inf")]

                for dir in [left, right, up, down]:
                    if not is_wall(dir) and dir not in path:
                        scores.append(search(dir, path + [dir], score))

                return min(scores)

        return search(self._deer, [(self._deer[0], self._deer[1] - 1), self._deer], -1)


def main():
    solution = Solution(filename="input.txt")
    print(solution.lowest_score())


if __name__ == "__main__":
    main()
