from operations import trampoline as tp


def test_factorial():
    assert tp.factorial(3) == 6

