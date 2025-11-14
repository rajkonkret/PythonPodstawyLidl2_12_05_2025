import chardet

# print(chardet)

file_path = 'test.log'

# rb - wczytanie binarnir
with open(file_path, "rb") as file:
    raw_data = file.read()

print(raw_data)

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}

encoding = result['encoding']

print(encoding)  # utf-8utf-8
print(raw_data.decode(encoding=encoding))

# Powitanie2
# Kolejny2
# Jeszcze jedno2
# Powitanie2
# Kolejny2
# Jeszcze jedno2
# Dośążźdane
