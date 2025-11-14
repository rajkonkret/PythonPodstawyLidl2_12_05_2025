a = 10
b = 10


def dodaj():
    a = 7
    b = 8  # argumenty lokalne
    print(a + b)


def dodaj2():
    print(a + b)  # globalne


def dodaj3():
    global a
    a = 9  # zmieniamy wartość globalnego a
    b = 17
    print(a + b)


print(f"Wartośc a z góry (globalne): {a=}")  # Wartośc a z góry (globalne): a=10
dodaj()  # 15
print(f"Wartośc a z góry (globalne): {a=}")  # Wartośc a z góry (globalne): a=10
dodaj2()
print(f"Wartośc a z góry (globalne): {a=}")  # Wartośc a z góry (globalne): a=10
dodaj3()
print(f"Wartośc a z góry (globalne): {a=}")  # Wartośc a z góry (globalne): a=9
dodaj2()  # 19
