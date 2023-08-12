i = int(input())
y = int(input())
if i < 1000 and y < 1000:
    if i > y:
        c = i - y
        vyvod = int(c)
        print(vyvod)
    if y > i:
        c = y - i
        vyvod1 = int(c)
        print(vyvod1)
    if i == y:
        print("Равны")