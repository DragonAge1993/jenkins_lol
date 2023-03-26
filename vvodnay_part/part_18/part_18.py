# Один малыш из детского сада услышал от старшей сестры о некоем действии с числами — сложении.
# И как это часто бывает — он не до конца разобрался, как работает сложение. Например, не совсем понял, как произвести перенос разряда.
# Теперь он хочет научить сложению остальных ребят и просит написать программу, которая поможет ему в качестве наглядного материала.

# Формат ввода
# В первой и второй строках записаны натуральные числа меньше 1000.

# Формат вывода
# Одно число — результат сложения введённых чисел без учёта переносов.

# Находим длину строки в Python с помощью функции len()
# str = 'otus'
# print(len(str)) 

# n1 = int(input())
# n2 = int(input())
# p = 1
# n3 = 0
# for _ in range(3):
#     n3 += (n1 + n2)%10*p
#     p *= 10
#     n1 //= 10
#     n2 //= 10
# print(n3)
 
# # поразрядно (строки)
# *n1, = map(int, input().zfill(3))
# *n2, = map(int, input().zfill(3))
# for i in range(len(n1)):
#     n2[-i-1] = (n1[-i-1] + n2[-i-1])%10
# print(int(''.join(map(str, n2))))


# public static int add(int a, int b)  {
#   if (b == 0) return a;
#   int sum = a ^ b;      // добавляем без переноса
#   int carry = (a & b) << 1;  // перенос без суммирования
#   return add(sum, carry);    // рекурсия
# }



# В первой и второй строках записаны натуральные числа меньше 1000.
# Формат вывода
# Одно число — результат сложения введённых чисел без учёта переносов.


i = int(input())
y = int(input())
list_one = ''
list_two = ''
str1 = str(i)
str2 = str(y)
max_lenght1 = len(str1)
max_lenght2 = len(str2)
print(max_lenght1)
print(max_lenght2)

lokek_cheburek = list(str1)
lokek_cheburek1 = list(str2)

print(lokek_cheburek)
print(lokek_cheburek1)


if i < 1000 and y < 1000:
    if max_lenght1 > max_lenght2:
        list_one = lokek_cheburek[1]+lokek_cheburek1[1]
        list_two = lokek_cheburek[0]+lokek_cheburek1[0]
        # stroka_1 = str(list_one)
        # stroka_2 = str(list_two)
        print(list_one)
        print(list_two)
        
        # print(f"{stroka_1}{stroka_2}")


# str1 = str(i)
# str2 = str(y)
# max_len1 = len(str1)
# max_len2 = len(str2)

# print(str1[0])
# print(str1[1])
# print(str1[2])

# print(str2[0])
# print(str2[1])


# if i < 1000 and y < 1000:
#     # if i > y:
#     if max_len1 > max_len2:
#         vyvod_str = str1[1]+str2[1]
#         print(vyvod_str)
#         vyvod_str1 = str1[0]+str2[0]
#         print(vyvod_str1)
#         print(f"{vyvod_str}{vyvod_str1}")
#         # print(vyvod_str)
#     if max_len1 == max_len2:
#         vyvod_str = str1[2]+str2[2]+str1[1]+str2[1]+str1[0]+str2[0]
#         print(vyvod_str)
# else:
#     print("Вы ввели не коректное значение i и y должно быть < 1000")
