from solution import mid_sum, direct_sort, is_update_valid, read_input


def test_mid_sum():
    updates = [
        [75,47,61,53,29],
        [97,61,53,29,13],
        [75,29,13]
    ]

    assert mid_sum(updates) == 143


def test_direct_sort():
    ord_rules, _ = read_input('test_input.txt')
    update = [75,97,47,61,53]
    assert is_update_valid(ord_rules, direct_sort(ord_rules, update)) == True
    update = [61,13,29]
    assert is_update_valid(ord_rules, direct_sort(ord_rules, update)) == True
    update = [97,13,75,29,47]
    assert is_update_valid(ord_rules, direct_sort(ord_rules, update)) == True
