import datetime
import os
import csv
import msvcrt

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

class Target(Goal):
    def __init__(self, money_tracker, target_date, amount):
        super().__init__(money_tracker)
        self.target_date = target_date
        self.amount = amount

    def set_goal(self):
        current_year_transactions = self.get_transactions_current_year()
        total_income = sum(transaction['amount'] for transaction in current_year_transactions if transaction['type'] == 'income')
        total_outcome = sum(transaction['amount'] for transaction in current_year_transactions if transaction['type'] == 'outcome')

        difference = total_income - total_outcome
        filled_progress, remaining_space, progress_percentage = self.calculate_progress(difference, self.amount)
        self.print_progress("Target", filled_progress, remaining_space, progress_percentage)

class MoneyTracker:
    def __init__(self, user):
        self.transactions = []  # Store transactions here
        self.load_transactions(user)

    def load_transactions(self, user, start_date=None, end_date=None):
        with open(user + '_transaction.csv', 'r') as readcsv:
            csvreader = csv.reader(readcsv)
            for row_number, row in enumerate(csvreader, start=1):
                try:
                    date_obj = datetime.datetime.strptime(row[1], '%Y-%m-%d').date()
                    # Check if the transaction date is within the specified range
                    if start_date is not None and date_obj < start_date:
                        continue
                    if end_date is not None and date_obj > end_date:
                        continue
                    transaction = {
                        'type': row[0],  # 'type' : 'Income' or 'Expense'
                        'date': date_obj,
                        'amount': float(row[2]),
                        'category': row[3].strip(),  # Remove leading/trailing whitespace
                        'notes': row[4]
                    }
                    self.transactions.append(transaction)
                    print(f"Transaction {row_number} loaded:", transaction)
                except ValueError as e:
                    # Error Handling if the date is not in the format YYYY-MM-DD
                    print(f"Skipping row {row_number} due to ValueError:", e)
                    continue

        # Sort data based on dates
        self.transactions = sorted(self.transactions, key=lambda x: x['date'])

# Add this line to check if transactions are loaded properly
money_tracker = MoneyTracker('user')
print("Transactions:", money_tracker.transactions)


class BudgetTracker:
    def __init__(self, user):
        self.user = user
        self.money_tracker = MoneyTracker(user)
        self.budget_categories = ['Gadget', 'Kebutuhan Pokok', 'Hiburan', 'Kesehatan', 'Makanan & Minuman', 'Pendidikan', 'Transportasi']
        self.budgets = self._initialize_budgets()
        self.target_year = None
        self.target_month = None

    def _initialize_budgets(self):
        return {category: Budget(self.money_tracker, category, 0) for category in self.budget_categories}

    def _print_budgets_progress(self):
        for category, budget in self.budgets.items():
            total_amount_spent = sum(transaction['amount'] for transaction in self.money_tracker.transactions if transaction['category'] == category and transaction['type'] == 'outcome')
            print(f"{category} budget progress: \n{total_amount_spent} / {budget.amount}", end="\n" )
            budget.set_goal()

    def set_budget(self):
        print("Available budget categories:")
        for i, category in enumerate(self.budget_categories, start=1):
            print(f"{i}. {category}")

        budget_choice = int(input("Enter the number corresponding to the budget category: "))
        selected_category = self.budget_categories[budget_choice - 1]
        budget_amount = float(input("Enter the budget amount: "))

        self.budgets[selected_category] = Budget(self.money_tracker, selected_category, budget_amount)

    def set_target(self):
        target_year_amount = float(input("Enter the yearly target amount: "))
        self.target_year = Target(self.money_tracker, datetime.date.today(), target_year_amount)
        self.target_month = Target(self.money_tracker, datetime.date.today(), target_year_amount / 12)

    def show_budget_and_target(self):
        print("Budgets:")
        self._print_budgets_progress()

        if self.target_year and self.target_month:
            print("\nYearly target progress:")
            self.target_year.set_goal()
            print("Monthly target progress:")
            self.target_month.set_goal()
        else:
            print("\nTargets are not set.")
        msvcrt.getch()

    def start_budget_tracker(self):
        while True:
            os.system('cls')
            print("\nOptions:")
            print("1. Set budget")
            print("2. Set target")
            print("3. Show budget and target")
            print("4. Back to main menu")

            choice = int(input("Enter your choice: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == 1:
                self.set_budget()
            elif choice == 2:
                self.set_target()
            elif choice == 3:
                self.show_budget_and_target()
            elif choice == 4:
                return
            else:
                print("Invalid choice. Please enter a valid option.")

budget_tracker = BudgetTracker('user')
budget_tracker.start_budget_tracker()