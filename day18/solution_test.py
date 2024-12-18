from solution import Solution


def test_shortest_path():
    solution = Solution(filename="test_input.txt", size=7, simulate=12)
    solution.print_grid([])
    path = solution.shortest_path()
    solution.print_grid(path)
    assert len(path) - 1 == 22
