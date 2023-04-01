i = int(input())
y = int(input())
z = int(input())
l = int(input())

str_one = i + y + z + l
str_two = str_one % 2
if str_two == 0:
    print("YES")
else:
    print("NO")
