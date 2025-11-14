import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/usd/"

response = requests.get(url)
print(response)
# <Response [200]>
# 2xx ok
# 3xx przekierowania, warningi
# 404 brajk zasobu, 400 Bad req
# 500 Internal serwer error
print(response.text)
# {"table":"A","currency":"dolar amerykański","code":"USD",
# "rates":[{"no":"221/A/NBP/2025","effectiveDate":"2025-11-14","mid":3.6376}]}
data = response.json()
print(data)
print(type(data))  # <class 'dict'>
# {'table': 'A',
# 'currency': 'dolar amerykański',
# 'code': 'USD',
# 'rates': [{'no': '221/A/NBP/2025', 'effectiveDate': '2025-11-14', 'mid': 3.6376}]}
print(data['rates'])
# [{'no': '221/A/NBP/2025', 'effectiveDate': '2025-11-14', 'mid': 3.6376}]
print(data['rates'][0]['mid'])  # 3.6376
