#Класс город
class City:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


#Класс здание
class Building:
    def __init__(self, street_name, house_number, total_area, base_payment_per_sqm):
        self._street_name = street_name
        self._house_number = house_number
        self._total_area = total_area
        self._base_payment_per_sqm = base_payment_per_sqm

    @property
    def street_name(self):
        return self._street_name

    @street_name.setter
    def street_name(self, new_street_name):
        self._street_name = new_street_name

    @property
    def house_number(self):
        return self._house_number

    @house_number.setter
    def house_number(self, new_house_number):
        self._house_number = new_house_number

    @property
    def total_area(self):
        return self._total_area

    @property
    def base_payment_per_sqm(self):
        return self._base_payment_per_sqm

    @base_payment_per_sqm.setter
    def base_payment_per_sqm(self, new_payment):
        self._base_payment_per_sqm = new_payment


#Класс помещение
class Room:
    def __init__(self, number, area, building):
        self._number = number
        self._area = area
        self._building = building

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, new_number):
        self._number = new_number

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, new_area):
        self._area = new_area

    @property
    def building(self):
        return self._building

    @building.setter
    def building(self, new_building):
        self._building = new_building




#Класс квартиру
class Apartment(Room):
    def __init__(self, number, area, residents, building):
        super().__init__(number, area, building)
        self._residents = residents

    @property
    def residents(self):
        return self._residents

    @residents.setter
    def residents(self, new_residents):
        self._residents = new_residents

    #Метод для расчета ежемесячной оплаты
    def calculate_monthly_payment(self):
        try:
            if not self._residents:
                raise ValueError("Нет жильцов в квартире")

            monthly_payment = self.area * self.calculate_base_payment()
            print(f"Ежемесячная оплата за квартиру: {monthly_payment}")

        except ValueError as e:
            print(f"Ошибка: {e}")

    #Метод для расчета базвой оплаты
    def calculate_base_payment(self):
        return self.area * self.building.base_payment_per_sqm


#Класс офис
class Office(Room):
    def __init__(self, number, area, company_name, business_type, building):
        super().__init__(number, area, building)
        self._company_name = company_name
        self._business_type = business_type

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, new_name):
        self._company_name = new_name

    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, new_type):
        self._business_type = new_type

    #Метод для расчета ежемесячной оплаты
    def calculate_monthly_payment(self):
        try:
            monthly_payment = self.area * self.calculate_base_payment()
            print(f"Ежемесячная оплата за офис: {monthly_payment}")
        except Exception as e:
            print(f"Ошибка: {e}")

    #Метод для расчета базовой оплаты
    def calculate_base_payment(self):
        return self.area * self.building.base_payment_per_sqm


#Ввод данных
city_name = input("Введите название города: ")
building_street = input("Введите название улицы: ")
building_number = input("Введите номер дома: ")
building_total_area = float(input("Введите общую площадь здания: "))
building_base_payment = float(input("Введите базовую ежемесячную оплату за квадратный метр: "))

apartment_number = input("Введите номер квартиры: ")
apartment_area = float(input("Введите площадь квартиры: "))
residents = input("Введите имена жильцов через запятую: ").split(", ")

office_number = input("Введите номер офиса: ")
office_area = float(input("Введите площадь офиса: "))
company_name = input("Введите название компании: ")
business_type = input("Введите вид деятельности компании: ")

#Создание объектов
city = City(city_name)
building = Building(building_street, building_number, building_total_area, building_base_payment)

apartment = Apartment(apartment_number, apartment_area, residents, building)
office = Office(office_number, office_area, company_name, business_type, building)

#Вызов методов для расчета ежемесячной оплаты
apartment.calculate_monthly_payment()
office.calculate_monthly_payment()