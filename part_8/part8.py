list_one = [3,10,25,12]
a=list_one[0]
b=list_one[1]
c=list_one[2]
d=list_one[3]

print(list_one)
# Кратно 5 должно быть
a1=a // 5
print(a1)
b1=b // 5
print(b1)
c1=c // 5
print(c1)
# print(x)
d1=d // 5
print(d1)

two_list = [a1,b1,c1,d1]
print(two_list)
max_number = max(two_list)
print("Наибольшее число в целочисленном дилении на 5:", max_number) # В списке [a1,b1,c1,d1]


max_number_now = max(list_one) # В списке [3,10,25,12]
print("Наибольшее число которое спокойно поделилось на и оставило целочисленное на 5:", max_number_now)
