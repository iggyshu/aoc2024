from day2 import is_safe

def test_is_safe():
    safe = [7, 6, 4, 2, 1]
    assert is_safe(safe) == True

    unsafe = [1, 2, 7, 8, 9]
    assert is_safe(unsafe) == False

    unsafe = [9, 7, 6, 2, 1]
    assert is_safe(unsafe) == False

    unsafe = [1, 3, 2, 4, 5]
    assert is_safe(unsafe) == False

    unsafe = [8, 6, 4, 4, 1]
    assert is_safe(unsafe) == False

    safe = [1, 3, 6, 7, 9]
    assert is_safe(safe) == True
