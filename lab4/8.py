a = int(input())
s = []
s_new = []
for i in range(a):
    s.append(input())
for i in s:
    if len(i)>10:
        s_new.append(i[0]+str(len(i)-2)+i[-1])
    else:
        s_new.append(i)
for i in s_new:
    print(i)
