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
    if i < sr_znach:men.append(i)
    elif i > sr_znach:bol.append(i)
    else:rav.append(i)
print("Меньше: ",men)
print("Больше: ",bol)
if len(rav) > 0: print("Равно: ",rav)
