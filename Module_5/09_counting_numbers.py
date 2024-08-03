def count_numbers(numbers: list, count_odd: bool = True, count_even: bool = True):
    """
    This function counts numbers by arguments

    :param numbers: List of arguments
    :param count_odd: Should I count odd numebrs?
    :param count_even: Should I count even numbers?
    :return: How many numbers exists in the argument (odd or even)
    """
    total = 0
    for number in numbers:
        if number % 2 == 0 and count_even:
            total += 1
        elif count_odd:
            total += 1

    return total


print(count_numbers([1,2,3,4,5,6], count_odd= False))