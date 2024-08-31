name = input('Your name: ')
surname = input('Your surname: ')

with open('h_03_file.txt', mode='a', encoding='utf8') as file:
    file.write(f'{name};{surname}\n')