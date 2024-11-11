e = open("file4.txt","r",encoding="utf8")
k = e.readlines()
first = 0
second = 0
for i in k:
    z = i.split(' ')
    if int(z[2]) > int(first): first = z[2]
    elif int(z[2]) > int(second) and int(z[2]) < int(first): second = z[2]
for i in k:
    if str(second) in i:
        print("".join(i))
        break
e.close()
