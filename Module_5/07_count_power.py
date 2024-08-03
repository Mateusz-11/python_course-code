def power(number:int) -> int:
    """
    This function counts power of number
    :param number: specific number to power e.g. 3
    :return: Power of number
    """
    if number == 0:
        return 1

    return number * power(number-1)


print(power(3))
print(power(4))
print(power(5))
