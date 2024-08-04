def sort_number(number: int) -> int:
    numbers = list(str(number))
    numbers.sort(reverse=True)
    output = "".join(numbers)
    return int(output)


print(f"Unsorted intigers: 123456. Sorted intigers (max to min): {sort_number(123456)}")
print(f"Unsorted intigers: 143986. Sorted intigers (max to min): {sort_number(143986)}")
