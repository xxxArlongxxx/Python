x=10

if x > 5:
    pass;

currencies = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "JPY": "Japanese Yen",}
'''
for currency in currencies.items():
    print(f"{currency[0]}: {currency[1]}")
'''
for range in range(5):
    if range == 2:
        continue
    print(range)