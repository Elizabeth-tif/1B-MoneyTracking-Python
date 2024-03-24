import datetime
import csv
from tabulate import tabulate
from asciichartpy import plot

#class recap :
class recap:
    #sebuah function untuk menampilkan recap harian dalam 1 bulan
    def dailyRecap(self, user, bulan, tahun):
        #deklarasi array
        uniqueDate = []
        income = []
        outcome = []
        months = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]

        # Membaca data dari income.csv
        with open(user+'_income.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:           #untuk setiap baris dalam file
                date_obj = datetime.datetime.strptime(row[0], '%Y-%m-%d').date()    #parsing dari string menjadi date type
                obj = {
                    'date' : date_obj,
                    'amount' : float(row[1])    #parse string to float
                }
                income.append(obj)  #push object ke array income
                    
                if date_obj not in uniqueDate and date_obj.month == bulan and date_obj.year == tahun:
                    uniqueDate.append(date_obj)
        
        with open(user+'_outcome.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:       #untuk setiap baris dalam file
                date_obj = datetime.datetime.strptime(row[0], '%Y-%m-%d').date()
                obj = {
                    'date' : date_obj,
                    'amount' : float(row[1])
                }
                outcome.append(obj)     #push object ke array outcome
                if date_obj not in uniqueDate and date_obj.month == bulan and date_obj.year == tahun:
                    uniqueDate.append(date_obj)
        #sort uniqueDate
        uniqueDate.sort()
        # Sort array income dan outcome by date
        income = sorted(income, key=lambda x: x["date"])
        outcome = sorted(outcome, key=lambda x: x["date"])

         # Assemble data dari array unique dates, income, dan outcome
        recap_data = []
        for date in uniqueDate:
            income_amount = next((item['amount'] for item in income if item['date'] == date), 0)
            outcome_amount = next((item['amount'] for item in outcome if item['date'] == date), 0)
            total_amount = income_amount - outcome_amount
            recap_data.append({'date': date, 'income': income_amount, 'outcome': outcome_amount, 'total': total_amount})


        print("\nRekap Harian di Bulan",months[bulan-1],"Tahun",tahun)
        # Cek apabila recap_data kosong
        if not recap_data:
            # Print pesan bahwa tidak ada transaksi apabila kosong
            message_table = tabulate([["Tidak ada data transaksi pada bulan dan tahun ini"]], tablefmt="pretty")
            print(message_table)
        else:
            # mengkonversi recap_data menjadi format table dengan tabulate
            table = tabulate(recap_data, headers="keys", tablefmt="pretty")
            print(table)

    def weeklyRecap(self, user, tahun):
        income = []
        outcome = []
        uniqueWeek = []
        recap_data = []
        with open(user+'_income.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                name = row[0].strip()
                isoDate = datetime.datetime.strptime(row[0], '%Y-%m-%d').date().isocalendar()
                obj = {
                    'week' : isoDate.week,
                    'amount' : float(row[1])
                }
                income.append(obj)

                if isoDate.week not in uniqueWeek and isoDate.year == tahun:
                    uniqueWeek.append(isoDate.week)

        with open(user+'_outcome.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                name = row[0].strip()
                isoDate = datetime.datetime.strptime(row[0], '%Y-%m-%d').date().isocalendar()
                obj = {
                    'week' : isoDate.week,
                    'amount' : float(row[1])
                }
                outcome.append(obj)

                if isoDate.week not in uniqueWeek and isoDate.year == tahun:
                    uniqueWeek.append(isoDate.week)
        
        uniqueWeek.sort()
        income = sorted(income, key=lambda x: x["week"])
        outcome = sorted(outcome, key=lambda x: x["week"])

        for week in uniqueWeek:
            startOfWeek, endOfWeek = recap.getWeekRange(tahun, week)
            weekRange = f"{startOfWeek} - {endOfWeek}"
            income_amount = sum(item['amount'] for item in income if item['week'] == week)
            outcome_amount = sum(item['amount'] for item in outcome if item['week'] == week)
            total_amount = income_amount - outcome_amount
            recap_data.append({'week': week, 'date': weekRange, 'income': income_amount, 'outcome': outcome_amount, 'total': total_amount})

        print("\nRekap Mingguan di Tahun",tahun)
        if not recap_data:
            message_table = tabulate([["Tidak ada data transaksi pada tahun ini"]], tablefmt="pretty")
            print(message_table)
        else:
            table = tabulate(recap_data, headers="keys", tablefmt="pretty")
            print(table)
        
    def getWeekRange(year, week):
        # Find the first day of the year
        firstDay = datetime.datetime(year, 1, 1)

        # Calculate the start of the week
        # startOfYear = firstDay - datetime.timedelta(days = firstDay.weekday())
        startOfWeek = firstDay + datetime.timedelta(weeks = week - 1)

        # Calculate the end of the week
        if week == 1:
            endOfWeek = startOfWeek + datetime.timedelta(days = 6 - startOfWeek.weekday())
        elif week == 53:
            endOfWeek = datetime.datetime(year, 12, 31)
        else:
            endOfWeek = startOfWeek + datetime.timedelta(days = 6)

        return startOfWeek.date(), endOfWeek.date()
    
    def monthRecap(self, user, tahun):
        #deklarasi array
        uniqueMonth = []
        income = []
        outcome = []
        months = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]

        # Membaca data dari income.csv
        with open(user+'_income.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:           #untuk setiap baris dalam file
                    date_obj = datetime.datetime.strptime(row[0], '%Y-%m-%d').date()    #parsing dari string menjadi date type
                    obj = {
                        'date' : date_obj,
                        'amount' : float(row[1])    #parse string to float
                    }
                    income.append(obj)  #push object ke array income
        # Membaca data dari outcome.csv
        with open(user+'_outcome.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:       #untuk setiap baris dalam file
                    date_obj = datetime.datetime.strptime(row[0], '%Y-%m-%d').date()
                    obj = {
                        'date' : date_obj,
                        'amount' : float(row[1])
                    }
                    outcome.append(obj)     #push object ke array outcome
        #sort months
        uniqueMonth = list(set([item['date'].month for item in income + outcome]))
        uniqueMonth.sort()
        # Sort array income dan outcome berdasarkan date
        income = sorted(income, key=lambda x: x["date"])
        outcome = sorted(outcome, key=lambda x: x["date"])

         # Assemble data dari array unique months, income, dan outcome
        recap_data = []
        for month in uniqueMonth:
            income_amount = sum([item['amount'] for item in income if item['date'].month == month])
            outcome_amount = sum([item['amount'] for item in outcome if item['date'].month == month])
            total_amount = income_amount - outcome_amount
            recap_data.append({'month': months[month-1], 'income': income_amount, 'outcome': outcome_amount, 'total': total_amount})

        #rekap bulanan
        print("\nRekap Bulanan Tahun",tahun)
        # Cek apabila recap_data kosong
        if not recap_data:
            # Print pesan bahwa tidak ada transaksi apabila kosong
            message_table = tabulate([["Tidak ada data transaksi pada tahun ini"]], tablefmt="pretty")
            print(message_table)
        else:
            # mengkonversi recap_data menjadi format table dengan tabulate
            table = tabulate(recap_data, headers="keys", tablefmt="pretty")
            print(table) 