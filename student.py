import random
class Student:
    """
    Класс студента.
    Атрибуты:
    Фамилия и имя.
    Номер группы.
    Список оценок.
    """
    def __init__(self, name, group_number, academic_perfomance):
        """
        Новый экземпляр класса Student.
        Аргументы:
        Фамилия и имя.
        Номер группы.
        Список оценок.
        """
        self.name = name
        self.group_number = group_number
        self.academic_perfomance = academic_perfomance
        self.gpa_scores = sum(self.academic_perfomance) / 5

    def print_info(self):
        """
        Вывод информаци о студенте.
        """
        print(f'ФИ: {self.name}\n'
              f'  Номер группы: {self.group_number}\n'
              f'  Успеваемость: {self.academic_perfomance}\n'
              f'  Средний балл: {self.gpa_scores}\n')
def byGPA_key(student):
    """
    Функция для сортировки студентов по баллу.
    Аргументы:
        student (Student): Экземпляр класса Student.
    """
    return student.gpa_scores
