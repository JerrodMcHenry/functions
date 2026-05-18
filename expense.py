expenses = []

def add_expense(amount, category, description):
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)

def view_expenses():
    for expense in expenses:
        print(f'${expense['amount']} - {expense['category']} - {expense['description']}')

add_expense(35, 'debit', 'pay for last night')

print(expenses)