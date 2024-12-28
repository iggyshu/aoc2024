from solution import Solution

def test_sum_of_all_part_numbers():
    sln = Solution(filename="test_input")
    res = sln.sum_of_all_the_part_numbers()
    assert res == 4361

def test_sum_of_gear_rations():
    sln = Solution(filename="test_input")
    res = sln.sum_of_gear_ratios()
    assert res == 467835
