import tkinter as tk  # Импорт модуля tkinter под псевдонимом tk
from tkinter import ttk  # Импорт классов ttk из модуля tkinter
import math  # Импорт модуля math для математических операций

def calculate_values():  # Определение функции calculate_values для табуляции значений функции
    for i in range(1, 10):  # Цикл для прохода по диапазону параметра от 1 до 9 с шагом 1
        x = i  # Присвоение значения x
        y = math.atan(2 * x + 1)  # Вычисление значения функции
        results_listbox.insert(tk.END, f"{x}            {y:.4f}")  # Добавление результатов в виджет Listbox
        update_progressbar(i * 10)  # Вызов функции для обновления значения Progressbar

def update_progressbar(value):  # Определение функции update_progressbar для обновления Progressbar
    progressbar['value'] = value  # Присвоение нового значения Progressbar
    root.update_idletasks()  # Обновление интерфейса

root = tk.Tk()  # Создание главного окна приложения
root.title("Табуляция функции y=arctg(2*x+1)")  # Установка заголовка окна

frame = tk.Frame(root)  # Создание фрейма в главном окне
frame.pack()  # Размещение фрейма в окне

label = tk.Label(frame, text="y = arctg(2*x+1)", font=('Arial', 16))  # Создание метки с текстом
label.pack(pady=10)  # Размещение метки во фрейме с отступом

calculate_button = ttk.Button(frame, text='Расчет', command=calculate_values)  # Создание кнопки Расчет
calculate_button.pack(pady=10)  # Размещение кнопки во фрейме с отступом

results_listbox = tk.Listbox(root, width=50, height=10)  # Создание виджета Listbox
results_listbox.pack(pady=10)  # Размещение виджета Listbox в окне с отступом

progressbar = ttk.Progressbar(root, length=200, mode='determinate')  # Создание виджета Progressbar
progressbar.pack(pady=10)  # Размещение виджета Progressbar внизу окна с отступом

root.mainloop()  # Запуск главного цикла обработки событий для отображения окна
