#Импорт класса PotatoGrad из модуля potato_grad
from potato_grad import PotatoGrad
#Создание класса PotatoGrad с параметром 5, означает начальное количество картошки.
potato_grad = PotatoGrad(5)
#Итерация 3 раза для моделирования роста и созревания картошки.
for _ in range(3):
    #Вызов метода grad_potatoes() для обновления состояния картошки
    potato_grad.grad_potatoes()
    #Вывод информации о текущей стадии роста.
    for potato in potato_grad.potatoes:
        print(f"Картошка {potato.number} сейчас {potato.potstage()}")
    #Проверка все ли картошки растения созрели.
    if potato_grad.check():
        print("Вся картошка созрела. Можно собирать!")
    else:
        print("Картошка ещё не созрела!")
    # Вывод пустой строки для разделения вывода между итерациями.
    print()
