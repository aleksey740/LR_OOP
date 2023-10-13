from patient import Patient

#Создаем массив объектов Patient
patients = [
    Patient("Иванов", "Илья", "Иванович", "Минск", 232, "Грипп"),
    Patient("Алексеев", "Петр", "Сергеевич", "Гродно", 787, "Ангина"),
    Patient("Дворецкий", "Павел", "Владимирович", "Витебск", 454, "ОРВИ"),
]

def find_patients_in_range(start, end):
    """
    Функция для поиска пациентов с номерами медицинских карт.

    Аргументы:
        Начальное значение интервала.
        Конечное значение интервала.
    """
    result = []
    for patient in patients:
        if start <= patient.medical_card_number <= end:
            result.append(patient)
    return result

#Выводим информацию о всех пациентах
for patient in patients:
    patient.print_info()

#Найдем пациентов в интервале медицинских карт от 1001 до 1003 и выведем их информацию
print("Пациенты в интервале от 232 до 787:")
patients_in_range = find_patients_in_range(232, 787)
for patient in patients_in_range:
    patient.print_info()
