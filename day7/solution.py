from typing import List


def read_input(filename: str = "input.txt") -> List:
    equations = []
    with open(filename) as f:
        lines = f.readlines()

        for line in lines:
            line.rstrip("\n")
            result = int(line.split(":")[0])
            operands = line.split(":")[1].split(" ")
            operands = [int(op) for op in operands if op.strip() != ""]
            equations.append((result, operands))

    return equations


def true_equation(equation: List) -> bool:
    result, operands = equation

    def test(curr_index: int, curr_res: int) -> bool:
        if curr_index >= len(operands) - 1:
            return curr_res == result
        else:
            nxt_index = curr_index + 1
            return test(nxt_index, curr_res * operands[nxt_index]) or test(
                nxt_index, curr_res + operands[nxt_index]
            )

    return test(0, operands[0])


def true_equation_with_concat(equation: List) -> bool:
    result, operands = equation

    def test(curr_index: int, curr_res: int) -> bool:
        if curr_index >= len(operands) - 1:
            return curr_res == result
        else:
            nxt_index = curr_index + 1
            return (
                test(nxt_index, curr_res * operands[nxt_index])
                or test(nxt_index, curr_res + operands[nxt_index])
                or test(nxt_index, int(f"{curr_res}{operands[nxt_index]}"))
            )

    return test(0, operands[0])


def sum_true_equations(equations: List, test_func) -> int:
    res = 0
    for eq in equations:
        if test_func(eq):
            res += eq[0]
    return res


def main():
    equations = read_input()
    result = sum_true_equations(equations, true_equation)
    result_with_concat = sum_true_equations(equations, true_equation_with_concat)
    print(f"Sum of true equations: {result}")
    print(f"Sum of true equations with concat: {result_with_concat}")


if __name__ == "__main__":
    main()
