import inputData

# main driver
def main():
    tracker = inputData.MoneyTracker()
    while True:
        print("\nMoney Tracking App")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Transactions")
        print("4. Load From File")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            date = inputData.get_valid_date_input("Enter a date (YYYY-MM-DD): ")
            notes = input("Enter the notes (leave - if no notes):")
            tracker.add_transaction(amount, 'Income', 'Income', date, notes)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            date = inputData.get_valid_date_input("Enter a date (YYYY-MM-DD): ")
            category = tracker.categoryPicking()
            notes = input("Enter the notes (leave - if no notes):")
            tracker.add_transaction(amount, 'Expense', category, date, notes)
        elif choice == '3':
            print("display")
        elif choice == '4':
            print('check')
            tracker.updateTransaction()  # Call the function from inputData.py
            print('check')
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()