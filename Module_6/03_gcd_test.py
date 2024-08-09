from math import ceil


def get_divisors(number: int) -> set:
    divisors = set()
    for test_divisor in range(2, ceil(number / 2) + 1):
        if number % test_divisor == 0:
            divisors.add(test_divisor)
    divisors.add(number)
    return divisors


def great_common_divisor(num1: int, num2: int) -> int:
    divisors1 = get_divisors(num1)
    divisors2 = get_divisors(num2)

    common_divisors = divisors1 & divisors2

    return max(common_divisors) if len(common_divisors) > 0 else None


def test_gcd_exists():
    assert great_common_divisor(20, 30) == 10
    assert great_common_divisor(15, 30) == 15


def test_gcd_doesnt_exist():
    assert great_common_divisor(7, 30) is None


def test_get_divisors():
    assert get_divisors(6) == {2, 3, 6}
