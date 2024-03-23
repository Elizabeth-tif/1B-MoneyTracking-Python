import datetime
import selectFile
import importlib
import subprocess

#Sebuah function untuk input date yang valid
def get_valid_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            # Attempt to parse the input string into a date object
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            date_now = datetime.date.today()
            if(date_obj.year<2020 or date_obj>date_now):
                print('Tolong masukkan tanggal minimum 2020-1-1 dan maximum',date_now)
            else:
                return date_obj
        except ValueError:
            # If parsing fails, inform the user and prompt again
            print("Invalid date format. Please enter date in YYYY-MM-DD and valid date format.")

#a function to automatically install tabulate library, so it won't show any error
def check_install_tabulate():
    try:
        importlib.import_module('tabulate')
    except ImportError:
        subprocess.check_call(['pip', 'install', 'tabulate'])
check_install_tabulate()

#class moneyTracker
class MoneyTracker:
    def __init__(self):
        self.transactions = []
    #Sebuah method untuk menambahkan transaksi baru, baik income atau outcome
    def add_transaction(self, user, amount, transaction_type, category, date, notes):
        if date is None:
            date = datetime.date.today()
        transaction = {
            'amount': amount,
            'type': transaction_type,
            'category': category,
            'date': date,
            'notes': notes
        }
        self.transactions.append(transaction)
        self.saveToFile(transaction, user)
        
    def saveToFile(self, object, user):
        transaction = object
        #append transaction ke file transaction.csv
        with open(user+"_transaction.csv","a") as file:
            file.write(f"{transaction['type']},{transaction['date']},{transaction['amount']},{transaction['category']},{transaction['notes']}\n")

        #Variable untuk mengecek apakah suatu date sudah ada di income.csv atau outcome.csv
        exists = False
        # menggunakan try-except untuk handle error jika file tidak ditemukan
        try:
            with open(user+"_income.csv" if transaction['type'] == 'Income' else user+"_outcome.csv", "r+") as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    data = line.split(',')
                    date_obj = datetime.datetime.strptime(data[0], '%Y-%m-%d').date()
                    if  date_obj == (transaction['date']):
                        exists = True
                        new_amount = float(data[1]) + transaction['amount']
                        line = f"{data[0]},{new_amount}\n"
                    file.write(line)

        except FileNotFoundError:
            exists=False

        # Jika transaksi dengan date sama tidak ditemukan, maka append ke file income/outcome
        if not exists:
            with open(user+"_income.csv" if transaction['type'] == 'Income' else user+"_outcome.csv", "a") as file:
                file.write(f"{transaction['date']},{transaction['amount']}\n")

    # Fungsi dibawah ini untuk memilih kategori untuk outcome 
    def categoryPicking(self):
        print("Expenses Category\n(1) Gadget\n(2) Kebutuhan Pokok\n(3) Hiburan\n(4) Kesehatan\n(5) Makanan & Minuman\n(6) Pendidikan\n(7) Transportasi")
        while True:
            choice = input("Select expenses category:")
            if choice == '1':
                return 'Gadget'
            elif choice == '2':
                return 'Kebutuhan Pokok'
            elif choice == '3':
                return 'Hiburan'
            elif choice == '4':
                return 'Kesehatan'
            elif choice == '5':
                return 'Makanan & Minuman'
            elif choice == '6':
                return 'Pendidikan'
            elif choice == '7':
                return 'Transportasi'
            else:
                print("Invalid choice. Please select a valid category.")

    #sebuah function untuk update file transaction.csv berdasarkan hasil import file
    def updateTransaction(self, user):
        file_path = selectFile.select_file_and_read()
        if file_path:
            print("Selected file:", file_path)
            try:
                # Buka file yang dipilih untuk dibaca
                with open(file_path, 'r') as file:
                    # Baca konten atau isi dari file
                    file_content = file.read()
                # Split konten menjadi baris baris
                lines = file_content.strip().split('\n')
                for line in lines:
                    # Split baris dengan koma dan pengecekan apakah dalam 1 baris memiliki semua value yang diminta
                    data = line.strip().split(',')
                    if len(data) == 5:  # Mengecek barisnya memiliki semua value yang diminta
                        transaction = {
                            'type': data[0],
                            'date': datetime.datetime.strptime(data[1], '%Y-%m-%d').date(),
                            'amount': float(data[2]),
                            'category': data[3],
                            'notes': data[4]
                        }
                        self.saveToFile(transaction, user)
                    else:
                        print("file has to include all transaction elements : type,date,amount,category,notes")

            except Exception as e:
                print("Error reading the file:", e)
        else:
            print("No file selected.")
    #function untuk make sure membuat file agar menghindari error di beberapa function/prosedur lain
    def createFile(self, user):
        with open(user+'_income.csv','a') as file:
            pass
        with open(user+'_outcome.csv','a') as file:
            pass
        with open(user+'_transaction.csv','a') as file:
            pass