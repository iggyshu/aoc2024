from solution import Solution


def test_total_worth():
    sln = Solution(filename="test_input")
    res = sln.total_worth()
    assert res == 13
