def filter_evens(to_filter: list) -> list:
    output = []
    for el in to_filter:
        if el % 2 == 0:
            output.append(el)

    return output


print(filter_evens([1,2,3,4,5,6,7,8]))