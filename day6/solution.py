from typing import List


def read_input(filename: str = "input.txt") -> List[List[str]]:
    tiles = []
    with open(filename) as f:
        lines = f.readlines()

        for line in lines:
            tiles.append(list(line.rstrip("\n")))

    return tiles


def find_guard(tiles: List[List[str]]) -> (int, int):
    for i, row in enumerate(tiles):
        for j, tile in enumerate(row):
            if tile in ("^", ">", "<", "v"):
                return (i, j)


def move_guard(guard_pos: (int, int), tiles: List[List[str]]) -> List[List[str]]:
    row, col = guard_pos

    while True:
        print(row, col)
        guard = tiles[row][col]
        if guard == "^":
            if row - 1 < 0:
                print("exiting")
                tiles[row][col] = "X"
                break
            elif tiles[row - 1][col] == "#":
                print("turn right")
                tiles[row][col] = ">"
            else:
                print("move up")
                tiles[row][col] = "X"
                tiles[row - 1][col] = guard
                row -= 1
        elif guard == ">":
            if col + 1 >= len(tiles[0]):
                print("exiting")
                tiles[row][col] = "X"
                break
            elif tiles[row][col + 1] == "#":
                print("turn down")
                tiles[row][col] = "v"
            else:
                print("move right")
                tiles[row][col] = "X"
                tiles[row][col + 1] = guard
                col += 1
        elif guard == "<":
            if col - 1 < 0:
                print("exiting")
                tiles[row][col] = "X"
                break
            elif tiles[row][col - 1] == "#":
                print("turn up")
                tiles[row][col] = "^"
            else:
                print("move left")
                tiles[row][col] = "X"
                tiles[row][col - 1] = guard
                col -= 1
        elif guard == "v":
            if row + 1 >= len(tiles):
                print("exiting")
                tiles[row][col] = "X"
                break
            elif tiles[row + 1][col] == "#":
                print("turn left")
                tiles[row][col] = "<"
            else:
                print("move down")
                tiles[row][col] = "X"
                tiles[row + 1][col] = guard
                row += 1
        else:
            raise "Guard drunk?"

        for r in tiles:
            print(r)
        print()

    return tiles


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


def main():
    tiles = read_input()
    result = task_one(tiles)
    print(f"Guard moves: {result}")
    # result = task_two(input)
    # print(f': {result}')


if __name__ == "__main__":
    main()
