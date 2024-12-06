from solution import read_input, find_guard, move_guard, count_moves, time_paradox


def test_find_guard():
    tiles = read_input("test_input.txt")

    row, col = find_guard(tiles)

    assert (row, col) == (6, 4)


def test_move_guard():
    tiles = read_input("test_input.txt")
    tiles_with_guard_moves = read_input("test_input_with_moves.txt")

    guard_pos = (6, 4)
    tiles_with_moves = move_guard(guard_pos, tiles)
    assert tiles_with_moves == tiles_with_guard_moves


def test_count_moves():
    tiles_with_guard_moves = read_input("test_input_with_moves.txt")
    assert count_moves(tiles_with_guard_moves) == 41


def test_time_paradox():
    tiles = read_input("test_input.txt")
    guard_pos = (6, 4)
    times_stuck = time_paradox(guard_pos, tiles)
    assert times_stuck == 6
