import os
from User import *

auth = User()

class Menu:
    def __init__(self) -> None:
        pass
    
    def showMenu(self,username,errorInput):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================== MONEY TRACKING APP ========================")
        print("============================== MENU ================================")
        print("Hi "+ username +", Welcome!!")
        if errorInput:
            print('!! Your input is not valid. Please try again. !!\n')
        print("1. Balances\n2. Recap\n3. Transaction History\n4. Budget & Target\n5. Log Out\n6. Exit")
        print('====================================================================')
        option = input("Your Input :")
        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            name=auth.login(False,False)
            self.showMenu(name,False)
        elif option == '6':
            exit()
        else:
            self.showMenu(username,True)
