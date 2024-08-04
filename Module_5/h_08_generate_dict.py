def get_stat(list_of_elements:list) -> dict:
    output = {"total": len(list_of_elements),
              "mean": sum(list_of_elements) / len(list_of_elements),
              "max": max(list_of_elements),
              "min": min(list_of_elements)}
    return output


print(get_stat([1,2,3,4]))