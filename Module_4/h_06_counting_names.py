result = {}
while True:
    status = input('If you finished, write "End". To continue press Enter: ')
    if status.lower() == "end":
        break
    print('- - - ' * 5)
    name = input('Write name to add: ')
    # print(result.get(name, 0) + 1)
    result[name] = result.get(name, 0) + 1
    print(result)

names = sorted(list(result.keys()))
print(names)
