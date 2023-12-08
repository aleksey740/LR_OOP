import math

x = float(input("Введите x координату точки M:"))
y = float(input("Введите y координату точки M:"))

n = math.sqrt(x**2 + y**2)

print("Расстояние от точки M до начала координат:",n)
