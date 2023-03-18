list_one = [3,10,25,12]
a=list_one[0]
b=list_one[1]
c=list_one[2]
d=list_one[3]
# Кратно 5 должно быть
a1=a // 5
print(a1)
b1=b // 5
print(b1)
c1=c // 5
print(c1)
d1=d // 5
print(d1)

# Сравниваем список
if a > b and a > c and a > d:
    print("Максимальное число A", a)
else:
    print("A не максимаальное число", a)
if b > a and b > c and b > d:
    print("Максимальное число B", b)
else:
    print("B не максимаальное число", b)
if c > a and c > b and c > d:
    print("Максимальное число C", c)
else:
    print("A не максимаальное число", a)
if d > a and d > b and d > c:
    print("Максимальное число D", d)
else:
    print("d не максимаальное число", d)

# Сравниваем полученный результат и получаем вывод

if a1 > b1 and a1 > c1 and a1 > d1:
    print("Максимальное число A", a)
else:
    print("A1 не максимаальное число", a1)
if b1 > a1 and b1 > c1 and b1 > d1:
    print("Максимальное число B", b)
else:
    print("B1 не максимаальное число", b1)
if c1 > a1 and c1 > b1 and c1 > d1:
    print("Максимальное число C1", c1)
else:
    print("A не максимаальное число", a)
if d1 > a1 and d1 > b1 and d1 > c1:
    print("Максимальное число D", d1)
else:
    print("d1 не максимаальное число", d1)
