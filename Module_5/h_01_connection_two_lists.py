def add_lists(list1:list, list2:list) -> list:
    """
    This function connect 2 lists
    :param list1:
    :param list2:
    :return: New list
    """
    output = []
    for el1, el2 in zip(list1,list2):
        output.append(el1 + el2)
    return output


print(add_lists([1,2,3,4], [0,9,8,7]))
