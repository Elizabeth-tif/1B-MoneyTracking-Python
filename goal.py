import datetime
import os
import csv
import msvcrt
import calendar

class Goal:
    def __init__(self, month_tracker, year_tracker):
        self.month_tracker = month_tracker
        self.year_tracker = year_tracker

    def set_goal(self):
        raise NotImplementedError("Subclasses must implement set_goal method")

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
    def __init__(self, month_tracker, year_tracker, category, amount):
        super().__init__(month_tracker, year_tracker)
        self.category = category
        self.amount = amount

    def set_goal(self):
        current_month_transactions = self.month_tracker.transactions  # Access transactions directly
        filtered_transactions = [transaction for transaction in current_month_transactions if
                                transaction['category'] == self.category and transaction['type'] == 'Expense']
        total_amount_spent = sum(transaction['amount'] for transaction in filtered_transactions)
        filled_progress, remaining_space, progress_percentage = self.calculate_progress(total_amount_spent, self.amount)
        self.print_progress(self.category, filled_progress, remaining_space, progress_percentage)


    def calculate_progress(self, total_amount_spent, goal_amount):
        if goal_amount == 0:
            excess_percentage = 0  # Set to 100% when goal_amount is zero
        else:
            excess_percentage = (total_amount_spent / goal_amount) * 100  # Calculate the progress percentage
        
        filled_progress = '▮' * min(int(excess_percentage / 10), 10)  # Limit visualization to 100% filled
        remaining_space = '▯' * max(10 - int(excess_percentage / 10), 0)  # No remaining space
        return filled_progress, remaining_space, excess_percentage

class Target(Goal):
    def __init__(self, month_tracker, year_tracker, target_date, amount):
        super().__init__(month_tracker, year_tracker)
        self.target_date = target_date
        self.amount = amount

    def set_goal(self):
        target_year_transactions = self.year_tracker.transactions  
        total_income = sum(transaction['amount'] for transaction in target_year_transactions if transaction['type'] == 'Income')
        total_expense = sum(transaction['amount'] for transaction in target_year_transactions if transaction['type'] == 'Expense')

        difference = total_income - total_expense
        filled_progress, remaining_space, progress_percentage = self.calculate_progress(difference, self.amount)
        print(f"{difference}/{self.amount}")
        if difference < 0:
            filled_progress = '▯' * 10
            remaining_space = '▮' * 0
        self.print_progress("Yearly Target", filled_progress, remaining_space, min(progress_percentage, 100))  # Cap at 100%

    def set_goalM(self):  
        target_month_transactions = self.month_tracker.transactions  # Access transactions directly
        total_income = sum(transaction['amount'] for transaction in target_month_transactions if transaction['type'] == 'Income')
        total_expense = sum(transaction['amount'] for transaction in target_month_transactions if transaction['type'] == 'Expense')

        difference = total_income - total_expense
        filled_progress, remaining_space, progress_percentage = self.calculate_progress(difference, self.amount)
        print(f"{difference}/{self.amount}")
        if difference < 0:
            filled_progress = '▯' * 10
            remaining_space = '▮' * 0
        self.print_progress("Target", filled_progress, remaining_space, min(progress_percentage, 100))


    def calculate_progress(self, total_amount_spent, goal_amount):
        if total_amount_spent > goal_amount:
            excess_percentage = (total_amount_spent / goal_amount) * 100  # Calculate the progress percentage
            filled_progress = '▮' * min(int(excess_percentage / 10), 10)  # Limit visualization to 100% filled
            remaining_space = '▯' * max(10 - int(excess_percentage / 10), 0)  # No remaining space
            return filled_progress, remaining_space, excess_percentage
        else:
            return super().calculate_progress(total_amount_spent, goal_amount)

class MonthTransaction:
    def __init__(self, user):
        self.transactions = []  # Store transactions here
        self.load_transactions(user)

    def load_transactions(self, user):
        current_date = datetime.date.today()
        start_date = datetime.date(current_date.year, current_date.month, 1)
        end_date = datetime.date(current_date.year, current_date.month, calendar.monthrange(current_date.year, current_date.month)[1])

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
        
        
class YearTransaction:
    def __init__(self, user):
        self.transactions = []  # Store transactions here
        self.load_transactions(user)

    def load_transactions(self, user):
        current_date = datetime.date.today()
        start_date = datetime.date(current_date.year, 1, 1)
        end_date = datetime.date(current_date.year, 12, calendar.monthrange(current_date.year, 12)[1])

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

class BudgetTracker:
    def __init__(self, user):
        self.user = user
        self.month_tracker = MonthTransaction(user)
        self.year_tracker = YearTransaction(user)
        self.budget_categories = ['Gadget', 'Kebutuhan Pokok', 'Hiburan', 'Kesehatan', 'Makanan & Minuman', 'Pendidikan', 'Transportasi']
        self.budgets = self._initialize_budgets()
        self.target_year = None
        self.target_month = None

    def _initialize_budgets(self):
        return {category: Budget(self.month_tracker, self.year_tracker, category, 0) for category in self.budget_categories}

    def _print_budgets_progress(self):
        for category, budget in self.budgets.items():
            total_amount_spent = sum(transaction['amount'] for transaction in self.month_tracker.transactions if transaction['category'] == category and transaction['type'] == 'Expense')
            print(f"{category} budget progress: \n{total_amount_spent} / {budget.amount}", end="\n" )
            budget.set_goal()

    def set_budget(self):
            print("======================== MONEY TRACKING APP ========================")
            print("=========================== BUDGET LIMIT ===========================")
            print("Available budget categories:")
            for i, category in enumerate(self.budget_categories, start=1):
                print(f"{i}. {category}")

            try:
                budget_choice = int(input("Enter the number corresponding to the budget category: "))
                selected_category = self.budget_categories[budget_choice - 1]
                budget_amount = float(input("Enter the budget amount: "))
            except (ValueError, IndexError):
                print("!! Input tidak valid, silahkan melakukan input ulang !!")
                return

            self.budgets[selected_category] = Budget(self.month_tracker, self.year_tracker,selected_category, budget_amount)

    def set_target(self):
        print("======================== MONEY TRACKING APP ========================")
        print("============================== TARGET ==============================")        
        try:
            target_year_amount = float(input("Enter the yearly target amount: "))
        except ValueError:
            print("!! Input tidak valid, silahkan melakukan input ulang !!")
            return

        self.target_year = Target(self.month_tracker, self.year_tracker, datetime.date.today(), target_year_amount)
        self.target_month = Target(self.month_tracker, self.year_tracker, datetime.date.today(), target_year_amount / 12)

    def show_budget_and_target(self):
        print("======================== MONEY TRACKING APP ========================")
        print("========================= BUDGET PROGRESS ==========================")
        self._print_budgets_progress()
        print("\n========================= TARGET PROGRESS ==========================")
        if self.target_year and self.target_month:
            print("Yearly target progress:")
            self.target_year.set_goal()
            print("Monthly target progress:")
            self.target_month.set_goalM()
        else:
            print("Targets are not set.")
        msvcrt.getch()

    def start_budget_tracker(self):
        while True:
            os.system('cls')
            print("======================== MONEY TRACKING APP ========================")
            print("========================== BUDGET & TARGET =========================")
            print("Options:")
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
                print("!! Input tidak valid, silahkan melakukan input ulang !!")
                msvcrt.getch()
                