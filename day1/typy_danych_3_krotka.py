# krotka - pozwala lepiej zarządzac pamięcią
# lista niemutowalna

tupla_imiona = ("Radek", "Tomek", "Zenek", "Roman")
print(type(tupla_imiona))
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Roman')

tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

tupla_1 = 43,
print(type(tupla_1))
print(tupla_1)
# <class 'tuple'>
# (43,)

# PEP8 zaleca nawias dla krotki jedoelemntowaj
tupla_2 = (43,)
print(type(tupla_2))
print(tupla_2)
# <class 'tuple'>
# (43,)

# tupla_liczby[3] = 123  # TypeError: 'tuple' object does not support item assignment

del tupla_liczby
# print(tupla_liczby) # NameError: name 'tupla_liczby' is not defined

print(tupla_imiona.count("Radek"))  # wystepuje 1 raz
print(tupla_imiona.index("Radek"))  # indeks 0

# rozpakowanie tupli
tup = 1, 2
print(type(tup))
a, b = 1, 2
a, b = tup
print(f"{a=}, {b=}")  # a=1, b=2

tup2 = 1, 2, 3
# a, b = tup2  # ValueError: too many values to unpack (expected 2)
a, *b = tup2  # * worek na pozostale dane
print(a, b)  # 1 [2, 3]

name1, name2, *name3 = tupla_imiona
print(f"{name1}, {name2}, {name3}")
# Radek, Tomek, ['Zenek', 'Roman']

*name1, name2, name3 = tupla_imiona
print(f"{name1}, {name2}, {name3}")
# ['Radek', 'Tomek'], Zenek, Roman

name1, *name2, name3 = tupla_imiona
print(f"{name1}, {name2}, {name3}")
# Radek, ['Tomek', 'Zenek'], Roman

lista_z_tupli = list(tupla_imiona)
print(lista_z_tupli)  # ['Radek', 'Tomek', 'Zenek', 'Roman']

print(sorted(tupla_imiona))
# ['Radek', 'Roman', 'Tomek', 'Zenek'] - zwraca liste
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Roman') nie zmieni krotki!!!
