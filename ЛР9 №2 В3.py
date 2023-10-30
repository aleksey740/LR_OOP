import math
#Класс для точек на плоскости
class PointPL:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#Класс для точек в пространстве
class PointPR:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
#Полиморфный метод для вычисления расстояния между двумя точками
def calculate_distance(point1, point2):
    if isinstance(point1, PointPL) and isinstance(point2, PointPL):
        #Вычисляем расстояние по формуле для плоскости
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    elif isinstance(point1, PointPR) and isinstance(point2, PointPR):
        #Вычисляем расстояние по формуле для пространства
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2 + (point1.z - point2.z)**2)
    else:
        #Если точки разных размерностей
        raise ValueError("Невозможно вычислить расстояние между точками разных размерностей.")
#Пример использования
point_pl_1 = PointPL(1, 2)
point_pl_2 = PointPL(4, 6)
distance_pl = calculate_distance(point_pl_1, point_pl_2)
print(f"Расстояние между двумя 2D точками: {distance_pl}")
point_pr_1 = PointPR(1, 2, 3)
point_pr_2 = PointPR(4, 6, 8)
distance_pr = calculate_distance(point_pr_1, point_pr_2)
print(f"Расстояние между двумя 3D точками: {distance_pr}")
