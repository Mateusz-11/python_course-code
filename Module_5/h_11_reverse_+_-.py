# e.g.: [1,2,3,-4] => [-1, -2, -3, 4]

def convert_list(list1:list) -> list:
    output = []
    for _ in list1:
        output.append(_*-1)
    return output


print(convert_list([1,2,3,-4]))
