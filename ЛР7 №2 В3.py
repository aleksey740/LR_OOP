class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @property
    def c(self):
        return 1.6 * self.a + self.b**4
#использование класса A
instance_of_A = A(2, 3)  #Инициализация полей a и b
result = instance_of_A.c  #Вычисление свойства c
print(result)  #Вывод результата
