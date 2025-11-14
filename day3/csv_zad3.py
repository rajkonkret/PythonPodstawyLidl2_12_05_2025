import pandas

# data = pandas.read_csv("records.csv")
data = pandas.read_csv("discount_dict.csv", delimiter=";")
print(data)
#    sku  exp_date   price
# 0    1     today  200.00
# 1    2     today  100.00
# 2    3  tomorrow  300.00
# 3    4     today   49.99
# 4    5     today  199.99

print(data.columns)
# Index(['sku', 'exp_date', 'price'], dtype='object')
