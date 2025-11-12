wiek = 47  # int
rok = 2025
temp = 36.3  # float

print(wiek + rok)  # 2072
print(wiek - rok)  # -1978
print(wiek * rok)  # 95175
print(wiek / rok)  # 0.023209876543209877
print(rok // wiek)  # czesc całkowita z dzielenia, 43
print(2025 // 47)
print(rok % wiek)  # modulo, reszta z dzielenia

print(wiek ** rok)

# len() długosc kolekcji
print(len(str(wiek ** rok)))  # długość : 3386
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 4 / 1 + 4 / 2)  # 36.0
print(54 - 5 * (4 / 1 + 4) / 2)  # 34.0

# błąd zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal() - obejscie problemu zaokrąglenia

# typ logiczny
# True, False
# prawda, fałsz
# 1, 0
czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>

print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # True
print(bool(0))  # False

print(bool(100))
print(bool(-100))

print(bool("Radek"))  # True

print(bool(""))  # False
print(bool("0"))  # True

print(bool(None))  # False, odpowiednik null, brak wartosc, wartośc nieokreslona

# operaccje logiczne

# and -> i
print(True and True)  # True
print(True and False)  # False

# or - lub
print(True or False)  # True

# not - negacja
print(not True)  # False

a = 8
b = 10
print(f"Porównnie {a} > {b} = {a > b}")  # Porównnie 8 > 10 = False
print(f"Porównnie {a > b = }")  # Porównnie a > b = False
print(f"Porównnie {a == b = }")  # == - czy równe, Porównnie a == b = False
print(f"Porównnie {a} != {b} = {a != b}")  # różne!!! Porównnie 8 != 10 = True
