# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

# мое решение
n = int(input('Введите число: '))
i = 0
number = 0
while i <= n and number * 2 <= n:
    number = 2 ** i
    print (number,end = ' ')
    i += 1

# решение в интернете
# n = int(input('Введите число: '))
# m=1

# while m <= n:
#     print(i)
#     m = m * 2
    