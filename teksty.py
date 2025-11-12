tekst = "Witaj"

print(tekst)
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
# """ Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)
print(tekst.upper())  # WITAJ
tekst_upper = tekst.upper()
print(tekst_upper)

tekst = "Witaj Świecie"

print(tekst.capitalize())  # Witaj świecie
print(tekst.lower())  # witaj świecie

print(tekst.removeprefix('Witaj'))  # " Świecie"
print(tekst.removesuffix('Świecie'))  # " Witaj "

# strip() - usunięcie biłaych znaków
print(tekst.removeprefix('Witaj').strip())  # "Świecie"

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9awiecie'
print(type(encoded_s))  # <class 'bytes'>
# \xc5\x9a zpis szesnastkowy literki Ś
print(encoded_s.decode('utf-8'))  # Witaj Świecie

print(tekst)
# Witaj Świecie
# 01234567890..

print(tekst[4])  # "j"

print(tekst.count("i"))  # wystąpi 3 razy
print(tekst.count("j", 0, 4))  # wystepuje 0 razy, indeks 4 nie jest brany pod uwagę

imie = "Radek"
print("imie:", imie)  # imie: Radek

print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

print(f"\tMam imię {imie}\n i lubię pythona.")
# "	 Mam imię Radek
#  i lubię pythona."

#
"""Komentarz
    dokumentacyjna"""
