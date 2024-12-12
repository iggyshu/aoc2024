from solution import read_grid, solution


def test_read_input():
    grid = read_grid("test_input.txt")

    assert len(grid) == 10
    assert len(grid[0]) == 10


def test_solution():
    grid = read_grid("test_input.txt")
    cost = solution(grid)
    assert cost == 1930
