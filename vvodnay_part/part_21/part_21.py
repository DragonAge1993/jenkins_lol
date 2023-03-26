# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!).

# 1534

# The next number for the number 1534 is 1535.
# The previous number for the number 1534 is 1533.

chislo_int = int(input())

next_chislo = chislo_int + 1
chislo_int_input = str(chislo_int)
chislo_int1 = int(next_chislo)
chislo_int1_str = str(next_chislo)
pred_chislo = chislo_int - 1
chislo_int2 = int(pred_chislo)
chislo_int2_str = str(pred_chislo)

print("The next number for the number ", chislo_int_input + " is " + chislo_int1_str)
print("The previous number for the number ",chislo_int_input + " is " + chislo_int2_str)