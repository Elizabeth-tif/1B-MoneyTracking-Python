import datetime
import selectFile
import csv

#Sebuah function untuk input date yang valid
def get_valid_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            # Attempt to parse the input string into a date object
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return date_obj
        except ValueError:
            # If parsing fails, inform the user and prompt again
            print("Invalid date format. Please enter date in YYYY-MM-DD and valid date format.")

#class moneyTracker
class MoneyTracker:
    def __init__(self):
        self.transactions = []
    #Sebuah method untuk menambahkan transaksi baru, baik income atau outcome
    def add_transaction(self, name, amount, transaction_type, category, date, notes):
        if date is None:
            date = datetime.date.today()
        transaction = {
            'name': name,
            'amount': amount,
            'type': transaction_type,
            'category': category,
            'date': date,
            'notes': notes
        }
        self.transactions.append(transaction)
        self.saveToFile(transaction)
        
    def saveToFile(self, object):
        transaction = object
        #append transaction ke file transaction.csv
        with open("transaction.csv","a") as file:
            file.write(f"{transaction['name']},{transaction['type']},{transaction['date']},{transaction['amount']},{transaction['category']},{transaction['notes']}\n")

        #Variable untuk mengecek apakah suatu date sudah ada di income.csv atau outcome.csv
        exists = False
        # menggunakan try-except untuk handle error jika file tidak ditemukan
        try:
            with open("income.csv" if transaction['type'] == 'Income' else "outcome.csv", "r+") as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    data = line.split(',')
                    if data[0] == transaction['name'] and data[1] == (transaction['date']):
                        exists = True
                        new_amount = float(data[2]) + transaction['amount']
                        line = f"{data[0]},{data[1]},{new_amount}\n"
                    file.write(line)

        except FileNotFoundError:
            exists=False

        # Jika transaksi dengan date sama tidak ditemukan, maka append ke file income/outcome
        if not exists:
            with open("income.csv" if transaction['type'] == 'Income' else "outcome.csv", "a") as file:
                file.write(f"{transaction['name']},{transaction['date']},{transaction['amount']}\n")

    # Fungsi dibawah ini untuk memilih kategori untuk outcome 
    def categoryPicking(self):
        print("Expenses Category\n(1) Gadget\n(2) Kebutuhan Pokok\n(3) Hiburan\n(4) Kesehatan\n(5) Makanan & Minuman\n(6) Pendidikan\n(7) Transportasi")
        while True:
            choice = input("Select expenses category:")
            if choice == '1':
                return 'gadget'
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
                return 'transportasi'
            else:
                print("Invalid choice. Please select a valid category.")

    #sebuah function untuk update file transaction.csv berdasarkan hasil import file
    def updateTransaction(self):
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
                    if len(data) == 6:  # Mengecek barisnya memiliki semua value yang diminta
                        transaction = {
                            'name': data[0],
                            'type': data[1],
                            'date': data[2],
                            'amount': float(data[3]),
                            'category': data[4],
                            'notes': data[5]
                        }
                        self.saveToFile(transaction)
                    else:
                        print("file has to include all transaction elements : name,type,date,amount,category,notes")

            except Exception as e:
                print("Error reading the file:", e)
        else:
            print("No file selected.")
    #function untuk make sure membuat file agar menghindari error di beberapa function/prosedur lain
    def createFile(self):
        with open('income.csv','a') as file:
            pass
        with open('outcome.csv','a') as file:
            pass
        with open('transaction.csv','a') as file:
            pass