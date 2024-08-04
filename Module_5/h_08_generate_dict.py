def get_stat(list_of_elements:list) -> dict:
    output = {}
    output["total"] = len(list_of_elements)
    output["mean"] = sum(list_of_elements) / len(list_of_elements)
    output["max"] = max(list_of_elements)
    output["min"] = min(list_of_elements)
    return output


print(get_stat([1,2,3,4]))