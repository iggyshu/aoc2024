from solution import Solution


def test_shortest_path():
    solution = Solution(filename="test_input.txt", size=7, simulate=12)
    solution.print_grid([])
    path = solution.shortest_path()
    solution.print_grid(path)
    assert len(path) - 1 == 22


def test_blocking_point():
    simulate = 25
    path = []
    while simulate > 0:
        print(f"simulate: {simulate}")
        try:
            solution = Solution(filename="test_input.txt", size=7, simulate=simulate)
            path = solution.shortest_path()
            break
        except:
            print("Failure!")
            simulate -= 1
    print(f"simulate: {simulate}")
    assert (simulate + 1) == 21
