"""
Даны координаты двух точек на плоскости, требуется определить, лежат ли они в одной
координатной четверти или нет (все координаты отличны от нуля)
"""

x = int(input())   # Вводим числовые значения
y = int(input())
z = int(input())
g = int(input())

if (x > 0 and y > 0) and (z > 0 and g > 0):   # Перебираем все условия нахождения в одной четверти (А так не говнокод ли?)
    print("Yes")
elif (x < 0 and y < 0) and (z < 0 and g < 0):
    print("Yes")
elif (x < 0 and y > 0) and (z < 0 and g > 0):
    print("Yes")
elif (x > 0 and y < 0) and (z > 0 and g < 0):
    print("Yes")
else:
    print("No")
