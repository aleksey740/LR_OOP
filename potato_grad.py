from potato import Potato
class PotatoGrad:
    """
    Класс грядки.
    """
    def __init__(self, num_potatoes):
        """
        Создание объекта PotatoGrad.
        """
        self.potatoes = [Potato(i) for i in range(1, num_potatoes + 1)]
    def grad_potatoes(self):
        """
        Увеличение стадии зрелости.
        """
        for potato in self.potatoes:
            potato.grad()
    def check(self):
        """
        Проверка зрелости картошки.
        """
        for potato in self.potatoes:
            if potato.potstage() != "Зрелая":
                return False
        return True