a = input()
f_part = ""
s_part = ""
k = 2
if a[-1] == "#":
    for i in a[:-1]:
        if k %2 == 0:
            f_part += i
        else:
            s_part = i + s_part
        k+=1
    print(f_part+s_part)
else:
    print("Ошибка! Отсутствует символ #")
