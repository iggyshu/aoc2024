from day3 import process, conditional_process

def test_process():
    input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

    result = process(input)
    assert result == 161


def test_conditional_process():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    result = conditional_process(input)
    assert result == 48
