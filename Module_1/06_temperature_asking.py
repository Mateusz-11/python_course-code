temperature = float(input('Text current temperature: '))

if temperature <= 10:
    print('Stay at home')
elif 10 < temperature < 20:
    print('Take a jacket')
else:
    print('Have fun!')
