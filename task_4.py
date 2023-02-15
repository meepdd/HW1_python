"""
Дано число Х. Требуется перевести это число в римскую систему счисления.
Условие: 1 <= x <= 100
"""

x = int(input())    # Вводим числовые значения
if 1 <= x <= 100:
    roman_num = ""
    roman_num += "C" * (x // 100)
    roman_num += "XC" if x % 100 >= 90 else "L" * ((x % 100) // 50)
    roman_num += "XL" if x % 50 >= 40 else "X" * ((x % 50) // 10)
    roman_num += "IX" if x % 10 == 9 else "V" * ((x % 10) // 5)
    roman_num += "IV" if x % 5 == 4 else "I" * (x % 5)
    print(roman_num)
else:
    print("Число не в пределах ограничений")

