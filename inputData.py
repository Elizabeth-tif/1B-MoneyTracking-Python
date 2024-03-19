import datetime
import selectFile

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
    def add_transaction(self, amount, transaction_type, category, date, notes):
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
        
        #append transaction ke file transaction.csv
        with open("transaction.csv","a") as file:
            file.write(f"{transaction['type']},{transaction['date']},{transaction['amount']},{transaction['category']},{transaction['notes']}\n")

        #Variable untuk mengecek apakah suatu date sudah ada di income.csv atau outcome.csv
        exists = False
        # menggunakan try-except untuk handle error jika file tidak ditemukan
        try:
            with open("income.csv" if transaction_type == 'Income' else "outcome.csv", "r+") as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:

                    data = line.split(',')
                    if data[0] == str(date):
                        exists = True
                        new_amount = float(data[1]) + amount
                        line = f"{data[0]},{new_amount}\n"
                    file.write(line)

        except FileNotFoundError:
            exists=False

        # Jika transaksi dengan date sama tidak ditemukan, maka append ke file income/outcome
        if not exists:
            with open("income.csv" if transaction_type == 'Income' else "outcome.csv", "a") as file:
                file.write(f"{transaction['date']},{transaction['amount']}\n")

    #Fungsi dibawah ini untuk memilih kategori untuk outcome 
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
                # Open the selected file for reading
                with open(file_path, 'r') as file:
                    # Read the contents of the file
                    file_content = file.read()
                # Split the content by line
                lines = file_content.strip().split('\n')
                for line in lines:
                    # Split the line by comma and check if it contains all expected values
                    data = line.strip().split(',')
                    if len(data) == 5:  # Ensure the line has all expected values
                        transaction = {
                            'type': data[0],
                            'date': data[1],
                            'amount': data[2],
                            'category': data[3],
                            'notes': data[4]
                        }
                        with open('transaction.csv','a') as append_file:
                            append_file.write(f"{transaction['type']},{transaction['date']},{transaction['amount']},{transaction['category']},{transaction['notes']}\n")
                    else:
                        print("file has to include all transaction elements : type,date,amount,category,notes")

            except Exception as e:
                print("Error reading the file:", e)
        else:
            print("No file selected.")

