from pprint import pprint

# product = {
#     "name": "iPhone 12",
#     "stock": 24,
#     "price": 65432.1,
#     'country': 'RU'
# }

# print(product)

# product['memory'] = 256 # добавление ключа

# product['name'] = 'Samsung 12' # замена жанных по ключу

# print(product['price']) # получение по ключу

# print(product.get('country', 0))

# phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11"]
# # print(product)
# product['recommendet'] = phones
# pprint(product)
# print(product['recommendet'][0])  # обращение к списку в нутри словаря 

# product['recommendet'].append('iPhone 11') # добавление в список внутри словаря 
# pprint(product)

# stock = [
#     {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
#        'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
#     {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
#     {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
# ]

# print(stock[0]) # словарь
# print(stock[0]['recomended']) # список
# print(stock[0]['recomended'][0]) # элемент
# stock[0]['recomended'].append('Xiaomi 11') # добавление в словарь
# print(stock)

# stock[2]['price'] = 30000 # замена цены в словаре
# print(stock)

# print(type(stock))

# Home work

infomation = {
    'city': 'Moscow',
    'temperature': 20
}
pprint(infomation)
# print(infomation['city'])
# infomation['temperature'] = 15
# print(infomation)
# print(infomation.get('country'))
infomation['country'] = 'Россия'
# print(infomation)
infomation['date'] = '20.05.2019'
print(infomation)