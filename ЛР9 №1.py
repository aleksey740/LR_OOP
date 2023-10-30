#Создаем класс Rectangle с двумя сторонами a и b.
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # Метод get_area возвращает площадь прямоугольника.
    def get_area(self):
        return self.a * self.b
#Определяем класс Square с одной стороной a.
class Square:
    def __init__(self, a):
        self.a = a
    #Метод get_area возвращает площадь квадрата.
    def get_area(self):
        return self.a ** 2
#Определяем класс Circle (Круг) с радиусом r.
class Circle:
    def __init__(self, r):
        self.r = r
    #Метод get_area() возвращает площадь круга, используя значение p(приближенно 3.14).
    def get_area(self):
        return 3.14 * self.r ** 2
#Создаем экземпляры классов и передаем соответствующие параметры.
rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 3)
square = Square(2)
circle = Circle(3)
#Создаем список, содержащий созданные экземпляры фигур.
figures = [rect1, rect2, square, circle]
#Итерируемся по списку фигур и выводим их площади.
for figure in figures:
    print(figure.get_area())
