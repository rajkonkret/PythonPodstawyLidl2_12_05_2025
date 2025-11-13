import random

# operacja na liczbach pseudolosowych

# """Return random integer in range [a, b], including both end points.
#         """
print(random.randint(-100, 100))  # int, 60 od 1 do 100
print(random.randint(1, 100))  # int, 60 od 1 do 100
print(random.randrange(1, 100))  # od 1 do 99, int, 36
print(random.randrange(5))  # od 0 do 4, 3

print(random.random())  # float, 0.8188078113794693 od 0 do 0.9999999
print(random.random() * 7)  # float, 3.4683891199870778 od 0 do 6.9999999

lista = [67, 45, 22, 68, 69, 90, 42]
print(lista[random.randrange(len(lista))])  # element: 42

print(random.choice(lista))  # 45

lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)

wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
print(lista_kule)

print(random.choices(lista_kule, k=6))  # [23, 44, 23, 44, 28, 37], losowanie z powtórzeniami
print(random.sample(lista_kule, 6))
print(random.sample(lista_kule, k=6))
# [4, 35, 13, 42, 14, 28]
# [46, 19, 37, 23, 11, 35]
