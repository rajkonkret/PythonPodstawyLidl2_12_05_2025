# pliki csv
# dane oddzielone separatorem ,;tabspac

import csv

fields = ['name', 'branch', "year", "coe"]
row = ["Radek", "coe", "3", 90]

filename = "records.csv"

# newline="" - ominiecie problemu pustego wiersza
with open(filename, "w", newline="") as fh:
    csvwriter = csv.writer(fh)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

products = [
    {"sku": 1, "exp_date": "today", "price": 200},
    {"sku": 2, "exp_date": "today", "price": 100},
    {"sku": 3, "exp_date": "tomorrow", "price": 300},
    {"sku": 4, "exp_date": "today", "price": 49.99},
    {"sku": 5, "exp_date": "today", "price": 199.99},
]
fields_list = [j for j in products[0]]
print(fields_list)  # ['sku', 'exp_date', 'price']

filename = "discount_dict.csv"
with open(filename, "w", newline="") as fh:
    csvwriter = csv.DictWriter(fh, fieldnames=fields_list, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products)
