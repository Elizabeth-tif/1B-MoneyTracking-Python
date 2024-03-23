import os
from datetime import date
import inputData
import Menu

class Balances:
    def __init__(self) -> None:
        pass

    def getCurrentBalance(self,name):
        incomeFile = open(name+"_income.csv","r")
        incomes = incomeFile.readlines()
        incomeFile.close
        outcomeFile = open(name+"_outcome.csv","r")
        outcomes = outcomeFile.readlines()
        outcomeFile.close
        currentBalance=0
        i = 0
        while (i<len(incomes)):
            income = incomes[i].split(',')
            currentBalance = currentBalance + float(income[1])
            i=i+1
        i = 0
        while (i<len(outcomes)):
            outcome = outcomes[i].split(',')
            currentBalance = currentBalance - float(outcome[1])
            i=i+1
        return str(currentBalance)

    def getThisMonthIncome(self,name):
        incomeFile = open(name+"_income.csv","r")
        incomes = incomeFile.readlines()
        incomeFile.close

        nowDate = date.today()
        nowDate = str(nowDate).split('-')
        nowYear = nowDate[0]
        nowMonth = nowDate[1]

        thisMonthIncome = 0
        i = 0
        while (i<len(incomes)):
            income = incomes[i].split(',')
            dates = income[0].split('-')
            year = dates[0]
            month = dates[1]
            if (year==nowYear and month==nowMonth):
                thisMonthIncome = thisMonthIncome + float(income[1])
            i=i+1
        return str(thisMonthIncome)
    
    def getLastMonthIncome(self,name):
        incomeFile = open(name+"_income.csv","r")
        incomes = incomeFile.readlines()
        incomeFile.close

        nowDate = date.today()
        nowDate = str(nowDate).split('-')
        nowYear = int(nowDate[0])
        nowMonth = int(nowDate[1])
        if (nowMonth==1):
            lastMonth = 12
            lastYear = nowYear - 1
        else:
            lastMonth = nowMonth - 1
            lastYear = nowYear

        lastMonthIncome = 0
        i = 0
        while (i<len(incomes)):
            income = incomes[i].split(',')
            dates = income[0].split('-')
            year = int(dates[0])
            month = int(dates[1])
            if (year==lastYear and month==lastMonth):
                lastMonthIncome = lastMonthIncome + float(income[1])
            i=i+1
        return str(lastMonthIncome)
    
    def getThisMonthOutcome(self,name):
        outcomeFile = open(name+"_outcome.csv","r")
        outcomes = outcomeFile.readlines()
        outcomeFile.close

        nowDate = date.today()
        nowDate = str(nowDate).split('-')
        nowYear = nowDate[0]
        nowMonth = nowDate[1]

        thisMonthOutcome = 0
        i = 0
        while (i<len(outcomes)):
            outcome = outcomes[i].split(',')
            dates = outcome[0].split('-')
            year = dates[0]
            month = dates[1]
            if (year==nowYear and month==nowMonth):
                thisMonthOutcome = thisMonthOutcome + float(outcome[1])
            i=i+1
        return str(thisMonthOutcome)
    
    def getLastMonthOutcome(self,name):
        outcomeFile = open(name+"_outcome.csv","r")
        outcomes = outcomeFile.readlines()
        outcomeFile.close

        nowDate = date.today()
        nowDate = str(nowDate).split('-')
        nowYear = int(nowDate[0])
        nowMonth = int(nowDate[1])
        if (nowMonth==1):
            lastMonth = 12
            lastYear = nowYear - 1
        else:
            lastMonth = nowMonth - 1
            lastYear = nowYear

        lastMonthOutcome = 0
        i = 0
        while (i<len(outcomes)):
            outcome = outcomes[i].split(',')
            dates = outcome[0].split('-')
            year = int(dates[0])
            month = int(dates[1])
            if (year==lastYear and month==lastMonth):
                lastMonthOutcome = lastMonthOutcome + float(outcome[1])
            i=i+1
        return str(lastMonthOutcome)

    def showBalancesMenu(self, errorInput,username):
        menu = Menu.Menu()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================== MONEY TRACKING APP ========================")
        print("============================= BALANCES =============================")
        if errorInput:
            print('!! Your input is not valid. Please try again. !!\n')

        print("Your Balance\t\t\t: Rp. "+ self.getCurrentBalance(username))
        print("Your Expanses (this Month)\t: -Rp. "+ self.getThisMonthOutcome(username))
        print("Your Expanses (last Month)\t: -Rp. "+ self.getLastMonthOutcome(username))
        print("Your Income (this Month)\t: +Rp. "+ self.getThisMonthIncome(username))
        print("Your Income (lasr Month)\t: +Rp. "+ self.getLastMonthIncome(username))
        print("1. Input Income\n2. Input Expanse\n3. Back")
        print("====================================================================")
        option = input("Your Input :")
        if (option=='1'):
            self.showInputIncome(False,username)
        elif(option=='2'):
            self.showInputExpanse(False,username)
        elif(option=='3'):
            menu.showMenu(username,False)
        else:
            self.showBalancesMenu(True,username)
    
    def showInputIncome(self, errorInput, username):
        tracker = inputData.MoneyTracker()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================== MONEY TRACKING APP ========================")
        print("========================== INPUT EXPANSE ===========================")
        if errorInput:
            print('!! Your input is not valid. Please try again. !!\n')
        amount = float(input("Enter income amount: "))
        date = inputData.get_valid_date_input("Enter a date (YYYY-MM-DD): ")
        notes = input("Enter the notes (leave - if no notes):")
        print("1. Submit\n2. Back and Cancel")
        print("====================================================================")
        option = input("Your Input :")
        if (option=='1'):
            tracker.add_transaction(username, amount, 'Income', 'Income', date, notes)
            self.showBalancesMenu(False,username)
        elif (option=='2'):
            self.showBalancesMenu(False,username)
        else:
            self.showInputIncome(True,username)
    
    def showInputExpanse(self, errorInput, username):
        tracker = inputData.MoneyTracker()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================== MONEY TRACKING APP ========================")
        print("========================== INPUT EXPANSE ===========================")
        if errorInput:
            print('!! Your input is not valid. Please try again. !!\n')
        amount = float(input("Enter expense amount: "))
        date = inputData.get_valid_date_input("Enter a date (YYYY-MM-DD): ")
        category = tracker.categoryPicking()
        notes = input("Enter the notes (leave - if no notes): ")
        print("1. Submit\n2. Back and Cancel")
        print("====================================================================")
        option = input("Your Input :")
        if (option=='1'):
            tracker.add_transaction(username, amount, 'Expense', category, date, notes)
            self.showBalancesMenu(False,username)
        elif (option=='2'):
            self.showBalancesMenu(False,username)
        else:
            self.showInputExpanse(True,username)