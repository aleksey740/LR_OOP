#Импортируем все классы и функции из модуля tkinter
from tkinter import*

#Функция для закрытия окна
def close_window():
    window.destroy()

#Создаем основное окно
window = Tk()

#Устанавливаем заголовок окна
window.title("Проект 1")

#Устанавливаем размеры окна
window.geometry('400x100')

#Создаем надпис ьв окне
lab = Label(window, text="Моя первая программа", font=('Arial', 14))

#Размещаем метку в окне
lab.pack()

#Создаем кнопку в окне с текстом "Закрыть" и связываем её с функцией close_window
btn = Button(window, text='Закрыть', font=('Arial', 14), command=close_window)

#Размещаем кнопку в окне
btn.pack()

#Запускаем бесконечный цикл обработки событий для отображения окна
window.mainloop()
