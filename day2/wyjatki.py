# wyjątek - błąd podczas wykonywania programu

# print(5 / 0)
# /Users/radoslawjaniak/PycharmProjects/PythonPodstawyLidl2_12_05_2025/day2/wyjatki.py
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/PythonPodstawyLidl2_12_05_2025/day2/wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    # print(5 / 0 )
    # print("a" * "23")
    # print(int("A"))
    # raise KeyError("Brak klucza")  # rzucenie konkretenego błedu
    value = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Bład wartości")
except Exception as e:  # pozstałe błedy
    print("Bląd:", e)
# Bląd: 'Brak klucza'
else:  # tylko gdy nie ma błedu
    print("Wartośc:", value)
finally:  # zawsze
    print("Kolejne oblicznie")
