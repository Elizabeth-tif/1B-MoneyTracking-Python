import datetime

class Goal:
    def __init__(self, money_tracker):
        self.money_tracker = money_tracker

    def set_goal(self):
        raise NotImplementedError("Subclasses must implement set_goal method")

    def get_transactions_current_month(self):
        current_date = datetime.date.today()
        current_month = current_date.month
        current_year = current_date.year
        transactions = self.money_tracker.transactions
        return [transaction for transaction in transactions if transaction['date'].month == current_month and transaction['date'].year == current_year]

    def get_transactions_current_year(self):
        current_year = datetime.date.today().year
        transactions = self.money_tracker.transactions
        return [transaction for transaction in transactions if transaction['date'].year == current_year]
    
    def calculate_progress(self, total_amount_spent, goal_amount):
        if goal_amount == 0:
            progress_percentage = 0
        else:
            progress_percentage = (total_amount_spent / goal_amount) * 100
        
        filled_progress = '▮' * int(progress_percentage / 10)  # Filled progress
        remaining_space = '▯' * (10 - int(progress_percentage / 10))  # Remaining space
        return filled_progress, remaining_space, progress_percentage

    def print_progress(self, category, filled_progress, remaining_space, progress_percentage):
        print(f"[{filled_progress}{remaining_space} ] {progress_percentage:.2f}%")

class Budget(Goal):
    def __init__(self, money_tracker, category, amount):
        super().__init__(money_tracker)
        self.category = category
        self.amount = amount

    def set_goal(self):
        current_month_transactions = self.get_transactions_current_month()
        filtered_transactions = [transaction for transaction in current_month_transactions if transaction['category'] == self.category and transaction['type'] == 'outcome']
        total_amount_spent = sum(transaction['amount'] for transaction in filtered_transactions)
        filled_progress, remaining_space, progress_percentage = self.calculate_progress(total_amount_spent, self.amount)
        self.print_progress(self.category, filled_progress, remaining_space, progress_percentage)
        
    def initObj(self):
        return Budget(self.money_tracker, "", 0)  # Initialize with default values

class Target(Goal):
    def __init__(self, money_tracker, target_date, amount):
        super().__init__(money_tracker)
        self.target_date = target_date
        self.amount = amount

    def set_goal(self):
        current_year_transactions = self.get_transactions_current_year()
        income_transactions = [transaction['amount'] for transaction in current_year_transactions if transaction['type'] == 'income']
        outcome_transactions = [transaction['amount'] for transaction in current_year_transactions if transaction['type'] == 'outcome']

        total_income = sum(income_transactions)
        total_outcome = sum(outcome_transactions)

        difference = total_income - total_outcome
        filled_progress, remaining_space, progress_percentage = self.calculate_progress(difference, self.amount)
        self.print_progress("Target", filled_progress, remaining_space, progress_percentage)

# Example usage
class MoneyTracker:
    def __init__(self):
        # Simulating transaction data
        self.transactions = [
            {'date': datetime.date(2024, 3, 15), 'type': 'outcome', 'category': 'Groceries', 'amount': 50},
            {'date': datetime.date(2024, 3, 18), 'type': 'outcome', 'category': 'Shopping', 'amount': 100},
            {'date': datetime.date(2024, 3, 20), 'type': 'income', 'category': 'Salary', 'amount': 2000},
            {'date': datetime.date(2024, 3, 22), 'type': 'outcome', 'category': 'Transport', 'amount': 30},
            {'date': datetime.date(2024, 3, 25), 'type': 'outcome', 'category': 'Groceries', 'amount': 40}
        ]

money_tracker = MoneyTracker()

# User input for budget category and amount
budget_categories = ['Gadget', 'Kebutuhan Pokok', 'Hiburan', 'Kesehatan', 'Makanan & Minuman', 'Pendidikan', 'Transportasi']
print("Available budget categories:")
for i, category in enumerate(budget_categories, start=1):
    print(f"{i}. {category}")

# Initialize Budget objects with default values
budgets = {category: Budget(money_tracker, category, 0) for category in budget_categories}

budget_choice = int(input("Enter the number corresponding to the budget category: "))
selected_category = budget_categories[budget_choice - 1]

budget_amount = float(input("Enter the budget amount: "))
budget = Budget(money_tracker, selected_category, budget_amount)

# Assign the created Budget object to the corresponding variable based on the selected category
budgets[selected_category] = budget

# Creating Budget objects
for budget_category, budget_obj in budgets.items():
    print(f"{budget_category} budget progress:")
    budget_obj.set_goal()

# User input for target amount
target_year_amount = float(input("Enter the yearly target amount: "))

# Creating Target objects for yearly and monthly goals
target_year = Target(money_tracker, datetime.date.today(), target_year_amount)
target_month = Target(money_tracker, datetime.date.today(), target_year_amount / 12)

# Setting goals for yearly and monthly targets
print("Yearly target progress:")
target_year.set_goal()
print("Monthly target progress:")
target_month.set_goal()
