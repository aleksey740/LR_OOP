#Импорт модуля tkinter
from tkinter import *
from tkinter import ttk

#Создание главного окна
window = Tk()
#Установка размеров окна
window.geometry("300x80")

#Создание переменной для хранения значения
value_var = IntVar()
#Создание вертикального Progressbar длиной 280 пикселей, связанного с переменной value_var и настроенного на режим 'determinate'
pb = ttk.Progressbar(window, orient="horizontal", length=280, variable=value_var, mode='determinate')
#Размещение Progressbar в окне
pb.pack()

#Функция для запуска Progressbar
def start():
    pb.start(100)
#Функция для остановки Progressbar
def stop():
    pb.stop()

#Создание кнопки Start для запуска Progressbar
start_btn = ttk.Button(text="Start", command=start)
start_btn.pack()
#Создание кнопки Stop для остановки Progressbar
stop_btn = ttk.Button(text="Stop", command=stop)
stop_btn.pack()

#Запуск главного цикла для отображения окна
window.mainloop()
