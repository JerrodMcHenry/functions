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

def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total 

def filter_by_category(category):
    filtered_expenses = []

    for expense in expenses:
        if expense["category"] == category:
            filtered_expenses.append(expense)
    
    return filtered_expenses

add_expense(25, "food", "Chipotle")
add_expense(80, "gas", "Chevron")
add_expense(15, "food", "Starbucks")

view_expenses()

print("Total spent:", calculate_total())

food_expenses = filter_by_category("food")
print(food_expenses)