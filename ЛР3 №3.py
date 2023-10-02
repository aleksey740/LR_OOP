def words_a(text):
    #Разбиваем текст на слова, используя пробел как разделитель.
    words = text.split()

    #Инициализируем счетчик слов, начинающихся с буквы a.
    count_a_words = 0

    #Перебираем каждое слово в тексте.
    for word in words:
        #Проверяем, начинается ли слово с буквы a.
        if word.lower().startswith('а'):
            count_a_words += 1

    return count_a_words

#Просим пользователя ввести текст.
user_text = input("Введите текст: ")

#Вызываем функцию для подсчета слов.
result = words_a(user_text)

#Выводим результат
print("Количество слов, начинающихся с буквы 'a':", result)
