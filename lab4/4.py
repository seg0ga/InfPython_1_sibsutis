s = []
bol = []
men = []
rav = []
a = 1
sum_all = 0
while a != "":
    a = input()
    if a != "":
        s.append(int(a))
        sum_all+=int(a)
sr_znach = sum_all/len(s)
for i in s:
    if i < sr_znach:men.append(str(i))
    elif i > sr_znach:bol.append(str(i))
    else:rav.append(str(i))
print("Меньше: "," ".join(men))
print("Больше: "," ".join(bol))
if len(rav) > 0: print("Равно: "," ".join(rav))
