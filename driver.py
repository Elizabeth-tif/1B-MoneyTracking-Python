import inputData
import datetime

#a function to input a valid date
def get_valid_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            # Attempt to parse the input string into a date object
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return date_obj
        except ValueError:
            # If parsing fails, inform the user and prompt again
            print("Invalid date format. Please enter date in YYYY-MM-DD and valid date format.")

#main driver
def main():
    tracker = inputData.MoneyTracker()
    while True:
        print("\nMoney Tracking App")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Transactions")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            date = get_valid_date_input("Enter a date (YYYY-MM-DD): ")
            notes = input("Enter the notes (leave - if no notes):")
            tracker.add_transaction(amount, 'Income', 'Income', date, notes)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            date = get_valid_date_input("Enter a date (YYYY-MM-DD): ")
            category = tracker.categoryPicking()
            notes = input("Enter the notes (leave - if no notes):")
            tracker.add_transaction(amount, 'Expense', category, date, notes)
        elif choice == '3':
            tracker.display_transactions()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()