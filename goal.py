import datetime
import os
import csv
import msvcrt
import calendar

class SaveBnT:
    def __init__(self, user, file_name=None):
        if file_name is None:
            file_name = user + '_budget_target.csv'
        self.file_name = file_name
        self.data = self.loadData(user)

    def add_data(self, idx, value):
        self.data[idx] = value
        self.save_to_file()

    def save_to_file(self):
        with open(self.file_name, 'w') as file:
            csv_line = ','.join(map(str, self.data))
            file.write(csv_line)

    def loadData(self, user):
        try:
            with open(user + '_budget_target.csv', 'r') as file:
                data = file.read()
                data = data.split(',')
                loaded_data = [float(value) for value in data]  
                return loaded_data  
        except FileNotFoundError:
            self.saveToFile(user)
            return [0.0] * 8 
    def saveToFile(self, user):
        with open(self.file_name, 'w') as file:
            default_data = ','.join('0.0' for _ in range(8))  
            file.write(default_data)
    
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

        filled_progress = '▮' * int(progress_percentage / 10)  
        remaining_space = '▯' * (10 - int(progress_percentage / 10))  
        return filled_progress, remaining_space, progress_percentage

    def print_progress(self, category, filled_progress, remaining_space, progress_percentage):
        print(f"[{filled_progress}{remaining_space} ] {progress_percentage:.2f}%")

class Budget(Goal):
    def __init__(self, month_tracker, year_tracker, category, amount):
        super().__init__(month_tracker, year_tracker)
        self.category = category
        self.amount = amount

    def set_goal(self, budget_data):  
        current_month_transactions = self.month_tracker.transactions  
        filtered_transactions = [transaction for transaction in current_month_transactions if
                                transaction['category'] == self.category and transaction['type'] == 'Expense']
        total_amount_spent = sum(transaction['amount'] for transaction in filtered_transactions)
        
        if (self.category == 'Gadget'):
            category = 0 
        elif (self.category == 'Kebutuhan Pokok'):
            category = 1
        elif (self.category == 'Hiburan'):
            category = 2
        elif (self.category == 'Kesehatan'):
            category = 3
        elif (self.category == 'Makanan & Minuman'):
            category = 4
        elif (self.category == 'Pendidikan'):
            category = 5
        elif (self.category == 'Transportasi'):
            category = 6
        
        budget_amount = budget_data[category]
        
        filled_progress, remaining_space, progress_percentage = self.calculate_progress(total_amount_spent, budget_amount)
        self.print_progress(self.category, filled_progress, remaining_space, progress_percentage)

    def calculate_progress(self, total_amount_spent, goal_amount):
        if goal_amount == 0:
            excess_percentage = 0  
        else:
            excess_percentage = (total_amount_spent / goal_amount) * 100  
        
        filled_progress = '▮' * min(int(excess_percentage / 10), 10)  
        remaining_space = '▯' * max(10 - int(excess_percentage / 10), 0)  
        return filled_progress, remaining_space, excess_percentage

class Target(Goal):
    def __init__(self, month_tracker, year_tracker, target_date, amount):
        super().__init__(month_tracker, year_tracker)
        self.target_date = target_date
        self.amount = amount

    def set_goal(self,data):
        self.amount = data[7]
        target_year_transactions = self.year_tracker.transactions  
        total_income = sum(transaction['amount']
        for transaction in target_year_transactions if transaction['type'] == 'Income')
        total_expense = sum(transaction['amount'] for transaction in target_year_transactions if transaction['type'] == 'Expense')
        difference = total_income - total_expense
        filled_progress, remaining_space, progress_percentage = self.calculate_progress(difference, self.amount)
        print(f"{difference}/{self.amount}")
        if difference < 0:
            filled_progress = '▯' * 10
            remaining_space = '▮' * 0
        self.print_progress("Yearly Target", filled_progress, remaining_space, min(progress_percentage, 100))  

    def set_goalM(self,data):
        self.amount = data[7] / 12
        target_month_transactions = self.month_tracker.transactions  
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
            if goal_amount == 0:
                excess_percentage = 0
            else:
                excess_percentage = (total_amount_spent / goal_amount) * 100  
            filled_progress = '▮' * min(int(excess_percentage / 10), 10)  
            remaining_space = '▯' * max(10 - int(excess_percentage / 10), 0)  
            return filled_progress, remaining_space, excess_percentage
        else:
            return super().calculate_progress(total_amount_spent, goal_amount)

