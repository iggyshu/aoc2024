from solution import read_input, true_equation


def test_read_input():
    lines = read_input("test_input.txt")
    assert len(lines) == 9


def test_true_equation():
    equations = read_input("test_input.txt")
    true_equations = []
    for eq in equations:
        if true_equation(eq):
            true_equations.append(eq)

    assert len(true_equations) == 3
