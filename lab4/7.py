a = input()
k = 0
chet = 0
nechet = 0
for i in a:
    k+=1
    if k%2==0:
        chet+=int(i)
    else:
        chislo = int(i)*2
        if chislo > 9:
            chislo-=9
        nechet += chislo
if len(a) != 16:
    print("Некорректный номер")
elif (chet+nechet)%10 == 0:
    print("Корректный номер")
else:
    print("Некорректный номер")
