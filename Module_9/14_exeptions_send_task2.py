try:
    fruits = []
    while len(fruits) < 10:
        print(fruits)
        _ = input('Write name of next fruit: ')
        if _ in fruits:
            raise Exception('This fruit is on the list!')
        fruits.append(_)


except Exception as e:
    print(e)