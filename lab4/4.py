s = input().split()
bol = []
men = []
rav = []
sum_all = 0
for  i in s:
    sum_all+=int(i)
sr_znach = sum_all/len(s)
for i in s:
    if int(i) < sr_znach:men.append(str(i))
    elif int(i) > sr_znach:bol.append(str(i))
    else: rav.append(str(i))
print("Меньше: "," ".join(men))
print("Больше: "," ".join(bol))
if len(rav) > 0: print("Равно: "," ".join(rav))
