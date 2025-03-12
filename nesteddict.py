coffee = {"Americano": {'ingredients': ["water", "coffee", "milk"], "price": 10}, "Iced Latte": {'ingredients': ['cream', 'coffee', "Ice"], 'price': 12}}

for key, value in coffee.items():
    print(key,value)



if "milk" in coffee['Americano']['ingredients']:
    print('Milk in da coffee')
else:
    print("No milk in da coffee")
print(coffee["Americano"]['ingredients'])