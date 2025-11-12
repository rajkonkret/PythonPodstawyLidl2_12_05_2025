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
