sentence = input('Text message: ')

for sign in sentence:
    print(f'The Unicode point of {sign} is {ord(sign)}')