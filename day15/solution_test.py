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


def test_move_robot():
    solution = Solution(input_filename="test_input.txt")
    robot = solution.find_robot()
    for direction in solution._moves:
        robot = solution.move_robot(robot, direction)

    res = []
    print()
    for row in solution._grid:
        joined = "".join(row)
        res.append(joined)
        print(joined)

    assert res == [
        "##########",
        "#.O.O.OOO#",
        "#........#",
        "#OO......#",
        "#OO@.....#",
        "#O#.....O#",
        "#O.....OO#",
        "#O.....OO#",
        "#OO....OO#",
        "##########",
    ]
