from solution import Solution

def test_sum_valid_game_ids():
    sln = Solution(filename="test_input")
    act_sum = sln.sum_valid_game_ids()
    assert act_sum == 8

def test_sum_of_game_powers():
    sln = Solution(filename="test_input")
    act_sum = sln.sum_of_game_powers()
    assert act_sum == 2286
