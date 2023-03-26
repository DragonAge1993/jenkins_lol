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

n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)