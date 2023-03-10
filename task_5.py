"""
Решить в целых числах уравнение ax + b = 0
Чтобы решить уравнение ax + b = 0 в целых числах, мы можем использовать основы алгебры,
чтобы выделить x и решить для него. Решение дается в виде:
x = -b / a
Если a делит b поровну, то уравнение имеет решение в целых числах, в противном случае - нет.
"""

a = int(input())  # Вводим числовые значения
b = int(input())

if (a == 0 and b == 0):  # Если a = 0 and b = 0 -> inf
    print('INF')
elif (a == 0 or (b % a) != 0):  # Если a = 0 or b % a != 0 -> inf
    print('NO')
else:
    print(int(-b / a))  # Иначе выводим это добро
