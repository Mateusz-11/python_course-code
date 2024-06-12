account_balance = 1000

while True:
    print('- - - ' * 5)
    action = int(input(
        "What do you want to do? \n [1] - payment on account \n [2] - withdrawal from the account \n [3] - checking account balance \n [0] - exit \n >>"
    ))
    match action:
        case 1:
            number = int(input('what amount do you want to deposit? '))
            account_balance += number
        case 2:
            number = int(input('what amount do you want to withdraw? '))
            if number > account_balance:
                print('Operation is impossible. Your account balance is insufficient')
            else:
                account_balance -= number
        case 3:
            print(f'Your account balance: {account_balance}')
        case 0:
            exit()
        case _:
            print('Incorrect value')
