b = input()
if len(b) == 6:
    if (int(b[0])+int(b[1])+int(b[2])) == (int(b[3])+int(b[4])+int(b[5])):
        print("Поздравляю, ваш билет - счастливый")
    else:
        print("Обычный билет")
else:
    print("Некорректный билет")
