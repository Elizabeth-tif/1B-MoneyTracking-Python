import Features.TransactionHistory as TransactionHistory
import os

history = TransactionHistory.History()

def histori(user):
    os.system('cls')
    print("======================== MONEY TRACKING APP ========================")
    print("======================= TRANSACTION  HISTORY =======================")
    history.TransHist(user)
    print("====================================================================")
    input("input anything to go back :")