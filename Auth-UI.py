def signIn(eCond,inUser,regCondition,logCondition):
    print("======================== MONEY TRACKING APP ========================")
    print("============================= SIGN IN ==============================")
    if (eCond==True) :
        print("!! Username/Password salah, silahkan input kembali !!")
        print("!! Jika belum memiliki akun, silahkan melakukan registrasi !!")
    inUser = input("Apakah anda sudah meniliki akun?(y/n)(0 to exit) :")
    if (inUser=="y"):
        username = input("Username\t:")
        password = input("Password\t:")
        print ("1.Submit\n2. Exit")
        print("====================================================================")
        inUser = input("\nInput :")
    elif (inUser=="n") :
        print("====================================================================")
        regCondition = True
        logCondition = False

def signIn(eCond,inUser,regCondition,logCondition):
    print("======================== MONEY TRACKING APP ========================")
    print("============================= SIGN UP ==============================")
    if (eCond==True) :
        print("!! Username sudah ada, gunakan username lain / lakukan log in !!")
    username = input("Username\t:")
    if (username=="username yang ada di database"):
        regCondition = True
        eCond = True
    else :
        regCondition = False
        logCondition = True
    password = input("Password\t:")
    print ("1.Submit\n2. Exit")
    print("====================================================================")
    inUser = input("\nInput :")
