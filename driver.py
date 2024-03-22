import inputData
import User
import Recap_UI
import TransactionHistory_UI
import tkinter
import os
import goal

# main driver
def main():
    auth = User.User()
    tracker = inputData.MoneyTracker()

    # Start tkinter's main loop
    root = tkinter.Tk()
    root.withdraw()
    root.update()
    
    user = auth.login(False)
    tracker.createFile(user)
    
    while True:
        os.system('cls')
        print("\nMoney Tracking App")
        print("Selamat datang, ",user,"!")
        print("1. Input Income")
        print("2. Input Outcome")
        print("3. Recap")
        print("4. Transaction History")
        print("5. Load Dari File")
        print("6. Budget & Target")
        print("7. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            date = inputData.get_valid_date_input("Enter a date (YYYY-MM-DD): ")
            notes = input("Enter the notes (leave - if no notes):")
            tracker.add_transaction(user, amount, 'Income', 'Income', date, notes)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            date = inputData.get_valid_date_input("Enter a date (YYYY-MM-DD): ")
            category = tracker.categoryPicking()
            notes = input("Enter the notes (leave - if no notes): ")
            tracker.add_transaction(user, amount, 'Expense', category, date, notes)
        elif choice == '3':
            Recap_UI.recap(user)
        elif choice == '4':
            TransactionHistory_UI.histori(user)
        elif choice == '5':
            root.deiconify()
            tracker.updateTransaction(user)  # Call the function from inputData.py
            root.withdraw()
            root.update()
        elif choice == '6':
            budget_tracker = goal.BudgetTracker(user)
            budget_tracker.start_budget_tracker()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()