class MonthTransaction:
    def __init__(self, user):
        self.transactions = []  
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
                    
                    if start_date is not None and date_obj < start_date:
                        continue
                    if end_date is not None and date_obj > end_date:
                        continue
                    transaction = {
                        'type': row[0],  
                        'date': date_obj,
                        'amount': float(row[2]),
                        'category': row[3].strip(),  
                        'notes': row[4]
                    }
                    self.transactions.append(transaction)
                    print(f"Transaction {row_number} loaded:", transaction)
                except ValueError as e:
                    
                    print(f"Skipping row {row_number} due to ValueError:", e)
                    continue

        
        self.transactions = sorted(self.transactions, key=lambda x: x['date'])


class YearTransaction:
    def __init__(self, user):
        self.transactions = []  
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
                    
                    if start_date is not None and date_obj < start_date:
                        continue
                    if end_date is not None and date_obj > end_date:
                        continue
                    transaction = {
                        'type': row[0],  
                        'date': date_obj,
                        'amount': float(row[2]),
                        'category': row[3].strip(),  
                        'notes': row[4]
                    }
                    self.transactions.append(transaction)
                    print(f"Transaction {row_number} loaded:", transaction)
                except ValueError as e:
                    
                    print(f"Skipping row {row_number} due to ValueError:", e)
                    continue

        
        self.transactions = sorted(self.transactions, key=lambda x: x['date'])

class BudgetTracker:
    def __init__(self, user):
        self.user = user
        self.month_tracker = MonthTransaction(user)
        self.year_tracker = YearTransaction(user)
        self.budget_categories = ['Gadget', 'Kebutuhan Pokok', 'Hiburan', 'Kesehatan', 'Makanan & Minuman', 'Pendidikan', 'Transportasi']
        self.budgets = self._initialize_budgets()
        self.savebnt = SaveBnT(user)
        save = SaveBnT(user)
        data = save.loadData(user)
        self.target_year = Target(self.month_tracker, self.year_tracker, datetime.date.today(), data[7])  
        self.target_month = Target(self.month_tracker, self.year_tracker, datetime.date.today(), data[7] / 12)

    def _initialize_budgets(self):
        return {category: Budget(self.month_tracker, self.year_tracker, category, 0) for category in self.budget_categories}

    def set_budget(self):
        save = SaveBnT(self.user)
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

        save.add_data(budget_choice-1, budget_amount)
        self.budgets[selected_category] = Budget(self.month_tracker, self.year_tracker, selected_category, budget_amount)
            
    def set_target(self):
        save = SaveBnT(self.user)
        print("======================== MONEY TRACKING APP ========================")
        print("============================== TARGET ==============================")        
        try:
            target_year_amount = float(input("Enter the yearly target amount: "))
        except ValueError:
            print("!! Input tidak valid, silahkan melakukan input ulang !!")
            return

        
        self.target_year = Target(self.month_tracker, self.year_tracker, datetime.date.today(), target_year_amount)
        self.target_month = Target(self.month_tracker, self.year_tracker, datetime.date.today(), target_year_amount / 12)
        
        save.add_data(7, target_year_amount)


    def show_budget_and_target(self, save):
        print("======================== MONEY TRACKING APP ========================")
        print("========================= BUDGET PROGRESS ==========================")
        data = save.loadData(self.user)  
        for i, (category, budget) in enumerate(self.budgets.items()):
            total_amount_spent = sum(transaction['amount'] for transaction in self.month_tracker.transactions if transaction['category'] == category and transaction['type'] == 'Expense')
            budget_amount = data[i]  
            print(f"{category} budget progress: \n{total_amount_spent} / {budget_amount}", end="\n")
            budget.set_goal(data)  
        print("\n========================= TARGET PROGRESS ==========================")
        if self.target_year is not None:  
            print("Yearly target progress:")
            self.target_year.set_goal(data)
            print("Monthly target progress:")
            self.target_month.set_goalM(data)
        else:
            print("Targets are not set.")
        msvcrt.getch()


    def start_budget_tracker(self,user):
        save = SaveBnT(user)
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
                self.show_budget_and_target(save)
            elif choice == 4:
                return
            else:
                print("!! Input tidak valid, silahkan melakukan input ulang !!")
                msvcrt.getch()