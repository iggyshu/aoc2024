from typing import List, Tuple


class Solution:
    def __init__(self, filename: str = "input.txt"):
        self._grid = []
        self._deer = ()
        self._end = ()

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


def main():
    pass


if __name__ == "__main__":
    main()
