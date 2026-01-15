import json

FILENAME = 'expenses.json'


def read_data():
    with open(FILENAME) as f:
        expenses = json.loads(f.read())

    return expenses


def add_expense():
    print('Add Expense:')
    amount = float(input('Amount: '))
    category = input('Category: ')

    new_expense = {
        'amount': amount,
        'category': category
    }

    expenses = read_data()

    expenses.append(new_expense)

    with open(FILENAME, 'w') as f:
        f.write(json.dumps(expenses, indent=4))


def show_expenses():
    expenses = read_data()

    print('All Expenses:')
    for expense in expenses:
        print(f'{expense["category"]}: {expense["amount"]:,.2f} so\'m')


def report_expenses():
    expenses = read_data()

    groups = {}
    for expense in expenses:
        groups.setdefault(expense['category'], []).append(expense['amount'])

    for group, amounts in groups.items():
        print(group, sum(amounts))


def main():
    while True:
        print('-----menu-----')
        print('1. Add Expense')
        print('2. Show Expenses')
        print('3. Report Expenses')
        print('0. Quit')

        choice = input('> ')
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            report_expenses()
        elif choice == '0':
            print('bye.')
            break
        else:
            print('bunday menu mavjud emas.')

main()
