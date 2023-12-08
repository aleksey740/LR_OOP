# Запрашиваем у пользователя ввод дня, месяца и года
day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

# Инициализируем переменную для проверки корректности даты
is_valid_date = True

# Проверяем корректность месяца
if month < 1 or month > 12:
    is_valid_date = False
# Проверяем корректность дня в зависимости от месяца
elif day < 1:
    is_valid_date = False
# Проверяем дни для февраля в случае високосного и не високосного года
elif month == 2:
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        if day > 28:
            is_valid_date = False
    elif day > 29:
        is_valid_date = False
# Проверяем количество дней для апреля, июня, сентября и ноября
elif month in (4, 6, 9, 11) and day > 30:
    is_valid_date = False
# Проверяем количество дней для остальных месяцев
elif day > 31:
    is_valid_date = False

# Определяем количество дней в каждом месяце
days_in_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
day_number = sum(days_in_month) + day

# Выводим результаты на основе проверки корректности даты
if is_valid_date:
    print("Дата корректна")
    print("Номер дня с начала года:", day_number)
else:
    print("Некорректная дата")
