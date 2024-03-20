import os

class User:
    def __init__(self):
        self.users = []

    # Mengecek apakah file users.csv sudah dibuat atau belum
    def check_file(self):
        try:
            open('users.csv', 'r')
            return True
        except FileNotFoundError:
            return False
        
    # Fungsi tambahan untuk login. Mengecek apakah username 
    # dan password sesuai dengan yang ada di file users.csv
    def check_user(self, username, password):
        with open('users.csv', 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                if data[0] == username and data[1] == password:
                    return True
        return False

    # Fungsi untuk login, apabila berhasil akan mengembalikan username
    def login(self, error):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('======================== MONEY TRACKING APP ========================')
        print('============================= SIGN IN ==============================')

        if error:
            print('Username or Password is incorrect. Please try again.\n')
        
        if self.check_file():
            option = input('Have an account? (y/n)(0 to exit): ')

            if option == 'y':
                username = input('Enter your username: ')
                password = input('Enter your password: ')
                print('====================================================================')
                loggedIn = self.check_user(username, password)
                if loggedIn:
                    print('Logged in successfully!')
                    return username
                else:
                    username = self.login(True)
                    return username
            elif option == 'n':
                self.signup(False)
            else:
                exit()
        else:
            self.signup(False)

    # Fungsi untuk signup
    def signup(self, error):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('======================== MONEY TRACKING APP ========================')
        print('============================= SIGN UP ==============================')    

        if error:
            print('Username already exists!\n')
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        print('====================================================================')
        self.add_user(username, password)

    # Fungsi untuk menambahkan user baru ke dalam file
    def add_user(self, username, password):
        user = {
            'username': username,
            'password': password
        }

        try:    
            # Check if username already exists
            with open('users.csv', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(',')
                    if data[0] == username:
                        self.signup(True)
                        return
            
            print('users.csv found. Appending new user...')
            # Append users to list and file
            self.users.append(user)
            with open('users.csv', 'a') as file:
                file.write(f'{username},{password}\n')
        except FileNotFoundError:
            print('users.csv not found. Creating new file...')
            # Append users to list and file
            self.users.append(user)
            with open('users.csv', 'a') as file:
                file.write(f'{username},{password}\n')