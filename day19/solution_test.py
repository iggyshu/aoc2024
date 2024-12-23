from solution import Solution


def test_valid_designs():
    solution = Solution(filename="test_input")
    valid_designs = solution.valid_designs()
    assert valid_designs == [
        "brwrr",
        "bggr",
        "gbbr",
        "rrbgbr",
        "bwurrg",
        "brgr",
    ]
