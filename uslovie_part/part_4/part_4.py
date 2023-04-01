# Условие
# Даны три целых числа. Выведите значение наименьшего из них.

i = int(input())
y = int(input())
z = int(input())

a = []
a.append(i)
a.append(y)
a.append(z)
# print(a)
min_list = min(a)
print(min_list)

# if i < y and i < z:
#     print(i)
# if y < i and y < z:
#     print(y)
# if z < i and z < y:
#     print(z)
# if i == y or y == z or i == z:
#     print(i)


# if i > y and i > z and y < i and z < i:
#     print(i)
# if y > i and y > z and i < y and z < y:
#     print(y)
# if z > i and z > y and i < z and y < z:
#     print(z)