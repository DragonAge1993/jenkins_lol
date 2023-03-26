# a = 10
# for i in range(2):
#     a -= 2
#     print(a)

# print(4, end="")
# for i in range(4,1,-1):
#     print(2*i, end="")

# a = 4
# for i in range(4):
#     a += a
#     print(a)

# i = ""
# print(i, end="")
# for i in range(3,6):
#     print(i,end="")

# for i in range(3,1,-1):
#     print(i, end="")

# a = 2
# for i in range(3):
#     a += i
#     print(a)

# a = 10
# for i in range(5):
#     a -= i
#     print(a)



# print(4, end="")
# for i in range(3,1,-1):
#     print(2*i, end="")


# a = 2
# for i in range(5):
#     a += i
#     print(a, end="")

# a = 10
# for i in range(5):
#     a -= i
#     print(a)

# i = ""
# print (i, end="" )
# for i in range(3,6):
#     print (i, end="" )


# a = 4
# for i in range(3):
#     a += a
#     print(a, end="")

# a = 10
# for i in range(2):
#     a -= 1
#     print(a, end="")


# for i in range(3,0,-1):
#     print (i, end="" )

# Что выведет программа при вводе 362
# n = int(input())
# p = 1
# i = 0
# while p < n:
#     p =p* 2
#     i += 1
# print(i)

# Чему будет равно значение целой переменной «a» после выполнения этого фрагмента программы?

# a = 10
# for i in range(4):
#     a -= i
#     print(a)


# for i in range(2,0,-1):
#     print ( i, end="" )

# i = ""
# print ( i, end="" )
# for i in range(4,8):
#     print ( i, end="" )

# a = 10
# for i in range(2):
#     a -= 1
#     print(a)


# a = 3
# for i in range(3):
#     a += a
#     print(a)


# print(4, end="")
# for i in range(3,0,-1):
#     print(2*i, end="")


# a = 3
# for i in range(3):
#     a += a
#     print(a)


# print(i, end="")
# for i in range(4,1,-1):
#     print(i, end="")


# a = 2
# for i in range(5):
#     a += i
#     print(a)

# a = 10
# for i in range(5):
#     a -= i
#     print(a)


# b = int(input())
# h = int(input())
# # Выводите результат через print()

# c = (b * h)/2
# print(c)


# Число n можно считать так:
# n = int(input())
# k = int(input())

# c = k / n
# c1 = k // n
# c2 = k % n

# # print(c)
# print(c1)
# print(c2)


# Выводите результат через print()

# Пример на деление, вычисление частного и остатка:


# Задача «Электронные часы»
# Условие
# Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). Учтите, что число n может быть больше, чем количество минут в сутках.

m = int(input())
chas = m // 60
# print(chas)
lokek = int(chas)
minut = m % 60
chas_v_sutkax = 24 * 60
chas_v_sutkax_int = int(chas_v_sutkax)
lolkek2 = int(minut)
if lokek < 24:
    chas = m // 60
    print(lokek)
# else:
#     print("0")
if lokek == 24:
    print("0")
if m > chas_v_sutkax:
    chas2 = (m - chas_v_sutkax_int) / 60
    chas3 = int(chas2)
    print(chas3)
# if lokek > 48:
#     chas2 = (m // 60) - 48
#     chas3 = int(chas2)
#     print(chas3)
# else:
#     print("0")
print(lolkek2)