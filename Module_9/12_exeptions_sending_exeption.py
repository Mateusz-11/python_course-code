while True:
    value = int(input('Write number: '))
    if not value % 5 == 0:
        raise Exception("Number isn't divisible by 5")

    print(value)
