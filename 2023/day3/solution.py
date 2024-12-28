from collections import deque
from typing import List, Tuple
from string import punctuation

class Solution():
    def __init__(self, filename: str = "input") -> None:
        self._grid = []
        self._symbols = set(list(punctuation))
        self._symbols.remove(".") # dot resembles blank space
        self._gears = [] # gear coordinates
        with open(filename) as f:
            for i, line in enumerate(f):
                self._grid.append(list(line.rstrip("\n")))
                for j, cell in enumerate(self._grid[-1]):
                    if cell == "*":
                        self._gears.append((i, j))

    def sum_of_all_the_part_numbers(self):
        engine_parts = []
        for i, row in enumerate(self._grid):
            j = 0
            while j < len(row):
                is_adjacent_to_symbol = False
                curr_part = []
                if row[j].isnumeric():
                    while j < len(row) and row[j].isnumeric():
                        curr_part.append(row[j])
                        is_adjacent_to_symbol = is_adjacent_to_symbol or self.is_adjacent(i, j)
                        j += 1
                if is_adjacent_to_symbol:
                    engine_parts.append(int("".join(curr_part)))
                j += 1
        print(f"Engine parts: {engine_parts}")
        return sum(engine_parts)

    def is_adjacent(self, y, x):
        nxt = [
            (y - 1, x - 1), # left up
            (y - 1, x), # up
            (y, x - 1), # left
            (y + 1 , x - 1), # left down
            (y + 1 , x + 1), # right down
            (y + 1, x), # down
            (y, x + 1), # right
            (y - 1, x + 1) # right up
        ]

        for adj in nxt:
            y, x = adj
            if y > 0 and x > 0 and y < len(self._grid) and x < len(self._grid[0]) \
               and self._grid[y][x] in self._symbols:
                return True
        return False

    def sum_of_gear_ratios(self):
        gear_ratios = []
        for gear in self._gears:
            Y, X = gear

            up = self.read_line((Y - 1, X))
            curr = self.read_line((Y, X))
            down = self.read_line((Y + 1, X))

            adj_numbers = up + curr + down

            print(f"Gear({gear}), adj numbers: {adj_numbers}")
            if len(adj_numbers) == 2:
                ratio = adj_numbers[0] * adj_numbers[1]
                gear_ratios.append(ratio)

        return sum(gear_ratios)

    def read_line(self, coordinates: Tuple[int, int]) -> List[int]:
        Y, X = coordinates
        if Y < 0 or Y > len(self._grid):
            return []

        numbers = []
        if self._grid[Y][X].isnumeric():
            numbers.append(self.read_number(coordinates))
        else:
            if X - 1 > 0 and self._grid[Y][X - 1].isnumeric():
                numbers.append(self.read_number((Y, X - 1)))
            if X + 1 < len(self._grid[0]) and self._grid[Y][X + 1].isnumeric():
                numbers.append(self.read_number((Y, X + 1)))
        return numbers

    def read_number(self, coordinates: Tuple[int, int]) -> int:
        Y, X = coordinates
        chars = deque([self._grid[Y][X]])
        left = X - 1
        while left >= 0 and self._grid[Y][left].isnumeric():
            chars.appendleft(self._grid[Y][left])
            left -= 1
        right = X + 1
        while right < len(self._grid[0]) and self._grid[Y][right].isnumeric():
            chars.append(self._grid[Y][right])
            right += 1
        return int("".join(chars))


def main():
    sln = Solution()
    part_numbers_sum = sln.sum_of_all_the_part_numbers()
    print(f"Part 1. Sum of all engine part numbers: {part_numbers_sum}")
    gear_ratios_sum = sln.sum_of_gear_ratios()
    print(f"Part 2. Sum of gear ratios: {gear_ratios_sum}")

if __name__ == "__main__":
    main()
