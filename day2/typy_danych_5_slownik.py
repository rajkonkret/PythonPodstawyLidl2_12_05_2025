# słownik - para klucz - wartość
# klucze nie mogą się powtarzac
# {"user":"Radek"}
# odpowiednik jsona

# pusty słownik
dictionary = {}
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

pusty_dict = dict()
print(type(pusty_dict))  # <class 'dict'>
print(pusty_dict)  # {}

# dodanie lementu słowniku
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 50
print(dictionary)  # {'imie': 'Radek', 'wiek': 50}

dict_list = {"imie": ["Radek", 'Tomek', "Zenek"]}
print(dict_list)  # {'imie': ['Radek', 'Tomek', 'Zenek']}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 50])
# dict_items([('imie', 'Radek'), ('wiek', 50)])

# wypisanie wartosci dla klucza
print(dictionary['imie'])

print(dict_list['imie'])  # ['Radek', 'Tomek', 'Zenek']
print(dict_list['imie'][1])  # Tomek

# print(dictionary['Imie'])  # KeyError: 'Imie'

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default, wskazujemy domyślną wartość
print(dictionary.get("imie", "default"))  # Radek

dictionary.update({"data": "31-12-2030"})
print(dictionary)
# {'imie': 'Radek', 'wiek': 50, 'data': '31-12-2030'}

# dict_items([('imie', 'Radek'), ('wiek', 50)])

dict_small = {"x": 4}
print(dict_small)
dict_small.update([("a", 8), ("b", 23)])
print(dict_small)  # {'x': 4, 'a': 8, 'b': 23}
