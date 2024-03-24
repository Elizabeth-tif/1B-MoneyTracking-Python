import os
from Auth import *
import Balances
import Recap_UI
import TransactionHistory_UI
import os
import goal
import inputData

auth = Auth()

class Menu:
    def __init__(self) -> None:
        pass
    
    def showMenu(self,username,errorInput,root):
        balances = Balances.Balances()
        # Start tkinter's main loop
        tracker = inputData.MoneyTracker()
        tracker.createFile(username)
        inputData.check_install_tabulate()

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("======================== MONEY TRACKING APP ========================")
            print("============================== MENU ================================")
            print("Hi "+ username +", Welcome!!")
            if errorInput:
                print('!! Your input is not valid. Please try again. !!\n')
            print("1. Balances\n2. Recap\n3. Transaction History\n4. Budget & Target\n5. Load From File\n6. Log Out\n7. Exit")
            print('====================================================================')
            option = input("Your Input :")
            if option == '1':
                balances.showBalancesMenu(False,username)
            elif option == '2':
                Recap_UI.recap(username)
            elif option == '3':
                TransactionHistory_UI.histori(username)
            elif option == '4':
                budget_tracker = goal.BudgetTracker(username)
                budget_tracker.start_budget_tracker(username)
            elif option == '5':
                root.deiconify()
                tracker.updateTransaction(username)  # Call the function from inputData.py
                root.withdraw()
                root.update()
            elif option == '6':
                name=auth.login(False,False)
                self.showMenu(name,False)
            elif option == '7':
                exit()
                break
            else:
                self.showMenu(username,True)
