import tkinter as tk
from random import randint

def roll_dice():
    #Генерация случайного числа от 1 до 6
    result = randint(1, 6)
    #Обновление текста
    label.config(text=str(result))

#Создание основного окна
window = tk.Tk()
window.title("Брось кубик")
window.geometry('360x100')
#Создание метки с начальным текстом
label = tk.Label(window, text="Брось кубик", font=('Arial', 18), fg='blue')
label.pack(pady=20)

#Создание кнопки "Бросить кубик"
button = tk.Button(window, text="Бросить кубик", command=roll_dice)
button.pack()

#Обработка закрытия окна
window.protocol("WM_DELETE_WINDOW", window.destroy)

#Запуск главного цикла
window.mainloop()
