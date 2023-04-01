# Условие
# Даны три целых числа. Определите, сколько среди них совпадающих. 
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

a = int(input())
b = int(input())
c = int(input())

if a == b and c == b and a == c:
    print("3")
elif a == b and b == a or a == c and c == a or b == c and c == b:
    print("2")
elif a != b and c != b and a != c:
    print("0")
elif a == b or c == b or a == c:
    print("1")

