#Импорт всего из модуля tkinter
from tkinter import *
#Создание главного окна
window = Tk()
#Установка размеров окна
window.geometry("250x200")
#Создание списка с возможностью выбора нескольких элементов
list1 = Listbox(window, height=5, width=15, selectmode=EXTENDED)
#Создание списка с возможностью выбора только одного элемента
list2 = Listbox(window, height=5, width=15, selectmode=SINGLE)
#Заполнение первого списка элементами из списка lst1
lst1 = ['Минск', 'Молодечно', 'Борисов', 'Жодино', 'Воложин']
for i in lst1:
    list1.insert(END, i)
#Заполнение второго списка элементами из списка lst2
lst2 = ['Гродно', 'Ивье', 'Новогрудок', 'Ошмяны', 'Островец']
for i in lst2:
    list2.insert(END, i)
#Размещение первого списка в окне
list1.pack()
#Размещение второго списка в окне
list2.pack()
#Запуск главного цикла для отображения окна
window.mainloop()
