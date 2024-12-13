from solution import read_equations, solution, solve_equation_brut


def test_read_input():
    equations = read_equations("test_input.txt")
    print(equations)
    assert (len(equations)) == 4


def test_solve_equation():
    equations = read_equations("test_input.txt")
    can_solve, sol = solve_equation_brut(equations[0])
    assert can_solve
    print(sol)
    assert tuple(sol) == (80, 40)

    can_solve, sol = solve_equation_brut(equations[1])
    assert not can_solve
    can_solve, sol = solve_equation_brut(equations[3])
    assert not can_solve

    can_solve, sol = solve_equation_brut(equations[2])
    assert can_solve
    assert tuple(sol) == (38, 86)


def test_solution():
    res = solution("test_input.txt")
    assert res == 480
