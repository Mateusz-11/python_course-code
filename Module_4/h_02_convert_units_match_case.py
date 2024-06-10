# Calculator of units - unce - kg - pund

kg_ounce = 35.274
kg_pound = 2.20462

value = int(input('Value: '))
action = int(input(
    'What convert you want do? \n [1] - kg to ounce \n [2] - ounce to kg \n [3] - kg to pound \n [4] - pound to kg ')
)
match action:
    case 1:
        print(f"{value} kg = {value * kg_ounce} ounce")
    case 2:
        print(f"{value} ounce = {value / kg_ounce} kg")
    case 3:
        print(f"{value} kg = {value * kg_pound} pound")
    case 4:
        print(f"{value} pound = {value / kg_pound} kg")
    case _:
        print(f"Incorrect value")
