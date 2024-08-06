def simple_sum(limit, *args):
    total = 0
    for _ in args:
        if _ > limit:
            total += _

    return total


print(simple_sum(4, 1, 2, 3, 4, 5, 6))
