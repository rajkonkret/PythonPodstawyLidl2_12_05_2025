# funkcja dekorator
# dodaje funkcjonalnosc do innej funkcji
def dekorator(func):
    def wrapper():
        print("Dekorujemy")
        return func()  # wykonanie funkxji i zwrócenie wyniku

    return wrapper  # zwracamy adres funkcji


@dekorator
def hello():
    print("witaj Świecie")


hello()
# Dekorujemy
# witaj Świecie
