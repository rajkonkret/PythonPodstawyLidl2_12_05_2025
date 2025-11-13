# zbiór (set) - przechowuja unikalne wartosci
# nie zachowuje kolejności przy dodawaniu
# nie posiadają indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(type(zbior))
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

# pusty zbiór
zb2 = set()  # pusty zbiór, tylko słówkiem set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(24)
zbior.add(32)
zbior.add(17)
zbior.add(33)
print(zbior)
# {32, 33, 66, 777, 11, 44, 17, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {32, 33, 66, 777, 11, 44, 17, 18, 22, 24}

# pop() - usuniecie usunięcie pierwszego elementu
print(zbior.pop())  # 32
print(zbior)

zmienna = zbior.pop()
print("Zmienna:", zmienna)  # Zmienna: 33

# operacje na zbiorach
zbior2 = {667, 11, 44, 12.34, 18, 53, 667, 62}

# suma zbiorów - zwraca nowy zbiór
print(zbior | zbior2)  # {66, 777, 11, 44, 12.34, 17, 18, 53, 22, 24, 667, 62}
print(zbior.union(zbior2))  # {66, 777, 11, 44, 12.34, 17, 18, 53, 22, 24, 667, 62}

zbior_3 = {66, 777, 11, 44, 12.34, 17, 18, 53, 22, 24, 667, 62, 82, 99, 88}
print(zbior.union(zbior2, zbior_3))
# {66, 777, 11, 12.34, 17, 18, 82, 22, 24, 88, 667, 99, 44, 53, 62}

# częśc wspólna zbiorów
print(zbior & zbior2)  # {18, 11, 44}
print(zbior.intersection(zbior2))  # {18, 11, 44}

# róznica zbiorów
print(zbior - zbior2)  # {66, 777, 17, 22, 24}
print(zbior.difference(zbior2))  # {66, 777, 17, 22, 24}
print(zbior2.difference(zbior))  # {667, 12.34, 53, 62}

# update() - łaczy zbiory, zapisuje w zbiorze oryginaalnym
zbior.update(zbior2)
print(zbior)
# {66, 777, 11, 44, 12.34, 17, 18, 53, 22, 24, 667, 62}

krotka = tuple(zbior)
print(krotka)
# (66, 777, 11, 44, 12.34, 17, 18, 53, 22, 24, 667, 62)

# sprawdzenie czy element istnieje w....
print(777 in zbior)  # True
print(777 in lista)  # True
print(777 in krotka)  # True
print(767 in krotka)  # False
