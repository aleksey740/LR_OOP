import tkinter as tk
from math import log, sin, tan, fabs

def calculate_formula(x):
    result = 1.8 + log(fabs(4)*(2/7) - tan(sin(5*x/3)))
    return result

def update_result_label():
    try:
        x_value = float(entry.get())
        result = calculate_formula(x_value)
        result_label.config(text=f"Выражение = {result}")
    except ValueError:
        result_label.config(text="Ошибка: Введите числовое значение для x")

#Создание основного окна
window = tk.Tk()
window.title("Подсчет по формуле")
window.geometry('240x180')

#Создание метки с заголовком
title_label = tk.Label(window, text="Подсчет по формуле", font=('Arial', 16), fg='blue')
title_label.place(x=20, y=20)

#Создание поля ввода с подписью
x_label = tk.Label(window, text="x = ")
x_label.place(x=20, y=60)

entry = tk.Entry(window)
entry.place(x=60, y=60)

#Создание кнопки для вычисления
calculate_button = tk.Button(window, text="Вычислить", command=update_result_label)
calculate_button.place(x=20, y=100)

#Создание метки для вывода результата
result_label = tk.Label(window, text="Выражение = ")
result_label.place(x=20, y=140)

#Обработка закрытия окна
window.protocol("WM_DELETE_WINDOW", window.destroy)

#Запуск главного цикла
window.mainloop()
