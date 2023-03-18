list_one = [3,10,25,12]
a=list_one[0]

b=list_one[1]
c=list_one[2]
d=list_one[3]
a1=a // 5
print(a1)
b1=b // 5
print(b1)
c1=c // 5
print(c1)
d1=d % 5
print(d1)
if (a > b) & (a > c) & (a > d):
    print("Максимальное число A", a)
else:
    print("A не максимаальное число", a)
if b > a and b > c and b > d:
    print("Максимальное число B", b)
else:
    print("B не максимаальное число", b)
if c > a and c > b and c > d:
    print("Максимальное число A", a)
else:
    print("A не максимаальное число", a)
if d > a and d > b and d > c:
    print("Максимальное число D", d)
else:
    print("d не максимаальное число", d)
