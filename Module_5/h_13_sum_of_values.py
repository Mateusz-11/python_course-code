def sum_values(highest_number: int) -> int:
    if highest_number == 0:
        return 0
    return highest_number + sum_values(highest_number-1)


print(sum_values(5))
print(sum_values(3))
print(sum_values(2))
print(sum_values(1))
print(sum_values(0))
