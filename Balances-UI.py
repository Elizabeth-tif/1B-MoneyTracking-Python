def balancesUi(eCond,inUser):
    balance ="Rp."+ "0" +",00" #"0" diisi oleh data yang sudah ada di file, jika belum ada, defult valuenya = 0
    expansesThisM ="Rp."+ "0" +",00" #"0" diisi oleh data yang sudah ada di file, jika belum ada, defult valuenya = 0
    expansesLastM ="Rp."+ "0" +",00" #"0" diisi oleh data yang sudah ada di file, jika belum ada, defult valuenya = 0
    incomeThisM ="Rp."+ "0" +",00" #"0" diisi oleh data yang sudah ada di file, jika belum ada, defult valuenya = 0
    incomeLastM ="Rp."+ "0" +",00" #"0" diisi oleh data yang sudah ada di file, jika belum ada, defult valuenya = 0
    print("======================== MONEY TRACKING APP ========================")
    print("============================= BALANCES =============================")
    if (eCond==True) :
        print("!! Input tidak valid, silahkan melakukan input ulang !!")
    print("Your Balance\t\t\t:"+balance)
    print("Your Expanses (this Month)\t:"+expansesThisM)
    print("Your Expanses (lasr Month)\t:"+expansesLastM)
    print("Your Income (this Month)\t:"+incomeThisM)
    print("Your Income (lasr Month)\t:"+incomeLastM)
    print("====================================================================")
    inUser = input("\nInput :")

balancesUi(True,3)
