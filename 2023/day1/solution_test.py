from solution import Solution

def test_sum_of_calibration_values():
    solution = Solution(filename="test_input")
    res = solution.sum_of_calibration_values()
    assert res == 142

def test_sum_of_calibration_values_with_digits():
    solution = Solution(filename="test_input_two")
    res = solution.sum_of_calibration_values_with_digits()
    assert res == 281
