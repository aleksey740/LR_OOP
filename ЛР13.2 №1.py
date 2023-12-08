import tkinter
from tkinter import *
# Функция для расчета дохода по вкладу
def calculate_interest():
    # Получаем значения из полей ввода
    principal = float(principal_entry.get())  # Сумма вклада
    duration = int(duration_entry.get())      # Срок в днях
    rate = float(rate_entry.get()) / 100      # Процентная ставка в процентах
    interest_type = interest_type_var.get()   # Выбранная схема начисления процентов
    # Рассчитываем доход в зависимости от выбранной схемы
    if interest_type == "Простые проценты":
        simple_interest = principal * rate * duration / 365  # Формула для простых процентов
        total_amount = principal + simple_interest             # Сумма в конце срока
    else:
        total_amount = principal * (1 + rate / 12)**(duration / 30)  # Формула для сложных процентов
    # Выводим результаты на экран
    income_var.set(f"Доход: {total_amount - principal:.2f}")   # Выводим доход
    total_amount_var.set(f"Сумма в конце срока вклада: {total_amount:.2f}")  # Выводим сумму в конце срока
# Создаем главное окно
window = Tk()
window.title("Калькулятор дохода по вкладу")
# Создаем и размещаем виджеты
principal_label = Label(window, text="Сумма вклада")
principal_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
principal_entry = Entry(window)
principal_entry.grid(row=0, column=1, padx=10, pady=10)
duration_label = Label(window, text="Срок в днях")
duration_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
duration_entry = Entry(window)
duration_entry.grid(row=1, column=1, padx=10, pady=10)
rate_label = Label(window, text="Процентная ставка")
rate_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
rate_entry = Entry(window)
rate_entry.grid(row=2, column=1, padx=10, pady=10)
interest_type_label = Label(window, text="Схема начисления процентов")
interest_type_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
# Используем переключатели RadioButtons для выбора схемы
interest_type_var = StringVar()
simple_interest_radio = Radiobutton(window, text="Простые проценты", variable=interest_type_var, value="Простые проценты")
simple_interest_radio.grid(row=4, column=0, padx=10, pady=10, sticky="w")
compound_interest_radio = Radiobutton(window, text="Сложные проценты", variable=interest_type_var, value="Сложные проценты")
compound_interest_radio.grid(row=5, column=0, padx=10, pady=10, sticky="w")
interest_type_var.set("Простые проценты")
calculate_button = Button(window, text="Вычислить", command=calculate_interest)
calculate_button.grid(row=6, column=0, columnspan=2, pady=20)
income_var = StringVar()
income_label = Label(window, textvariable=income_var)
income_label.grid(row=7, column=0, columnspan=2)
total_amount_var = StringVar()
total_amount_label = Label(window, textvariable=total_amount_var)
total_amount_label.grid(row=8, column=0, columnspan=2, pady=10)
# Запускаем цикл событий
window.mainloop()
