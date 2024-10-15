a = input("Введите номер: ")
if a[0:3].isalpha() and a[3:6].isdigit() and len(a) == 6:
    print("Старый формат")

elif a[0:4].isdigit() and a[4:7].isalpha() and len(a) == 7:
    print("Новый формат")
else:
    print("Ну где-то ошибка")
