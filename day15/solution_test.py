from solution import find_robot, read_input


def test_read_input():
    grid, moves = read_input(filename="test_input.txt")

    assert len(grid) == 10
    assert len(grid[0]) == 10
    assert len(moves) == 700


def test_find_robot():
    grid, _ = read_input(filename="test_input.txt")
    y, x = find_robot(grid)
    assert y == 4 and x == 4
