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

def main():
    sln = Solution()
    res = sln.sum_of_all_the_part_numbers()
    print(f"Sum of all engine part numbers: {res}")

if __name__ == "__main__":
    main()
