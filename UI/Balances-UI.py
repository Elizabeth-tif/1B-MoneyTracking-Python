def balancesUi(eCond,inUser):
    print("======================== MONEY TRACKING APP ========================")
    print("============================= BALANCES =============================")
    if (eCond==True) :
        print("!! Input tidak valid, silahkan melakukan input ulang !!")
    balance ="Rp."+ "0" +",00" #"0" diisi oleh data yang sudah ada di file, jika belum ada, defult valuenya = 0
    expansesThisM ="Rp."+ "0" +",00" #"0" diisi oleh data yang sudah ada di file, jika belum ada, defult valuenya = 0
    expansesLastM ="Rp."+ "0" +",00" #"0" diisi oleh data yang sudah ada di file, jika belum ada, defult valuenya = 0
    incomeThisM ="Rp."+ "0" +",00" #"0" diisi oleh data yang sudah ada di file, jika belum ada, defult valuenya = 0
    incomeLastM ="Rp."+ "0" +",00" #"0" diisi oleh data yang sudah ada di file, jika belum ada, defult valuenya = 0
    print("Your Balance\t\t\t:"+balance)
    print("Your Expenses (this Month)\t:"+expansesThisM)
    print("Your Expenses (last Month)\t:"+expansesLastM)
    print("Your Income (this Month)\t:"+incomeThisM)
    print("Your Income (last Month)\t:"+incomeLastM)
    print("====================================================================")
    inUser = input("\nInput :")

def inputIncome(eCond,inUser):
    print("======================== MONEY TRACKING APP ========================")
    print("=========================== INPUT INCOME ===========================")
    if (eCond==True) :
        print("!! Input tidak valid, silahkan melakukan input ulang !!")
    income = input("Income\t:")
    date = input("Date\t:")
    notes = input("Notes\t:")
    print("1. Submit\n2. Back and Cancel")
    print("====================================================================")
    inUser = input("\nInput :")

def inputOutcome(eCond,inUser):
    print("======================== MONEY TRACKING APP ========================")
    print("========================== INPUT EXPENSE ===========================")
    if (eCond==True) :
        print("!! Input tidak valid, silahkan melakukan input ulang !!")
    income = input("Income\t\t:")
    date = input("Date\t\t:")
    print("Categories\t")
    print("\t1. a\n\t2. b\n\t3. c\n\t4. d")
    category = input("Input Category\t:")
    notes = input("Notes\t\t:")
    print("1. Submit\n2. Back and Cancel")
    print("====================================================================")
    inUser = input("\nInput :")
inputOutcome(True,3)
