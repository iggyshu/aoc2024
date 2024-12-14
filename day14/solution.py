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
                self.x = 0
            elif self.x < 0:
                self.x = self.grid_x - 1
            if self.y >= self.grid_y:
                self.y = 0
            elif self.y < 0:
                self.y = self.grid_y - 1

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


def main():
    pass


if __name__ == "__main__":
    main()
