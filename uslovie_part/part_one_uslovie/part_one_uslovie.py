# i = int(input())
# if i > 0:
#     print(i)
# else:
#     print(-i)

# i = int(input())
# if i < 0:
#     i = -i
#     print(i)

# i = int(input())
# y = int(input())
# if i > 0:
#     if y > 0:
#         print("Первая четверть!")
#     else:
#         print("Вторая четверть!")
# else:
#     if y > 0:
#         print("Третья четверть!")
#     else:
#         print("Четвртая чертверть!")

# a = int(input())
# b = int(input())
# c = a % 10 == 0
# c1_float = int(c)
# y1 = b % 10 == 0
# y1_float = int(y1)
# if c1_float or y1_float:
#     print(f"Делится на 10 без остатка, результат: {c1_float} and {y1_float}")
# else:
#     print(f"На цело не делится, результат: {c1_float} and {y1_float}")


x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("Первая четверть!")
elif x > 0 and y < 0:
    print("Вторая четверть!")
elif x < 0 and y > 0:
    print("Третья четверть!")
else:
    print("Четвертая четверть!")
