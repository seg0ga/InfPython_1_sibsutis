a = input()
s = a.split("/")
a1 = 0
a2 = 0
a3 = 0

def kolvo(x):
    m = 0
    glas = "ёуеоаэыяиюЁУЕЭОАЫЯИЮ"
    for i in glas:
        m+= x.count(i)
    return m

if len(s) < 3 or len(s) > 3:
    print("Не хайку, должно быть 3 строки")
else:
    if kolvo(s[0]) == 5 and kolvo(s[1]) == 7 and kolvo(s[2]) == 5:
        print("Хайку")
    else:
        print("Не хайку")



#Вечер за окном. / Еще один день прожит. / Жизнь скоротечна...
