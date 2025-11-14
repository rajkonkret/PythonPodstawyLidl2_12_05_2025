from datetime import datetime, date, timedelta

today = date.today()
print(today)  # 2025-11-14
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2025-11-14 09:34:13.974935

print(time.year)  # 2025
print(time.day)  # 14

formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 14/11/2025
print(type(formated_date))  # <class 'str'>

object_time = datetime.now().strptime("14/11/2025", "%d/%m/%Y")
print(object_time)  # 2025-11-14 00:00:00
print(type(object_time))  # <class 'datetime.datetime'>

# 3 TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# tomorrow = today + 1
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2025-11-15

print(35 * "-")
products = [
    {"sku": 1, "exp_date": today, "price": 200},
    {"sku": 2, "exp_date": today, "price": 100},
    {"sku": 3, "exp_date": tomorrow, "price": 300},
    {"sku": 4, "exp_date": today, "price": 49.99},
    {"sku": 5, "exp_date": today, "price": 199.99},
]
