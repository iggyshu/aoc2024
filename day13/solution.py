def parse_params(line: str) -> (int, int):
    right_side = line.split(": ")[-1]
    params = right_side.split(", ")
    return int(params[0].split("+")[-1]), int(params[1].split("+")[-1])


def parse_res(line: str) -> (int, int):
    right_side = line.split(": ")[-1]
    params = right_side.split(", ")
    return int(params[0].split("=")[-1]), int(params[1].split("=")[-1])


def read_equations(filename: str = "input.txt"):
    equations = []

    with open(filename) as f:
        lines = f.readlines()
        for i in range(0, len(lines), 4):
            A_x, A_y = parse_params(lines[i])
            B_x, B_y = parse_params(lines[i + 1])
            X, Y = parse_res(lines[i + 2])
            equations.append(
                (
                    [[A_x, B_x], [A_y, B_y]],
                    [X, Y],
                )
            )

    return equations


def solve_equation_brut(equation):
    X = equation[1][0]
    Y = equation[1][1]
    A1 = equation[0][0][0]
    A2 = equation[0][1][0]
    B1 = equation[0][0][1]
    B2 = equation[0][1][1]

    can_solve = False
    sol = ()

    for i in range(100):
        for j in range(100):
            if A1 * i + B1 * j == X and A2 * i + B2 * j == Y:
                can_solve = True
                sol = (i, j)
                break

    return can_solve, sol


def solution(filename="input.txt"):
    equations = read_equations(filename)

    res = 0

    for equation in equations:
        can_solve, sol = solve_equation_brut(equation)
        if can_solve:
            A, B = sol

            cost = A * 3 + B
            res += cost

    return res


def main():
    print(solution())


if __name__ == "__main__":
    main()
