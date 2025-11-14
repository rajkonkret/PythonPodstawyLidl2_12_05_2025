# funkcja lambda
# skrócony zapis funkcji
# return
from functools import reduce


def odejmij(a, b):
    return a - b


print(odejmij(3, 1))  # 2

odejmij2 = lambda a, b: a - b
print(odejmij2(6, 9))  # -3

wiek = lambda x: "dziecka" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(10))  # nastolatek
print(wiek(18))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 4, 35, 55, 60, 100, 500]
l1 = []
for i in lista:
    l1.append(i * 2)
print(l1)

print([i * 2 for i in lista])  # [2, 4, 6, 8, 70, 110, 120, 200, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 6, 8, 70, 110, 120, 200, 1000]

# map() - modyfikuje dane sposobem jaki poda funkcja
print(f"Zastosowanie map: {list(map(zmien, lista))}")
# Zastosowanie map: [2, 4, 6, 8, 70, 110, 120, 200, 1000]
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map: {list(map(lambda x: x * 3, lista))}")
print(f"Zastosowanie map: {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map: {list(map(lambda x: x * 1.5, lista))}")
# Zastosowanie map: [2, 4, 6, 8, 70, 110, 120, 200, 1000]
# Zastosowanie map: [3, 6, 9, 12, 105, 165, 180, 300, 1500]
# Zastosowanie map: [4, 8, 12, 16, 140, 220, 240, 400, 2000]
# Zastosowanie map: [1.5, 3.0, 4.5, 6.0, 52.5, 82.5, 90.0, 150.0, 750.0]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 5:
        l3.append(i)
print(l3)  # [1, 2, 3, 4]

# filter()
# Zastosowanie filter: [1, 2, 3, 4]
print(f"Zastosowanie filter: {list(filter(lambda x: x < 5, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x > 5 and x < 100, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: 5 < x < 100, lista))}")

#  calculates ((((1 + 2) + 3) + 4) + 5)
print(reduce(lambda a, b: a + b, [1, 2, 3, 4, 5]))  # 15
