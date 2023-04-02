# Условие
# Шахматная ладья ходит по горизонтали или вертикали. 
# Даны две различные клетки шахматной доски, определите, может ли ладья попасть 
# с первой клетки на вторую одним ходом. 
# Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, 
# потом для второй клетки. Программа должна вывести YES, если 
# из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = (a + b + c + d) % 2
# print(result)
# if a > 0 or a <= 8 and b > 0 or b <= 8 and c > 0 or c <= 8 and d > 0 or d <= 8 and result == 0:
#     print("NO")
# else:
#     print("YES")
#     # print("Вы ввели не корректное число")

while a > 0 and a <= 8 and b > 0 or b <= 8 and c > 0 or c <= 8 and d > 0 or d <= 8 and result == 0:
    print("NO")
else:
    print("YES")