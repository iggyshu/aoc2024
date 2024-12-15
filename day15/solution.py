from typing import List, Tuple


class Solution:
    def __init__(self, input_filename: str):
        grid, moves = self.read_input(input_filename)
        self._grid = grid
        self._moves = moves

    def read_input(self, filename: str) -> Tuple[List[List[str]], List[str]]:
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

    def find_robot(self):
        for y, row in enumerate(self._grid):
            for x, cell in enumerate(row):
                if cell == "@":
                    return y, x
        raise Exception("What happened to the robot!?")

    def get_adj_cell(self, coordinates, direction) -> Tuple[str, Tuple[int, int]]:
        y, x = coordinates
        match direction:
            case "<":
                return self._grid[y][x - 1], (y, x - 1)
            case ">":
                return self._grid[y][x + 1], (y, x + 1)
            case "^":
                return self._grid[y - 1][x], (y - 1, x)
            case "v":
                return self._grid[y + 1][x], (y + 1, x)
            case _:
                raise ValueError("Something is wrong with your direction!")

    def swap(self, coord, adj_coord):
        y, x = coord
        a_y, a_x = adj_coord
        self._grid[y][x], self._grid[a_y][a_x] = self._grid[a_y][a_x], self._grid[y][x]

    def move_box(self, box: Tuple[int, int], direction: str) -> bool:
        adj_value, adj_coord = self.get_adj_cell(box, direction)

        if adj_value == ".":
            # empty space
            self.swap(box, adj_coord)
            return True
        elif adj_value == "#":
            return False  # we hit a wall :)
        elif adj_value == "O":
            # another box
            if self.move_box(adj_coord, direction):
                self.swap(box, adj_coord)
                return True
            else:
                # the other box doesn't move
                return False
        else:
            raise ValueError("Something is wrong with adj cell!")

    def move_robot(self, robot: Tuple[int, int], direction: str):
        adj_value, adj_coord = self.get_adj_cell(robot, direction)

        if adj_value == ".":
            self.swap(robot, adj_coord)
            return adj_coord
        elif adj_value == "#":
            return robot
        elif adj_value == "O":
            if self.move_box(adj_coord, direction):
                self.swap(robot, adj_coord)
                return adj_coord
            else:
                return robot
        else:
            raise ValueError("Something is wrong with adj cell! - Robot")

    def get_box_coordinates(self):
        res = 0
        for y, row in enumerate(self._grid):
            for x, cell in enumerate(row):
                if cell == "O":
                    res += y * 100 + x
        return res


def main():
    solution = Solution(input_filename="input.txt")
    robot = solution.find_robot()
    for direction in solution._moves:
        robot = solution.move_robot(robot, direction)
    print(solution.get_box_coordinates())


if __name__ == "__main__":
    main()
