import Recap
import os

rekap = Recap.recap()
def recap(user):
    status = True
    while(status):
        os.system('cls')
        print("======================== MONEY TRACKING APP ========================")
        print("============================== RECAP ===============================")
        print("1. Daily\n2. Weekly\n3. Monthly\n4. Back")
        print("====================================================================")
        inUser = input("\nInput :")
        if(inUser == '1'):
            daily(user)
        elif(inUser == '2'):
            weekly(user)
        elif(inUser == '3'):
            monthly(user)
        elif(inUser == '4'):
            status=False
        else:
            print("Input tidak valid!")

def daily(user):
    inMonth=1
    inYear=1
    wrong = False
    while(int(inMonth)>0 and int(inYear)>0):
        os.system('cls')
        print("======================== MONEY TRACKING APP ========================")
        print("============================ DAILY RECAP ===========================")
        if(wrong):
            print("Tolong input bulan dan tahun yang valid! (tahun 2020-2024)")
        inMonth = int(input("Input Bulan (1-12) :"))
        inYear = int(input("Input tahun: "))
        if((inMonth<0 or inMonth>12) or inYear<2020 or inYear>2024):
            wrong=True
        else:
            break
    rekap.dailyRecap(user, inMonth, inYear)
    inUser = input('Melihat recap harian lainnya? (y untuk yes, yang lain untuk tidak) = ')
    if(inUser=='y'):
        daily(user)

def weekly(user):
    inYear = 1
    wrong = False
    while(int(inYear)>0):
        os.system('cls')
        print("======================== MONEY TRACKING APP ========================")
        print("=========================== WEEKLY RECAP ===========================")
        if(wrong == True):
            print("Tolong input tahun dari range 2020-2024!")
        inYear = int(input("Input tahun: "))
        if(inYear<2020 or inYear>2024):
            wrong = True
        else:
            break
    rekap.weeklyRecap(user, inYear)
    inUser = input('Melihat recap weekly lainnya? (y untuk yes, yang lain untuk tidak) = ')
    if(inUser=='y'):
        weekly(user)

def monthly(user):
    inYear = 1
    wrong = False
    while(int(inYear)>0):
        os.system('cls')
        print("======================== MONEY TRACKING APP ========================")
        print("=========================== MONTHLY RECAP ==========================")
        if(wrong == True):
            print("Tolong input tahun dari range 2020-2024!")
        inYear = int(input("Input tahun: "))
        if(inYear<2020 or inYear>2024):
            wrong = True
        else:
            break
    print('rekap bulanan') #ubah dengan method rekap bulanan
    inUser = input('Melihat recap weekly lainnya? (y untuk yes, yang lain untuk tidak) = ')
    if(inUser=='y'):
        monthly(user)