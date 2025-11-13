# pętle - wykonanie kodu wielokrotnie
# for - iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)

for i in range(3):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    print("Test")
    # print(_)

for i in range(5):
    print(i * 2)
    print(i + 2)

lista_kule = list(range(1, 50))
lista_wynik = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)
# [3, 47, 4, 38, 27, 25]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzyste")
# 0 parzyste
# 2 parzyste
# 4 parzyste
# 6 parzyste
# 8 parzyste

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:
    if c > 4:
        print(c, "większe od 4")
    elif c == 4:
        print(c, "Równe 4")
    else:
        print(c, "Mniejsze od 4")
# 0 Mniejsze od 4
# 2 Mniejsze od 4
# 4 Równe 4
# 6 większe od 4
# 8 większe od 4

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -3):  # ujemny krok
    print(i)

for c in lista3:
    if c == 2:
        c += 1
        print("tylko dla c==2")
    print("Za każdym przejściem pętli")
print("Po zakończeniu pętli")
# Za każdym przejściem pętli
# tylko dla c==2
# Za każdym przejściem pętli
# Za każdym przejściem pętli
# Za każdym przejściem pętli
# Za każdym przejściem pętli
# Po zakończeniu pętli

imiona = ['Radek', "Tomek", "Zenek", "Ania"]
print(imiona)
print(type(imiona))

for p in imiona:
    print(p)

# 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate()
for i in enumerate(imiona):
    print(i)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

imiona = ['Radek', "Tomek", "Zenek", "Ania", "Marzena"]
wiek = [45, 65, 34, 27]

# Radek 45
# IndexError: list index out of range - dla różnych długosci list
# for i in imiona:
#     print(i, wiek[imiona.index(i)])
# Radek 45
# Tomek 65
# Zenek 34
# Ania 27

# zip() łączy kolekcje
for i in zip(imiona, wiek):
    print(i)
    # ('Radek', 45)
    # ('Tomek', 65)
    # ('Zenek', 34)
    # ('Ania', 27)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 45
# Tomek 65
# Zenek 34
# Ania 27
#
# 0 Radek 45
for i in enumerate(zip(imiona, wiek)):
    print(i)

# (3, ('Ania', 27))
a, b = (3, ('Ania', 27))
print(a, b)
# 3 ('Ania', 27)
c, d = ('Ania', 27)
print(a, c, d)
a, (c, d) = (3, ('Ania', 27))
for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 45
# 1 Tomek 65
# 2 Zenek 34
# 3 Ania 27