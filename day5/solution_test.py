from solution import mid_sum, is_update_valid


def test_mid_sum():
    updates = [
        [75,47,61,53,29],
        [97,61,53,29,13],
        [75,29,13]
    ]

    assert mid_sum(updates) == 143



