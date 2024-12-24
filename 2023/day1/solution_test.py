from solution import Solution

def test_sum_of_calibration_values():
    solution = Solution(filename="test_input")
    res = solution.sum_of_calibration_values()
    assert res == 142
