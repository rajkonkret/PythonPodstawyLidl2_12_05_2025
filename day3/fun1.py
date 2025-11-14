# funkcje - wydzielony fragment kodu, można wywołać w dowolnym momencie
# funkcja musi najpierw zostac zadeklarowana
# żeby uruchomic funkcjee, musi zostać wywołana

a = 8
b = 9


# deklaracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):
    print(a + b)


# 3 symulowanie przeciążania argumentów funkcji
def odejmij(a, b, c=0):
    print(a - b - c)


# wywołanie funkcji()
dodaj()  # 17
# dodaj2()
# TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# argumenty po pozycji
dodaj2(4, 8)  # 12
odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4

# po nazwie
odejmij(c=9, b=0, a=34)  # 25

# mieszane
odejmij(1, 2, c=90)  # -91


# pozycyjne przed nazwanami
# SyntaxError: positional argument follows keyword argument
# odejmij(a=1, 3, 4)

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(dodaj() + dodaj2(7, 9))


# funkcje zwracajace wynik

def dodaj3(a, b):
    return a + b


print(dodaj3(7, 9))  #
zm = dodaj3(5, 9)
print('Zmienna:', zm)  # Zmienna: 14

print(dodaj3(5, 1) + dodaj3(67, 90))  # 163
