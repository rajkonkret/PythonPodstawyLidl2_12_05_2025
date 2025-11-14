# funkcja dekorator
# dodaje funkcjonalnosc do innej funkcji

from colorama import init, Fore, Style

# pip install colorama
init(autoreset=True)


def dekorator(func):
    def wrapper():
        print("Dekorujemy")
        return func()  # wykonanie funkxji i zwrócenie wyniku

    return wrapper  # zwracamy adres funkcji


def color_decorator(func):
    def wrapper():
        result = func()
        return Fore.RED + result + Style.RESET_ALL

    return wrapper


@dekorator
def hello():
    print("witaj Świecie")


@color_decorator
def hello2():
    return "Tekst"


hello()
# Dekorujemy
# witaj Świecie
print(hello2())  # Tekst
