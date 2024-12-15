import datetime


def add(items, product_name, amount, expiration_date=None):
    year, month, day = map(int, expiration_date.split('-'))  # 2023 9 5
    dictionary = {'amount': amount, 'expiration_date': datetime.date(year, month, day)}
    if product_name in goods:
        items[product_name].append(dictionary)
    else:
        items[product_name] = [dictionary]


def add_by_note(items, note):
    product_name, amount, expiration_date = note.split(" ")
    add(items, product_name, int(amount), expiration_date)


def find(items, needle):
    products = []
    for item in items:
        if needle.upper() in item.upper():
            products.append(item)
    return products


def amount(items, needle):
    count = 0
    for item in items:
        if item.upper() == needle.upper():
            for shipment in items[item]:
                count += shipment['amount']
    return count

goods = {
    'Колбаса': [
        {'amount': 1, 'expiration_date': datetime.date(2012, 12, 12)},
        {'amount': 2, 'expiration_date': datetime.date(2024, 12, 12)},
    ],
    'Яйца': [
        {'amount': 10, 'expiration_date': datetime.date(2025, 12, 12)}
    ]
}

add(goods, 'сыр', 3, '2023-9-30')
add_by_note(goods, 'шоколад 2 2023-4-23')
print(find(goods, 'кол'))
print(amount(goods, 'колбаса'))
print(goods)
