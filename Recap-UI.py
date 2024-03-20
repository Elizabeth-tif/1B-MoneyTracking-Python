def recap(eCond,inUser):
    print("======================== MONEY TRACKING APP ========================")
    print("============================== RECAP ===============================")
    if (eCond==True) :
        print("!! Input tidak valid, silahkan melakukan input ulang !!")
    print("1. Daily\n2. Weekly\n3. Monthly\n4. Back")
    print("====================================================================")
    inUser = input("\nInput :")
recap(False,2)

def daily(eCond,inUser):
    print("======================== MONEY TRACKING APP ========================")
    print("============================ DAILY RECAP ===========================")
    if (eCond==True) :
        print("!! Input tidak valid, silahkan melakukan input ulang !!")
    inMonth = input("Input Month (1-12) :")
    print("Rekap Bulan "+ inMonth)
    #while (i<#banyaknyaData)
        #print(#date[i] + "|" + #income[i] + "|" + #outcome[i] + "|" + #total[i])
        #i++
    inUser = input("Back?(y/n) :")

def weekly(eCond,inUser):
    print("======================== MONEY TRACKING APP ========================")
    print("=========================== WEEKLY RECAP ===========================")
    if (eCond==True) :
        print("!! Input tidak valid, silahkan melakukan input ulang !!")
    #while (i<#banyaknyaData)
        #print(i+1 + ".) " + #weekNumber[i] + #date[i] + "|" + #income[i] + "|" + #outcome[i] + "|" + #total[i])
        #i++
    print("====================================================================")
    inUser = input("Back?(y/n) :")

def monthly(eCond,inUser):
    print("======================== MONEY TRACKING APP ========================")
    print("=========================== MONTHLY RECAP ==========================")
    if (eCond==True) :
        print("!! Input tidak valid, silahkan melakukan input ulang !!")
    inYear = input("Input Year(2000-2050) :")
    print("Rekap Tahun "+ inYear)
    #while (i<#banyaknyaData)
        #print(#month[i] + "|" + #income[i] + "|" + #outcome[i] + "|" + #total[i])
        #i++
    print("====================================================================")
    inUser = input("Back?(y/n) :")