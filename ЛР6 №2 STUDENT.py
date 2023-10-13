#Импортирование класса Student и функции byGPA_key из модуля student
from student import Student, byGPA_key

#Импортирование модуля random для генерации чисел
import random

#Основная функция программы
def main():
    #Создание списка студентов с использованием генератора списка и ввода данных с клавиатуры
    students = [
        Student(
            input('Введите фамилию и имя студента: '),
            input('Введите номер группы: '),
            [random.randint(1, 10) for i_grade in range(5)]
        )
        for i_student in range(10)
    ]

    # Сортировка списка студентов по средней оценке (GPA) с использованием функции byGPA_key
    students_sort = sorted(students, key=byGPA_key)

    # Вывод информации о студентах после сортировки
    for student in students_sort:
        student.print_info()

# Запуск функции main только если скрипт запущен как отдельный файл
if __name__ == "__main__":
    main()
