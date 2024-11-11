s = input("Введите строку: ")
z = open("for5.txt","r")
k = z.readlines()
z.close()
if len(k)%2 == 0:
    k = k[0:int((len(k)/2))] + [s+"\n"] + k[(int(len(k)/2)):]
else:
    k = k[0:int((len(k) // 2))] + [s + "\n"] + k[(int(len(k) // 2)):]
z = open("for5.txt","w")
for i in k:
    z.write(i)
z.close()
