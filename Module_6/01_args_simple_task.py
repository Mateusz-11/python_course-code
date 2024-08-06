def simple_sum(limit: int = 0, *args) -> int:
    total = 0
    for arg in args:
        if arg > limit:
            total += arg

    return total


print(simple_sum(4, 1, 2, 3, 4, 5, 6))
