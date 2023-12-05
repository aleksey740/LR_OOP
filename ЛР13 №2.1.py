from tkinter import*

def clicked():
    lab.configure(text="Первые и не последние!", fg='blue', font=('Arial', 16, 'italic'))

def close_window():
    window.destroy()

window = Tk()  #создание графического окна
window.title("Проект 2")
window.geometry('400x100')

#Создаем стиль для изменения вида текста при загрузке окна
style = {'fg': 'green', 'font': ('Arial', 18, 'bold')}

lab = Label(window, text="Первые успехи!", **style)
lab.grid(column=1, row=0)

btn = Button(window, text='Приветствие', font=('Arial', 14), command=clicked)
btn.grid(column=0, row=1)

btn1 = Button(window, text='Закрыть', font=('Arial', 14), command=close_window)
btn1.grid(column=2, row=1)

window.mainloop()
