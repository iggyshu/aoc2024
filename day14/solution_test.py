from solution import read_robots


def test_read_robots():
    robots = read_robots((11, 7), "test_input.txt")
    for robot in robots:
        print(robot)
    assert len(robots) == 12
