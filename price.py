# price = 100
# discount = 5

def discounted(price, discount, max_discount=20): # 3 аргумент именнованый именованные агрументы не могут идти перед позиционными
    price =abs(price)   # абсолютный аргумент
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Максимальная скидка не может быть больше 100')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount


# defdicounted(100, 10)
# defdicounted(-100, 5)
# price_discounted = discounted(100, 50)
# print(price_discounted)
# product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
# product['with_discount'] = (discounted(product['price'], product['discount']))
# print(product)
print(discounted(100, 5))
print(discounted(100, 50))
print(discounted(100, 50, max_discount=60))
