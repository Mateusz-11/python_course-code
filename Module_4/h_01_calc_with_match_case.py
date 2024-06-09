# Napisz program, który będzie wykonywał różne operacje matematyczne.
# w zależności od wyboru użytkownika. Uzytkownik powinien mieć możliwość wyboru między: + - * /

while True:
    value1 = int(input('Value 1: '))
    value2 = int(input('Value 2: '))
    action = input('What do you want to do? [+] [-] [*] [/]')

    match action:
        case '+':
            result = value1 + value2
        case '-':
            result = value1 - value2
        case '*':
            result = value1 * value2
        case '/':
            result = value1 / value2
        case _:
            print('Error. Bad Answer')
            break

    print(f'Output of operations = {result}')
