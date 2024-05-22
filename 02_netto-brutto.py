net_value = float(input("Write netto value:"))
vat=0.23

gross = (net_value*(1 + vat))

print(f'Gross price from {net_value} is: {gross:.2f}')