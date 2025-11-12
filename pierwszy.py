import sys

print("Radek")
print('Radek')
# rtrtrt
# Radek
# Radek

# print('Radek")
#   File "/Users/radoslawjaniak/PycharmProjects/PythonPodstawyLidl2_12_05_2025/pierwszy.py", line 7
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 7)
# Process finished with exit code 1 - błąd wykonania

print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>. dane tekstowe

print("39")
print(type("39"))  # <class 'str'>
print("39" + "39")  # konkatenacja, łączenie tekstów, 3939

print(39)
print(type(39))  # <class 'int'>, liczby całkowite

print(39 + 39)  # 78

# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str

# rzutowanie typów
print(int("39") + 39)  # 78

print("Radek" + str(1))

print(168 * "35")
print(10 * "-")
print(int(168) * int(35))  # 5880
print(50 * "-")
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
# sizeof_digit=4, default_max_str_digits=4300,
# str_digits_check_threshold=640)

# zmienna - pudełko na dane
# snake_case
name = "radek"
print(name)
print(type(name))  # <class 'str'>

name = 90
print(type(name))  # <class 'int'>

# 3 podpowiedzi typów
name: str = "Radek"
print(name)
name = 90
print(name)

age: int = 90
print(age)  # 90
# mypy
# pip install mypy
# pip install mypy-1.18.2-cp313-cp313-win_amd64.whl
import mypy
# (.venv) radoslawjaniak@MacBook-Air-radosaw-2 PythonPodstawyLidl2_12_05_2025 % mypy pierwszy.py
# pierwszy.py:56: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:60: error: Name "name" already defined on line 52  [no-redef]
# pierwszy.py:62: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 3 errors in 1 file (checked 1 source file)

#  python -m mypy pierwszy.py
