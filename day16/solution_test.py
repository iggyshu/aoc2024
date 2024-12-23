from solution import Solution


def test_ctor():
    solution = Solution(filename="test_input.txt")
    solution.print_grid()
    assert len(solution._grid) == 15
    assert len(solution._grid[0]) == 15
    assert solution._deer == (13, 1)
    assert solution._end == (1, 13)


def test_lowest_score():
    solution = Solution(filename="test_input.txt")
    score = solution.lowest_score()
    assert score == 7036
