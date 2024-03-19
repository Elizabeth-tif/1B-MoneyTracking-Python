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
                    data = line.strip().split(',')
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
