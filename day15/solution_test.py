from solution import Solution


def test_read_input():
    solution = Solution(input_filename="test_input.txt")

    assert len(solution._grid) == 10
    assert len(solution._grid[0]) == 10
    assert len(solution._moves) == 700


def test_find_robot():
    solution = Solution(input_filename="test_input.txt")

    y, x = solution.find_robot()
    assert y == 4 and x == 4
