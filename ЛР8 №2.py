class Vector:
    def __init__(self, *args):
        #Конструктор класса, принимающий произвольное количество аргументов.
        self.values = []  #Создание пустого списка для хранения значений вектора.
        for arg in args:
            if isinstance(arg, int):
                #Проверка, что аргумент является целым числом и добавление его в список значений.
                self.values.append(arg)
            self.values.sort()  #Сортировка значений вектора.
    def __str__(self):
        #Метод представления вектора в виде строки.
        if len(self.values) == 0:
            return 'пусть вектор'
        return f'вектор{tuple(self.values)}'

    def __add__(self, other):
        #Метод для сложения векторов.
        new_v = []  #Создание списка для нового вектора.
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] + other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('сложение векторов разной длины недопустимо.')
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i] + other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        #Метод для умножения векторов.
        new_v = []  #Создание списка для нового вектора.
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] * other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('умножение векторов разной длины недопустимо.')
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i] * other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
            print(f'Вектор нельзя умножить на {other}')
#Создание объектов класса Vector.
v1 = Vector(1, 2, 3)
print(v1)
v2 = Vector(4, 7, 1, 12)
print(v2)
v3 = Vector(7, 11, 3, 18)
print(v3)
#Выполнение сложения и умножения векторов.
print(v2 + v3)
print(v2 * v3)
