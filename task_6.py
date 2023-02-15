"""
Даны действительные числа a,b,c. Найдите все решения квадратного
уравнения
"""

a = int(input())
b = int(input())
c = int(input())

d = (b ** 2) - (4 * a * c)
line = 2 * a

if d == 0:
    print(-b / (2 * a))
elif d > 0:
    print((-b + (d ** (1 / 2))) / line,
          (-b - (d ** (1 / 2)/ line) ))
