import datetime
import csv
from tabulate import tabulate

class History:
    def TransHist(self, user):
        uniqueData = []
        with open('transaction.csv', 'r') as readcsv:
            csvreader = csv.reader(readcsv)
            for row in csvreader:
                name = row[0].strip()
                if name == user:
                    try:
                        date_obj = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
                        obj = {
                            'date' : date_obj,
                            'type' : row[1], # 'type' : 'Income' or 'Expense'
                            'amount' : float(row[3]),
                            'category' : row[4],
                            'note' : row[5]
                        }
                        uniqueData.append(obj)
                    except ValueError:
                        # Error Handling apabila tanggal tidak sesuai dengan format YYYY-MM-DD
                        continue
        
        # Sort uniqueData berdasarkan tanggal
        uniqueData.sort(key=lambda x: x['date']) 

        history_data = []
        #append data ke history_data
        for item in uniqueData:
            history_data.append({
                'type': item['type'],
                'date': item['date'],
                'amount': item['amount'],
                'category': item['category'],
                'note': item['note']
            })

        print("\nTransaction History")

        # Cek apabila history_data kosong
        if not history_data:
            message_table = tabulate([["Tidak ada data Transaksi"]], tablefmt="pretty")
            print(message_table)
        else:
            table = tabulate(history_data, headers="keys", tablefmt="pretty")
            print(table)
