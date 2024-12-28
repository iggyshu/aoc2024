from collections import deque
from typing import Tuple, Union
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
                print(f"{self._grid[y][x]} is a symbol")
                return True
        return False

    def sum_of_gear_ratios(self):
        gear_ratios = []
        for gear in self._gears:
            y, x = gear
            left = (y, x - 1)
            right = (y, x + 1)
            down = (y + 1, x)
            up = (y - 1, x)
            up_left = (y - 1, x - 1)
            up_right = (y - 1, x + 1)
            down_left = (y + 1, x - 1)
            down_right = (y + 1, y + 1)
            adj_numbers = []

            left_number = self.read_number(left)
            if left_number is not None:
                adj_numbers.append(left_number)

            right_number = self.read_number(right)
            if right_number is not None:
                adj_numbers.append(right_number)

            down_number = self.read_number(down)
            up_number = self.read_number(up)

            if down_number is not None:
                adj_numbers.append(down_number)
            else:
                down_left_number = self.read_number(down_left)
                if down_left_number is not None:
                    adj_numbers.append(down_left_number)
                down_right_number = self.read_number(down_right)
                if down_right_number is not None:
                    adj_numbers.append(down_right_number)

            if up_number is not None:
                adj_numbers.append(up_number)
            else:
                up_left_number = self.read_number(up_left)
                if up_left_number is not None:
                    adj_numbers.append(up_left_number)
                up_right_number = self.read_number(up_right)
                if up_right_number is not None:
                    adj_numbers.append(up_right_number)

            print(f"gear ({gear}), adj numbers: {adj_numbers}")
            if len(adj_numbers) == 2:
                ratio = adj_numbers[0] * adj_numbers[1]
                gear_ratios.append(ratio)

        return sum(gear_ratios)

    def read_number(self, coordinates: Tuple[int, int]) -> Union[int, None]:
        Y, X = coordinates
        if (Y < 0 or Y > len(self._grid)) or (X < 0 or X > len(self._grid[0])):
            return None
        if not self._grid[Y][X].isnumeric():
            return None
        chars = deque([self._grid[Y][X]])
        left = X - 1
        while left >= 0 and self._grid[Y][left].isnumeric():
            chars.appendleft(self._grid[Y][left])
            left -= 1
        right = X + 1
        while right < len(self._grid[0]) and self._grid[Y][right].isnumeric():
            chars.append(self._grid[Y][right])
            right += 1
        print(f"chars: {''.join(chars)}")
        return int("".join(chars))


def main():
    sln = Solution()
    part_numbers_sum = sln.sum_of_all_the_part_numbers()
    print(f"Sum of all engine part numbers: {part_numbers_sum}")
    gear_ratios_sum = sln.sum_of_all_the_part_numbers()
    print(f"Sum of gear ratios: {gear_ratios_sum}")

if __name__ == "__main__":
    main()
