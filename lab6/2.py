e1 = open("file5.txt","r",encoding="utf8")
k1 = e1.readlines()
e2 = open("file6.txt","r",encoding="utf8")
k2 = e2.readlines()
flag5 = 0
flag6 = 0
for i in k1:
    if "Academy" in i:
        flag5 = 1
for i in k2:
    if "Academy" in i:
        flag6 = 1

if flag5 == 1 and flag6 == 1:
    print("В обоих")
elif flag6 == 1:
    print("В шестом")
elif flag5 == 1:
    print("В пятом")
else:
    print("В файлах нет слова")
e1.close()
e2.close()
