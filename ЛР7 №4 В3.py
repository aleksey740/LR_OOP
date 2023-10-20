class Aircraft:
    def __init__(self, model, max_payload, fuel_consumption):
        self.model = model
        self.max_payload = max_payload  # Грузоподъемность в килограммах
        self.fuel_consumption = fuel_consumption  # Потребление топлива в литрах на 100 км
class AviationCompany:
    def __init__(self, name):
        self.name = name
        self.aircraft_list = []
    def add_aircraft(self, aircraft):
        self.aircraft_list.append(aircraft)
    def total_payload_capacity(self):
        return sum(aircraft.max_payload for aircraft in self.aircraft_list)
    def find_aircraft_by_fuel_consumption(self, min_fuel_consumption, max_fuel_consumption):
        return [aircraft for aircraft in self.aircraft_list
                if min_fuel_consumption <= aircraft.fuel_consumption <= max_fuel_consumption]
#Создаем объекты-самолеты
aircraft1 = Aircraft("Boeing 747", 300000, 150)
aircraft2 = Aircraft("Airbus A380", 350000, 160)
aircraft3 = Aircraft("Boeing 777", 250000, 140)
#Создаем объект авиакомпании и добавляем в него самолеты
aviation_company = AviationCompany("MyAir")
aviation_company.add_aircraft(aircraft1)
aviation_company.add_aircraft(aircraft2)
aviation_company.add_aircraft(aircraft3)
#Выводим общую грузоподъемность
print(f"Общая грузоподъемность {aviation_company.name}: {aviation_company.total_payload_capacity()} кг")
#Находим самолеты с потреблением горючего в заданном диапазоне
min_fuel = 140
max_fuel = 160
matching_aircraft = aviation_company.find_aircraft_by_fuel_consumption(min_fuel, max_fuel)
#Выводим информацию о найденных самолетах
print(f"Самолеты с потреблением горючего от {min_fuel} до {max_fuel} л/100 км:")
for aircraft in matching_aircraft:
    print(f"Модель: {aircraft.model}, Грузоподъемность: {aircraft.max_payload} кг, Потребление горючего: {aircraft.fuel_consumption} л/100 км")
