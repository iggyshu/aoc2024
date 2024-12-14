from solution import read_robots, safety_rating


def test_read_robots():
    robots = read_robots((11, 7), "test_input.txt")
    for robot in robots:
        print(robot)
    assert len(robots) == 12


def test_safety_rating_one_robot():
    gridsize = (11, 7)
    robots = read_robots(gridsize, "test_small_input.txt")
    rating = safety_rating(robots, gridsize, 5)
    assert rating == 0


def test_safety_rating():
    gridsize = (11, 7)
    robots = read_robots(gridsize, "test_input.txt")
    rating = safety_rating(robots, gridsize, 100)
    assert rating == 0
