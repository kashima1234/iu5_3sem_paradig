class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items) if isinstance(items, (list, tuple)) else items
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                item = next(self.items)
            except StopIteration:
                raise StopIteration
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.seen:
                self.seen.add(key)
                return item

# Примеры использования:
data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
unique_numbers1 = Unique(data1)
print(list(unique_numbers1))  # Вывод: [1, 2]

# Пример с генератором:
import random

def gen_random(count, begin, end):
    for _ in range(count):
        yield random.randint(begin, end)

data2 = gen_random(10, 1, 3)
unique_numbers2 = Unique(data2)
print(list(unique_numbers2))  # Вывод: [1, 2, 3]

data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
unique_chars1 = Unique(data3)
print(list(unique_chars1))  # Вывод: ['a', 'A', 'b', 'B']

unique_chars2 = Unique(data3, ignore_case=True)
print(list(unique_chars2))  # Вывод: ['a', 'b']

