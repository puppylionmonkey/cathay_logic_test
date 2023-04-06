def number_logic(number):
    result = ''
    if number % 2 != 0:
        result = 'X'
    else:
        if 2 <= number <= 5:
            result = 'O'
        elif 6 <= number <= 20:
            result = 'X'
        elif number > 20:
            result = 'O'
    print(result)
    return result


def test_number_logic():
    assert number_logic(1) == 'X'
    assert number_logic(2) == 'O'
    assert number_logic(3) == 'X'
    assert number_logic(5) == 'X'
    assert number_logic(6) == 'X'
    assert number_logic(14) == 'X'
    assert number_logic(15) == 'X'
    assert number_logic(20) == 'X'
    assert number_logic(21) == 'X'
    assert number_logic(22) == 'O'
