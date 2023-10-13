class Potato:
    """
    Класс картошки.
    """
    def __init__(self, number):
        """
        Создание объекта Potato.
        """
        self.number = number
        self.stage = 0
    def potstage(self):
        """
        Возвращает текущую стадию зрелости.
        """
        stages = ["Росток", "Зелёная", "Зрелая"]
        return stages[self.stage]
    def grad(self):
        """
        Увеличивает стадию зрелости картошки на одну.
        """
        if self.stage < 2:
            self.stage += 1