from solution import read_equations


def test_read_input():
    equations = read_equations("test_input.txt")
    print(equations)
    assert (len(equations)) == 4
