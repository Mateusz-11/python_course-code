CONTROL_NUMBER_LIST = list("13791379131")

for i, value in enumerate(CONTROL_NUMBER_LIST):
    CONTROL_NUMBER_LIST[i] = int(value)

pesel1 = list("18210177915")
pesel2 = list("99010124415")

for i, value in enumerate(pesel1):
    pesel1[i] = int(value)

total = 0
if len(pesel1) == 11:
    for control, pesel in zip(CONTROL_NUMBER_LIST, pesel1):
        total += control * pesel
    if total % 10 == 0:
        print('Pesel is correct')
    else:
        print('Pesel is incorect')
        print(total)
else:
    print('Length of number isn\'t correct')
