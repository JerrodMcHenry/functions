# The global state. the entire prgram revolves around this variable.
# Every function either modifies it, reads from it, derives information from it
expenses = []

def get_expense_input():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    amount = float(amount)

    add_expense(amount, category, description)
    print("Expense added successfully.")

# Why parameters? Functions should recieve the data they operate on. 
# This makes the function reusalble, fixable and modular. Hardcoding values would destroy scalability
def add_expense(amount, category, description):

# Why a dictionary? Because one expense has multiple named fields. A dictionary models structured data
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

# Why append? Because we are adding to a collection and order matters. Previous expsneses must remain. This modifies application state
    expenses.append(expense)

def view_expenses():

#Why loop? There are many expenses and operations must happen repeatedly
    for expense in expenses:

# Why bracket notatation? Dictionaries sotre values by keys. You access the data via epense["amount"]
        print(f'${expense['amount']} - {expense['category']} - {expense['description']}')

# Why initialize the total? Accumulation requires a starting value. This is a running accumulator pattern.
def calculate_total():
    total = 0

# Why loop? - Tottls require processing every item. SUM the amount.
    for expense in expenses:
        total += expense["amount"]
# Why return instead of print? - Returned data can be resued, composed, tested and stored. Professional code returns data. 
    return total 

def filter_by_category(category):
# Why empty list? - You need a NEW collection. Matching items must be gathered. 
    filtered_expenses = []

    for expense in expenses:
# Why compare values? - Filtering is conditional selection.
        if expense["category"] == category:

# Why append mataching items? - Results must be colledcted. 
            filtered_expenses.append(expense)
    
    return filtered_expenses



def show_menu():
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Calculate total")
    print("4. Filter by category")
    print("5. Quit")


def run_app():
    while True:
        show_menu()
        choice = input ("Choose an option: ")

        if choice == "1":
            get_expense_input()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Total spent:", calculate_total())

        elif choice == "4":
            category = input("Enter category")
            results = filter_by_category(category)
            print(results)

        elif choice == "5":
            print("Goodbye")
            break
        
        else:
            print("Invalid option. Try again.")
        
run_app()