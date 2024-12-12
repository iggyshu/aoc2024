from typing import List


def read_grid(filename: str = "input.txt") -> List[List[str]]:
    grid = []
    with open(filename) as f:
        lines = f.readlines()
        grid = [list(line.rstrip("\n")) for line in lines]
    return grid


def solution(grid: List[List[str]]) -> int:
    def in_bounds(cell):
        row, col = cell
        return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])

    def same_plants(cell, other):
        return grid[cell[0]][cell[1]] == grid[other[0]][other[1]]

    visited = set()

    def explore(cell, area, perimeter):
        visited.add(cell)
        area += 1
        row, col = cell
        up = (row - 1, col)
        left = (row, col - 1)
        right = (row, col + 1)
        down = (row + 1, col)
        neighbor_cells = [up, down, left, right]

        for nb_cell in neighbor_cells:
            if not in_bounds(nb_cell):
                perimeter += 1
            elif not same_plants(cell, nb_cell):
                perimeter += 1
            elif nb_cell not in visited:
                area, perimeter = explore(nb_cell, area, perimeter)

        return (area, perimeter)

    regions = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in visited:
                continue
            regions.append(((row, col), explore((row, col), 0, 0)))

    for i, region in enumerate(regions):
        cell = region[0]
        area, perimeter = region[1]
        print(
            f"{i} ({cell[0]}, {cell[1]}) region: {grid[cell[0]][cell[1]]}, perimeter: {perimeter}, area: {area}"
        )
    cost = sum([x[1][0] * x[1][1] for x in regions])

    return cost


def main():
    grid = read_grid()
    cost = solution(grid)
    print(f"Cost: {cost}")


if __name__ == "__main__":
    main()
