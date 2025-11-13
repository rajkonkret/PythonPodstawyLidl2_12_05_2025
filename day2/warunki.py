# instrukcje warunkowe
# instrukcje sterowanie przepływem programu
# if -  w zależności od warunku (True/False) wykonuje odpowiedni blok programu

odp = True
# odp = False
# Indend Rainbow
if odp:
    # wykona się gdy warunek True
    print("Kod programu")
    print("Kod programu")
    print("Kod programu")
    print("Kod programu")
    print("Kod programu")

print("Dalsza częśc programu")

odp = "Radek"
print(bool(odp))  # True
if odp:
    print("Radek")  # Radek

if odp == "Radek":
    print("Radek")  # Radek

odp = 0
if odp:
    print("Działą")
else:  # wartośc domyslna, inne
    print("Zero -> False")
# Zero -> False

a = "Radek"
# warunek ma byc True gdy długosc większa niż 3

if len(a) > 3:
    print(f'Długosć wynosi: {len(a)}')
# Długosć wynosi: 5

n = len(a)
if n > 3:
    print(f'Długosć wynosi: {n}')

# walrus operator - operator morsa
if (n := len(a)) > 3:
    print(f'Długosć wynosi: {n}')
    # Długosć wynosi: 5

# podatek = 0
# zarobki = int(input("Podaj zarobki:"))
#
# # kolejność ma znaczeie
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"podatek wynosi: {podatek * zarobki} pln.")
# # podatek 0.2 dla przedział od 10000 do 39999
# # podatek wynosi: 5000.0 pln.

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0
print("Rabat wynosi:", rabat)  # Rabat wynosi: 25

# operator warunkowy
rabat = 25 if suma_zam > 100 else 0
print("Rabat wynosi:", rabat)  # Rabat wynosi: 25

# napisac test z
# dodac punktację
punkty = 0
odp = input("Podaj datę Chrztu Polski")
if odp == '966':
    print("Dobrze")
    punkty += 1  # punkty  = punkty + 1
else:
    print("Musisz jescze się douczyć")

odp = input("Podaj datę Bitwy pod Grunwaldem")
if odp == '1410':
    print("Dobrze")
    punkty += 1  # punkty  = punkty + 1
else:
    print("Musisz jescze się douczyć")

print("Zdobyłęś pkt:", punkty)# Podaj datę Chrztu Polski966
# Dobrze
# Podaj datę Bitwy pod Grunwaldem1410
# Dobrze
# Zdobyłęś pkt: 2
