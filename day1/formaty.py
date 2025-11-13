user = "Tomek"
wiek = 67
wersja = 3.900001
print(type(wersja))  # <class 'float'>, liczby zmienoprzecinkowe
liczby = 890123456123  # int

print("witaj %s, masz teraz %d lat" % (user, wiek))
# %s - str
# %d - digit
# witaj Tomek, masz teraz 67 lat

# sprawdza typy danych
# print("witaj %d, masz teraz %s lat" % (user, wiek))
# TypeError: %d format: a real number is required, not str

# f - string format, nie sprawdza typu
print(f"Witaj {user}, masz teraz {wiek} lat.")
# Witaj Tomek, masz teraz 67 lat.
print("Witaj {}, masz teraz {} lat.".format(user, wiek))

print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
# %f - float
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4

print(f"Uzywamy pythona {wersja}")  # Uzywamy pythona 3.900001
print(f"Uzywamy pythona {wersja:.2f}")  # Uzywamy pythona 3.90
print(f"Uzywamy pythona {wersja:.1f}")  # Uzywamy pythona 3.9
print(f"Uzywamy pythona {wersja:.0f}")  # Uzywamy pythona 4

user = "Tomek"
print(f"{user:>10}")  # "     Tomek"
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^20}")  # "       Tomek        "
print(liczby)
print(f"Nasza duza liczba: {liczby:,}")  # Nasza duza liczba: 890,123,456,123
print(f"Nasza duza liczba: {liczby:_}")  # Nasza duza liczba: 890_123_456_123
print(f"Nasza duza liczba: {liczby:_}".replace("_", "."))  # Nasza duza liczba: 890.123.456.123
print(f"Nasza duza liczba: {liczby:_}".replace("_", " "))  # Nasza duza liczba: 890 123 456 123

# liczba = 15000000000000
liczba = 15_000_000_000_000
print(type(liczba))  # <class 'int'>
print(liczba)  # 15000000000000
