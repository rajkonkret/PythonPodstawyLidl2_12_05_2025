from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa Ptaak  w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkościa", self.szybkosc)

    # metoda abstrakcyjna
    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Dziedziczy po kalsie Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, 'Ja nie latam')

    def wydaj_odglos(self):
        print("Ko ko ko ko ")


class Orzel(Ptak):

    def wydaj_odglos(self):
        print("Kier kir kier kir")


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzel", 54)
# print(or1.szybkosc)
# print(or1.gatunek)
# # 54
# # Orzel
# or1.latam()  # Tu Orzel Lecę z szybkościa 54
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkościa 0

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam
kur2.wydaj_odglos()

or2 = Orzel("Bielik", 60)
or2.wydaj_odglos()
# Kier kir kier kir

lista = [or2, kur2]
# polimorfizm -  obiektu róznych klas maja cechy wspolne dzieki klasie abstrakcyjnej
for i in lista:
    i.wydaj_odglos()
