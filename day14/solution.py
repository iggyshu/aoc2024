from typing import List, Tuple


class Robot:
    def __init__(
        self, pos: Tuple[int, int], vel: Tuple[int, int], gridsize: Tuple[int, int]
    ):
        self.x, self.y = pos
        self.vel_x, self.vel_y = vel
        self.grid_x, self.grid_y = gridsize

    def __str__(self):
        return f"Robot: p={self.x},{self.y} v={self.vel_x},{self.vel_y}"

    def move(self, times: int):
        for _ in range(times):
            self.x += self.vel_x
            self.y += self.vel_y
            if self.x >= self.grid_x:
                self.x -= self.grid_x
            elif self.x < 0:
                self.x += self.grid_x
            if self.y >= self.grid_y:
                self.y -= self.grid_y
            elif self.y < 0:
                self.y += self.grid_y

    def is_in_quadrant(
        self, quadrant_start: Tuple[int, int], quadrant_end: Tuple[int, int]
    ) -> bool:
        X_s, Y_s = quadrant_start
        X_e, Y_e = quadrant_end
        return (X_s <= self.x <= X_e) and (Y_s <= self.y <= Y_e)


def read_robots(gridsize: Tuple[int, int], filename: str = "input.txt") -> List[Robot]:
    robots = []

    with open(filename) as f:
        lines = f.readlines()

        for line in lines:
            parts = line.rstrip("\n").split(" ")
            pos = map(int, parts[0].lstrip("p=").split(","))
            vel = map(int, parts[1].lstrip("v=").split(","))
            robots.append(Robot(pos, vel, gridsize))

    return robots


def print_grid(robots, X, Y):
    print("==================================")
    for i in range(Y):
        counts = []
        for j in range(X):
            count = 0
            for robot in robots:
                if robot.x == j and robot.y == i:
                    count += 1
            counts.append(str(count))
            if counts[-1] == "0":
                counts[-1] = "."
        print(" ".join(counts))
    print("==================================")


def safety_rating(robots: List[Robot], gridsize: Tuple[int, int], seconds: int):
    X, Y = gridsize

    up_left = (0, 0), (X // 2 - 1, Y // 2 - 1)
    up_right = (X // 2 + 1, 0), (X - 1, Y // 2 - 1)
    down_left = (0, Y // 2 + 1), (X // 2 - 4, Y - 1)
    down_right = (X // 2 + 1, Y // 2 + 1), (X - 1, Y - 1)
    quadrants = [up_left, up_right, down_left, down_right]

    print_grid(robots, X, Y)
    for _ in range(seconds):
        for robot in robots:
            robot.move(1)
        print_grid(robots, X, Y)

    print()
    print("Quadrants:")
    for q in quadrants:
        print(q)

    for robot in robots:
        print(robot)

    robots_quadrants = []
    for q in quadrants:
        res = 0
        for robot in robots:
            if robot.is_in_quadrant(q[0], q[1]):
                res += 1
        robots_quadrants.append(res)

    print("Robots in quadrants:")
    print(robots_quadrants)

    rating = sum(robots_quadrants)
    print(f"Safety rating: {rating}")
    return rating


def main():
    pass


if __name__ == "__main__":
    main()
