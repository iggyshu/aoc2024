from solution import read_grid, print_grid, count_antinodes, with_resonant_harmonics


def test_read_input():
    grid = read_grid("test_input.txt")
    print_grid(grid)

    assert len(grid) == 12
    assert len(grid[0]) == 12


def test_count_antinodes():
    grid = read_grid("test_input.txt")
    count = count_antinodes(grid)
    assert count == 14


def test_with_resonant_harmonics():
    grid = read_grid("test_input.txt")
    count = with_resonant_harmonics(grid)
    assert count == 34
