from simple_moving_average import simple_moving_average

def test_simple_moving_average():
    results = simple_moving_average([1] * 40)

    first = 0
    last = len(results) - 1
    twentieth = 19
    twentyfirst = 20

    # The first result should be 0
    assert results[first]['sma'] == 0

    # The twentieth result should be 0
    assert results[twentieth]['sma'] == 0

    # The twenty-first result should be 1
    assert results[twentyfirst]['sma'] == 1

    # The last results should be 1
    assert results[last]['sma'] == 1

    # The len of the results should be 40
    assert len(results) == 40