import datetime
import csv

#class recap :
class recap:
    #a function to show daily recap per month
    def dailyRecap(self):
        # Read data from the CSV file
        uniqueDate = []
        # Read data from income.csv
        with open('income.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                date_obj = datetime.datetime.strptime(row[1], '%Y-%m-%d').date()
                if date_obj not in uniqueDate:
                    uniqueDate.append(date_obj)

        with open('outcome.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                date_obj = datetime.datetime.strptime(row[1], '%Y-%m-%d').date()
                if date_obj not in uniqueDate:
                    uniqueDate.append(date_obj)
        print(uniqueDate)

r = recap()
r.dailyRecap()

