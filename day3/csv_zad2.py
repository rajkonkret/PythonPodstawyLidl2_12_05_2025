import csv

# filename = "records.csv"
filename = "discount_dict.csv"
rows = []
with open(filename, "r", newline="") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)
    csv_f.seek(0)  # cofniecie an apoczątek pliku
    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)
    fields = next(csvreader)  # wyciaga jeden wierszz, ustawia wskaznik na nastepny

    for row in csvreader:
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'coe']
# Rows: [['Radek', 'coe', '3', '90']]
