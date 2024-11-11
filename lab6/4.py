col = int(input("Введите количество имен: "))
gender = input("Введите гендер: ")
if col < 0 or gender not in "МмЖж":
    print("Неверные значения")
else:
    if gender in "Мм":
        e = open("file8.txt","r",encoding="utf8")
        k = e.readlines()
    else:
        e = open("file7.txt","r",encoding="utf8")
        k = e.readlines()
    for i in range(col):
        print(k[i].split()[0])
e.close()
