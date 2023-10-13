class Patient:
    """
    Класс для представления информации о пациенте.

    Атирибуты:
        Фамилия.
        Имя.
        Отчество.
        Адрес.
        Номер медицинской карты.
        Диагноз пациента.
    """

    def __init__(self, last_name, first_name, middle_name, address, medical_card_number, diagnosis):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.medical_card_number = medical_card_number
        self.diagnosis = diagnosis

    def print_info(self):
        """
        Метод для вывода информации.
        """
        print(f"Фамилия: {self.last_name}")
        print(f"Имя: {self.first_name}")
        print(f"Отчество: {self.middle_name}")
        print(f"Адрес: {self.address}")
        print(f"Номер медицинской карты: {self.medical_card_number}")
        print(f"Диагноз: {self.diagnosis}")
