import random

class Flower:
    def __init__(self, stem_length, freshness):
        self.stem_length = stem_length
        self.freshness = freshness

    @property
    def stem_length(self):
        return self.__stem_length

    @stem_length.setter
    def stem_length(self, value):
        if not isinstance(value, int):
            print('Длина стебля должна быть числом')
        elif value < 5:
            print('Длина стебля должна быть минимум 5')
        elif value > 20:
            print('Длина стебля должна быть максимум 20')
        else:
            self.__stem_length = value

    @property
    def freshness(self):
        return self.__freshness

    @freshness.setter
    def freshness(self, value):
        if not isinstance(value, int):
            print('Уровень свежести должен быть числом')
        elif value < 1:
            print('Уровень свежести должен быть минимум 1')
        elif value > 10:
            print('Уровень свежести должен быть максимум 10')
        else:
            self.__freshness = value

#Создание списка объектов класса Flower, для которых значения атрибутов - случайные числа
flowers = []
for i in range(5):
    stem_length = random.randint(5, 20)
    freshness = random.randint(1, 10)
    flowers.append(Flower(stem_length, freshness))
    print(f'Цветок {i+1} - Уровень свежести {flowers[i].freshness}')

#Задание диапазона длин стеблей
start = int(input('Введите начальное значение диапазона: '))
end = int(input('Введите конечное значение диапазона: '))

#Вывод элементов списка в заданном диапазоне
for i in range(5):
    if start <= flowers[i].stem_length <= end:
        print(f'Цветок {i+1} - Длина стебля {flowers[i].stem_length}')
