from solution import read_grid, print_grid, find_trailheads, trailhead_scores


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


def test_trailhead_scores():
    grid = read_grid("test_input.txt")
    trailheads = find_trailheads(grid)
    scores = trailhead_scores(grid, trailheads)
    print(scores)
    assert len(scores) == 9
    assert sorted(scores) == sorted([5, 6, 5, 3, 1, 3, 5, 3, 5])
    assert sum(scores) == 36
