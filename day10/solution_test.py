from solution import read_grid, print_grid, find_trailheads


def test_read_input():
    grid = read_grid("test_input.txt")
    print_grid(grid)

    assert len(grid) == 8
    assert len(grid[0]) == 8


def test_find_trailheads():
    grid = read_grid("test_input.txt")

    trailheads = find_trailheads(grid)
    print(trailheads)
    assert len(trailheads) == 9
