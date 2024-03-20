def budgetTarget(eCond,inUser):
    print("======================== MONEY TRACKING APP ========================")
    print("========================== BUDGET & TARGET =========================")
    if (eCond==True) :
        print("!! Input tidak valid, silahkan melakukan input ulang !!")
    print("~TARGET~")
    print("\tYearly : Rp. "+ "0" + ",00 / Rp. " + "0"+ ",00")
    print("\tMonthly : Rp. "+ "0" + ",00 / Rp. " + "0"+ ",00")
    
    print("\n~TARGET~")
    #show budget in every categories with this format : #category + ": Rp. "+ "0" + ",00 / Rp. " + "0"+ ",00"
    print("\n1. Add/Update Target\n2. Add/Update Budget Limit\n3. Back")
    print("====================================================================")
    inUser = input("\nInput :")

def Target(eCond,inUser):
    print("======================== MONEY TRACKING APP ========================")
    print("============================== TARGET ==============================")
    if (eCond==True) :
        print("!! Input tidak valid, silahkan melakukan input ulang !!")
    inTarget = input ("Enter Target :")
    print ("1.Submit\n2. Back and Cancel")
    print("====================================================================")
    inUser = input("\nInput :")

def Budget(eCond,inUser):
    print("======================== MONEY TRACKING APP ========================")
    print("=========================== BUDGET LIMIT ===========================")
    if (eCond==True) :
        print("!! Input tidak valid, silahkan melakukan input ulang !!")
    print("Categories\t")
    print("\t1. a\n\t2. b\n\t3. c\n\t4. d")
    category = input("Input Category :")
    budgetLimit = input("Enter Budget :")
    print ("1.Submit\n2. Back and Cancel")
    print("====================================================================")
    inUser = input("\nInput :")