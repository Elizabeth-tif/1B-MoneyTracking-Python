import os

class Auth:
    def __init__(self):
        self.users = []

    # Mengecek apakah file users.csv sudah dibuat atau belum
    def check_file(self):
        try:
            open('./Storage/users.csv', 'r')
            return True
        except FileNotFoundError:
            return False
        
    # Fungsi tambahan untuk login. Mengecek apakah username 
    # dan password sesuai dengan yang ada di file users.csv
    def check_user(self, username, password):
        with open('./Storage/users.csv', 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                if data[0] == username and data[1] == password:
                    return True
        return False

    # Fungsi untuk login, apabila berhasil akan mengembalikan username
    def login(self, errorAuth, errorInput):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('======================== MONEY TRACKING APP ========================')
        print('============================= SIGN IN ==============================')
        if errorInput:
            print('!! Your input is not valid. Please try again. !!\n')
        if errorAuth:
            print('!! Username or Password is incorrect. Please try again. !!\n')
        
        if self.check_file():
            option = input('Have an account? (y/n): ')

            if option == 'y':
                username = input('Enter your username: ')
                password = input('Enter your password: ')
                print ("1. Submit\n2. Exit")
                print('====================================================================')
                option = input("Your Input :")
                if option == '1':
                    loggedIn = self.check_user(username, password)
                elif option == '2':
                    exit()
                else:
                    username = self.login(False,True)
                if loggedIn:
                    print('Logged in successfully!')
                else:
                    username = self.login(True,False)
            elif option == 'n':
                self.signup(False,False)
                username = self.login(False,False)
            else:
                username = self.login(False,True)
        else:
            self.signup(False,False)
            username = self.login(False,False)
        return username

    # Fungsi untuk signup
    def signup(self, errorAuth, errorInput):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('======================== MONEY TRACKING APP ========================')
        print('============================= SIGN UP ==============================')    
        if errorInput:
            print('!! Your input is not valid. Please try again. !!\n')
        if errorAuth:
            print('!! Username already exists !!\n')
        
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        print ("1. Submit\n2. Back")
        print('====================================================================')
        option = input("Your Input :")
        if option == '1':
            self.add_user(username, password)
        elif (option!= '2' or option!='1'):
            self.signup(False,True)
        

    # Fungsi untuk menambahkan user baru ke dalam file
    def add_user(self, username, password):
        user = {
            'username': username,
            'password': password
        }

        try:
            # Check if username already exists
            with open('./Storage/users.csv', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(',')
                    if data[0] == username:
                        self.signup(True,False)
                        return
            
            print('users.csv found. Appending new user...')
            # Append users to list and file
            self.users.append(user)
            with open('./Storage/users.csv', 'a') as file:
                file.write(f'{username},{password}\n')
        except FileNotFoundError:
            print('users.csv not found. Creating new file...')
            # Append users to list and file
            self.users.append(user)
            with open('./Storage/users.csv', 'a') as file:
                file.write(f'{username},{password}\n')