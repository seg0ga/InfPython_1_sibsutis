e = open("file6.txt","r",encoding="utf8")
k = e.readlines()
count_vsego = 0
count_e = 0
for i in k:
    i = i.split(" ")
    for j in i:
        count_vsego+=1
        if "e" in j or "E" in j:
            count_e+=1
print(count_e*100/count_vsego)
e.close()
