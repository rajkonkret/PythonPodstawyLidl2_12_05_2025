# stworzyc funkcję obliczającą średnią
def srednia(name=None, *cyfry):  # * dowolna ilosc argumentów pozycyjnych
    print(cyfry)
    count = len(cyfry)
    suma_p = sum(cyfry)
    try:
        suma = 0
        for c in cyfry:
            suma += c
        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"Średnia dla ucznia: {name} wynosi: {avg}")
        print(f"Średnia dla ucznia: {name} wynosi: {avg_p}")
    finally:
        print("Kolejny uczeń")


srednia()
srednia(1)
srednia(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)
