from solution import read_input, blink


def test_read_input():
    stones = read_input("test_input.txt")
    print(stones)
    assert stones == [125, 17]


def test_blink():
    stones = read_input("test_input.txt")
    stones = blink(stones, 6)
    assert (len(stones)) == 22
