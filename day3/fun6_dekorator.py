# generator
import time


def kwadrat(x):
    for i in range(x):
        print(i ** 2)


kwadrat(5)


def kwadrat2(x):
    for i in range(x):
        yield i ** 2


kwa = kwadrat2(5)
print(next(kwa))
print(next(kwa))
print(next(kwa))
print("Zrób cokolwiek")
print(next(kwa))
print(next(kwa))
try:
    print(next(kwa))  # StopIteration, koniec danych
except StopIteration:
    print("Koniec danych")

for i in kwadrat2(5):
    print(i)
    time.sleep(1)
