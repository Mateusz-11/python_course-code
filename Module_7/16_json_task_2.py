from json import load, dump

operation = input('What you want to do? [a] Add expense [s] Show all: ')

with open("16_expenses.json") as file:
    expenses = load(file)

if operation == "a":
    new_category = input("What is the expense for? ")
    new_amount = input("How much was spent? ")

    with open("16_expenses.json", mode="w") as file:
        expenses.append({
            "category": new_category,
            "amount": new_amount
        })
        dump(expenses, file)

elif operation == "s":
    print("All expenses:")
    for expense in expenses:
        print("Category: ", expense.get('category'))
        print("Amount: ", expense.get('amount'))
        print("- - - " * 5)

else:
    print("Wrong answer")

