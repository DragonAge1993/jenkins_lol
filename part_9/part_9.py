# Излишняя автоматизация
# «Повторение — мать учения!» и «Если это можно автоматизировать — автоматизируй!»
# Этим принципам следуют многие программисты. Но что будет, если их объединить?

# Формат ввода
# Одна строка — весьма полезная информация.

# Формат вывода
# Трижды повторённая весьма полезная информация.


# Ввод
# 2 + 2 = 4

# Вывод
# 2 + 2 = 4
# 2 + 2 = 4
# 2 + 2 = 4
i = 0
a = input("")
while i < 3:
    print(a)
    i += i + 1
