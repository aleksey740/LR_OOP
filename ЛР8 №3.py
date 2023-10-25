class Quadrilateral:
    def __init__(self, width, height=None):
        if height is None:
            #Если передан только один аргумент, то создаем квадрат.
            self.width = width
            self.height = width
        else:
            #Иначе создаем прямоугольник.
            self.width = width
            self.height = height

    def __str__(self):
        if self.width == self.height:
            return f"Куб размером {self.width}х{self.height}"
        else:
            return f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):
        return self.width == self.height

#Пример использования:
q1 = Quadrilateral(10)
print(q1)  #Печатает "Куб размером 10х10"
print(bool(q1))  #Печатает "True"

q2 = Quadrilateral(3, 5)
print(q2)  #Печатает "Прямоугольник размером 3х5"
print(bool(q2))  #Печатает "False"
