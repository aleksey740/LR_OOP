class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.barand = brand
        self.max_speed = max_speed
        self.kind = kind
    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развивать скорость {self.max_speed} км/ч"

class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f"Осталось бензина на {self.__gasoline_residue} км"

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue += value
            print(f"Обьем топлива увеличен на {value}  л и состовляет {self.__gasoline_residue} л")
        else:
            print("Ошибка заправки автомобиля")

class Boat(Transport):

    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"

class Plane(Transport):

    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity

    def __str__(self):
        return f"Самолет марки {self.brand} вмещает в себя {self.capacity} людей"

