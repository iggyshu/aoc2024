from typing import List, Tuple
from collections import deque


def read_grid(filename: str = "input.txt") -> List[List[str]]:
    grid = []
    with open(filename) as f:
        lines = f.readlines()
        grid = [list(line.rstrip("\n")) for line in lines]
    return grid


def print_grid(grid):
    for row in grid:
        print(row)


def find_trailheads(grid: List[List[str]]) -> List[Tuple[int, int]]:
    trailhead = "0"
    trailheads = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == trailhead:
                trailheads.append((i, j))
    return trailheads


def trailhead_score(grid: List[List[str]], trailhead: Tuple[int, int]) -> int:
    def in_bounds(node):
        row, col = node
        return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])

    def is_gradual(node, next_node):
        return int(grid[next_node[0]][next_node[1]]) - int(grid[node[0]][node[1]]) == 1

    def is_peak(node):
        return grid[node[0]][node[1]] == "9"

    visited = set()
    score = 0

    frontier = deque()
    frontier.append(trailhead)

    print("")
    print("beginning BFS")

    while frontier:
        print(frontier)
        node = frontier.popleft()
        visited.add(node)

        if is_peak(node):
            score += 1
        else:
            up = (node[0] - 1, node[1])
            left = (node[0], node[1] - 1)
            right = (node[0], node[1] + 1)
            down = (node[0] + 1, node[1])
            neighbor_nodes = [up, left, right, down]

            for neighbor in neighbor_nodes:
                if (
                    in_bounds(neighbor)
                    and (neighbor not in visited)
                    and is_gradual(node, neighbor)
                    and (neighbor not in frontier)
                ):
                    frontier.append(neighbor)

    print(f"trailhead: {trailhead}, score: {score}")
    return score


def trailhead_scores(
    grid: List[List[str]], trailheads: List[Tuple[int, int]]
) -> List[int]:
    return [trailhead_score(grid, trailhead) for trailhead in trailheads]


def main():
    grid = read_grid()
    trailheads = find_trailheads(grid)
    scores = trailhead_scores(grid, trailheads)
    print(sum(scores))


if __name__ == "__main__":
    main()
