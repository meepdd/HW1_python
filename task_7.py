"""
Для данного числа n<100 закончите фразу “На лугу пасется...”
одним из возможных продолжений: “n коров”, “n корова”,
“n коровы”, правильно склоняя слово “корова”.
"""


n = int(input())  # Числовое значение
if n >= 11 and n <= 14:
        print(n, 'korov')
else:
        b = n % 10
        if b == 0 or (b >= 5 and b <= 9):
                print(n, 'korov')
        if b == 1:
                print(n, 'korova')
        if b >= 2 and b <= 4 :
                print(n, 'korovy')