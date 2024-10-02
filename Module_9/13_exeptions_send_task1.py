source_code = ""

while True:
    text = input('Write text to revers: ')
    if text == "":
        raise ValueError('Empty string. Try again')
    else:
        source_code = text
        break

def rev_str(text_to_conv):
    return text_to_conv[::-1]

reversed_text = rev_str(text)

print(reversed_text)


