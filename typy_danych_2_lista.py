# kolekcje

# lista - przechowuje dowolna ilosc danych różnego typu
# zachowuje kolejnośc przy dodawaniu elementów

lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(type(pusta_lista))
print(pusta_lista)

# append() - dodanie elemntów do listy

lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Anna")
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Anna']
# ['Radek', 'Tomek', 'Zenek', 'Anna']
#     0        1        2       3
#     -4       -3       -2      -1
print(lista[2])  # Zenek

# print(lista[10])  # IndexError: list index out of range

print(len(lista))  # 4
print(lista[len(lista) - 1])  # Anna
print(lista[-1])  # Anna
print(lista[-2])  # Zenek

# ['Radek', 'Tomek', 'Zenek', 'Anna']
# slicowanie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'] - 012
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[1:])  # ['Tomek', 'Zenek', 'Anna'], z ostatnim włacznie
print(lista[1:3])  # ['Tomek', 'Zenek']

print(lista[2:15])  # ['Zenek', 'Anna']
print(lista[20:456])  # []

print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek']

print(lista[::2])  # [start:stop:krok]
# ['Radek', 'Zenek']

# # ['Radek', 'Tomek', 'Zenek', 'Anna']
# #     0        1        2       3
# #     -4       -3       -2      -1
print(lista[-2:0])  # -> [2:0], []
print(lista[0:-2])  # -> [0:2], ['Radek', 'Tomek']

lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[::-3])  # [14, 11, 8, 5, 2]

# nadpisanie elementu
lista[3] = "Radek"
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Radek']

# wstawieni elementu
lista.insert(1, "Anna")
print(lista)
#  ['Radek', 'Anna', 'Tomek', 'Zenek', 'Radek']

print(lista.count("Radek"))  # radek występuje 2 razy

# sprawzenie indeksu
print(lista.index("Radek"))  # 0, pierwszy od lewej

# usuniecie elemntu po elemencie
# pierwszy napotkany
lista.remove("Radek")
print(lista)  # ['Anna', 'Tomek', 'Zenek', 'Radek']

# usunięcie po indeksie
print(lista.pop(3))  # Radek
print(lista)  # ['Anna', 'Tomek', 'Zenek']
print(lista.pop())  # usunie ostatni
