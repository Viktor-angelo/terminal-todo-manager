import json

gastos = []

# function to add 
def add_expense():
    description = str(input('\033[4mDescription: \033[m'))
    value = float(input('\033[4mAmount: R$\033[m'))
    category = str(input('\033[4mCategory: \033[m'))

    expense = {
        'description': description,
        'value': value,
        'category': category
    }
    gastos.append(expense)
    print('\033[32mExpense added successfully!\033[m')

# function to list 
def list_expenses():
    if not gastos:
        print('\033[31mNo expenses recorded yet.\n\033[m')
    else:
        print('\033[4m----List of Expenses----\033[m')
        for i, expense in enumerate(gastos, 1):
            print(f"\033[4m{i}. {expense['description']} - R${expense['value']:.2f} - {expense['category']}\033[m")
        print('')

# function to save
def save_expenses():
    with open('gastos.json', 'w') as file:
        json.dump(gastos, file, indent=4)
    print("\033[32mExpenses saved successfully.\n\033[m")

# function to load 
def load_expenses():
    global gastos
    try:
        with open('gastos.json', 'r') as file:
            gastos = json.load(file)
        print('\033[32mExpenses loaded successfully.\n\033[m')
    except FileNotFoundError:
        print('\033[31mExpenses file not found.\n\033[m')

# function to remove
def remove_expense():
    list_expenses()
    if not gastos:
        return
    try:
        num = int(input('\033[4mEnter the number of the expense to remove: \033[m'))
        if 1 <= num <= len(gastos):
            removed = gastos.pop(num - 1)
            print(f"\033[32mExpense '{removed['description']}' removed successfully!\033[m")
        else:
            print('\033[31mInvalid number.\033[m')
    except ValueError:
        print('\033[31mPlease enter a valid number.\033[m')

# main menu function
def menu():
    load_expenses()
    while True:
        print("\033[34m==== MENU ====\033[m")
        print("\033[4m[ 1 ] Add expense\033[m")
        print("\033[4m[ 2 ] List expenses\033[m")
        print("\033[4m[ 3 ] Save expenses\033[m")
        print("\033[4m[ 4 ] Exit\033[m")
        print("\033[4m[ 5 ] Remove expense\033[m")

        choice = int(input('\033[4mChoose an option (1-5): \033[m'))
        if choice == 1:
            add_expense()
        elif choice == 2:
            list_expenses()
        elif choice == 3:
            save_expenses()
        elif choice == 4:
            print("\033[4mExiting...\033[m")
            break
        elif choice == 5:
            remove_expense()
        else:
            print('\033[31mInvalid option.\n\033[m')

# start the program
menu()
