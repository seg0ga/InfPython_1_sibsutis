n = int(input())
if n <= 0:
    print("Ошибка!")
else:
    k = 0
    for i in range(n):
        if (i+1) <= 2:
            k+=10.5
        else:
            k+=4
    print(k)
