# # programownie obiektowe
# klasa - szablon, przepis
# obiekt - instancja klasy - stworzeony wg przepisu
# musi byc najpierw zadeklarowana
# tworzenie obiektu uruchamia metodę __init__
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase
class Human:
    """
    Klasa Human w Pythonie
    """
    imie = ""
    wiek = None


print(Human.__doc__)  # Klasa Human w Pythonie
print(print.__doc__)
# pydoc -b
# pydoc -w kl1

# tworzenie obiektu klasy
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x109b31550>
print(cz1.imie)
cz1.imie = "Radek"
print(cz1.imie)  # Radek
