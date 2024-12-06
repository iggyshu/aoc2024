from copy import deepcopy
from typing import List


def read_input(filename: str = "input.txt") -> List[List[str]]:
    tiles = []
    with open(filename) as f:
        lines = f.readlines()

        for line in lines:
            tiles.append(list(line.rstrip("\n")))

    return tiles


def print_tiles(tiles):
    for row in tiles:
        print(row)
    print()


def find_guard(tiles: List[List[str]]) -> (int, int):
    for i, row in enumerate(tiles):
        for j, tile in enumerate(row):
            if tile in ("^", ">", "<", "v"):
                return (i, j)


def move_guard(guard_pos: (int, int), tiles: List[List[str]]) -> List[List[str]]:
    row, col = guard_pos

    while True:
        guard = tiles[row][col]
        if guard == "^":
            if row - 1 < 0:
                tiles[row][col] = "X"
                break
            elif tiles[row - 1][col] == "#":
                tiles[row][col] = ">"
            else:
                tiles[row][col] = "X"
                tiles[row - 1][col] = guard
                row -= 1
        elif guard == ">":
            if col + 1 >= len(tiles[0]):
                tiles[row][col] = "X"
                break
            elif tiles[row][col + 1] == "#":
                tiles[row][col] = "v"
            else:
                tiles[row][col] = "X"
                tiles[row][col + 1] = guard
                col += 1
        elif guard == "<":
            if col - 1 < 0:
                tiles[row][col] = "X"
                break
            elif tiles[row][col - 1] == "#":
                tiles[row][col] = "^"
            else:
                tiles[row][col] = "X"
                tiles[row][col - 1] = guard
                col -= 1
        elif guard == "v":
            if row + 1 >= len(tiles):
                tiles[row][col] = "X"
                break
            elif tiles[row + 1][col] == "#":
                tiles[row][col] = "<"
            else:
                tiles[row][col] = "X"
                tiles[row + 1][col] = guard
                row += 1
        else:
            raise "Guard drunk?"

    return tiles


def time_paradox(guard_pos: (int, int), tiles: List[List[str]]) -> int:
    def move(
        guard_pos: (int, int), tiles: List[List[str]], obstacles: set()
    ) -> List[List[str]]:
        row, col = guard_pos
        # we now we are in a loop when we visit the same obstacle twice
        visited = obstacles

        while True:
            guard = tiles[row][col]
            if guard == "^":
                if row - 1 < 0:
                    return False
                elif tiles[row - 1][col] == "#":
                    obstacle = (row, col, row - 1, col)
                    if obstacle in visited:
                        return True
                    else:
                        visited.add(obstacle)
                    tiles[row][col] = ">"
                else:
                    tiles[row - 1][col] = guard
                    row -= 1
            elif guard == ">":
                if col + 1 >= len(tiles[0]):
                    return False
                elif tiles[row][col + 1] == "#":
                    obstacle = (row, col, row, col + 1)
                    if obstacle in visited:
                        return True
                    else:
                        visited.add(obstacle)
                    tiles[row][col] = "v"
                else:
                    tiles[row][col + 1] = guard
                    col += 1
            elif guard == "<":
                if col - 1 < 0:
                    return False
                elif tiles[row][col - 1] == "#":
                    obstacle = (row, col, row, col - 1)
                    if obstacle in visited:
                        return True
                    else:
                        visited.add(obstacle)
                    tiles[row][col] = "^"
                else:
                    tiles[row][col - 1] = guard
                    col -= 1
            elif guard == "v":
                if row + 1 >= len(tiles):
                    return False
                elif tiles[row + 1][col] == "#":
                    obstacle = (row, col, row + 1, col)
                    if obstacle in visited:
                        return True
                    else:
                        visited.add(obstacle)
                    tiles[row][col] = "<"
                else:
                    tiles[row + 1][col] = guard
                    row += 1
            else:
                raise "Guard drunk?"

    count = 0
    # there is a smarter way to do this:
    # we could use task one's output, to reduce the search space,
    # but I solved it and I want to sleep...
    for i, row in enumerate(tiles):
        for j, tile in enumerate(row):
            if tile == ".":
                tile_copy = deepcopy(tiles)
                tile_copy[i][j] = "#"
                print_tiles(tile_copy)
                stuck = move(guard_pos, tile_copy, set())
                if stuck:
                    count += 1

    return count


def count_moves(tiles):
    count = 0
    for row in tiles:
        for tile in row:
            if tile == "X":
                count += 1
    return count


def task_one(tiles):
    guard_pos = find_guard(tiles)
    tiles = move_guard(guard_pos, tiles)

    return count_moves(tiles)


def task_two(tiles):
    guard_pos = find_guard(tiles)
    times_stuck = time_paradox(guard_pos, tiles)
    return times_stuck


def main():
    tiles = read_input()
    tiles_two = deepcopy(tiles)
    result = task_one(tiles)
    print(f"Guard moves: {result}")
    result_two = task_two(tiles_two)
    print(f"Ways to get guard stuck: {result_two}")


if __name__ == "__main__":
    main()
