def count_char(text: str, char_start:str='(', char_end:str = ')'):
    should_i_count_char = False
    counter = 0
    for char in text:
        if char == char_end:
            should_i_count_char = False

        if should_i_count_char:
            counter += 1

        if char == char_start:
            should_i_count_char = True

    return counter

print('0->', count_char("Lorem ipsum dolor sit amet"))
print('5->', count_char("(Lorem) ipsum dolor sit amet"))
print('10->', count_char("(Lorem) ipsum (dolor) sit amet"))

