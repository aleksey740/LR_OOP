#Импорт всего из модуля tkinter
from tkinter import *
from tkinter import ttk

#Функция для сохранения информации о пользователе в файл
def save_to_file():
    #Открытие файла с именем user_info.tx в режиме записи
    with open('user_info.txt', 'w') as file:
        #Запись имени пользователя в файл
        file.write(f'Имя: {nameT.get()}\n')
        #Запись фамилии пользователя в файл
        file.write(f'Фамилия: {lastNameT.get()}\n')
        #Запись пола пользователя в файл
        file.write(f'Пол: {polvar.get()}\n')
        #Запись любимых предметов пользователя в файл
        file.write('Любимые предметы:\n')
        #Проверка, нравится ли пользователю математика, и запись этого в файл, если да
        if var1.get() == 1:
            file.write('математика\n')
        #Проверка, нравится ли пользователю английский язык, и запись этого в файл, если да
        if var2.get() == 1:
            file.write('английский язык\n')
        #Проверка, нравятся ли пользователю информационные технологии, и запись этого в файл, если да
        if var3.get() == 1:
            file.write('информационные технологии\n')

#Создание главного окна
window = Tk()
#Установка заголовка окна
window.title('Регистрация')

#Создание меток для имени, фамилии, пола и любимых предметов пользователя
name = Label(window, text='Имя', width=20, height=1, fg='blue', font='arial 18')
lastName = Label(window, text='Фамилия', width=20, height=1, fg='blue', font='arial 18')
pol = Label(window, text='Пол', width=20, height=1, fg='blue', font='arial 18')
likePr = Label(window, text='Любимые предметы', width=20, height=1, fg='blue', font='arial 18')

#Создание полей ввода для имени и фамилии пользователя
nameT = Entry(window, width=30, font='arial 14')
lastNameT = Entry(window, width=30, font='arial 14')

#Создание Radiobutton для выбора пола пользователя
polvar = StringVar()
polvar.set(' ')
radio1 = Radiobutton(window, text='мужской', variable=polvar, value='м')
radio2 = Radiobutton(window, text='женский', variable=polvar, value='ж')

#Создание флажков для выбора любимых предметов пользователя
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
check1 = Checkbutton(window, text='математика', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(window, text='английский язык', variable=var2, onvalue=1, offvalue=0)
check3 = Checkbutton(window, text='информационные технологии', variable=var3, onvalue=1, offvalue=0)

#Создание кнопки для отправки информации пользователя
btn = Button(window, text='Принять', width=25, height=5, fg='blue', font='arial 14', command=save_to_file)

#Упаковка всех виджетов в окне
name.pack()
nameT.pack()
lastName.pack()
lastNameT.pack()
pol.pack()
radio1.pack()
radio2.pack()
likePr.pack()
check1.pack()
check2.pack()
check3.pack()
btn.pack()

#Запуск главного цикла для отображения окна
window.mainloop()
