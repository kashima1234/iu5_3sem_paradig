def field(items, *args):
    filtered_item = []
    for item in items:
        founded_keys = {}
        for key in args:
            if key in item and item[key] is not None:
                founded_keys[key] = item[key]
        if len(founded_keys):
            filtered_item.append(founded_keys)
    return filtered_item

# Пример использования
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

# Примеры использования генератора
print("По одному полю:")
for title in field(goods, 'title'):
    print(title)

print("По нескольким полям:")
for item in field(goods, 'title', 'price'):
    print(item)

