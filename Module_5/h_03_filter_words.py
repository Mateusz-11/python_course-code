def filter_words(to_filter: list, min_length: int = 4, max_length:int = 8) -> list:
    output = []
    for element in to_filter:
        if min_length < len(element) < max_length:
            output.append(element)
    return output


print(filter_words(['python', 'java', 'javascript', 'go', 'kotlin']))