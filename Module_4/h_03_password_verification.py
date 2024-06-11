string_to_check = "qwe123"

while True:
    print('- - - ' * 5)
    user_try = input('Write password: ')
    if string_to_check == user_try:
        print('Correct password!')
        break
    else:
        print('Password incorrect')
