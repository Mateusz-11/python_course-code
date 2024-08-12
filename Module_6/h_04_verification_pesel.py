def verify_pesel(pesel: str) -> bool:
    CONTROL = '13791379131'

    if len(pesel) != 11:
        return False

    control_sum = 0
    for pesel_char, control_char in zip(pesel, CONTROL):
        control_sum += int(pesel_char) * int(control_char)

    if control_sum % 10 != 0:
        return False

    return True


def test_pesel_in_valid():
    assert verify_pesel('82012974188')
    assert verify_pesel('06281074994')


def test_pesel_is_invalid():
    assert not verify_pesel('123456')
    # assert not verify_pesel('00012974188')
