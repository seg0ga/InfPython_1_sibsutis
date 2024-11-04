s = []
n = int(input())
m = int(input())
for i in range(n):
    s.append([])
    if i == 0:
        s[0].append("1")
        for j in range(1,m):
            s[0].append("     1")
    else: s[i].append("1")
for i in range(1,n):
    for j in range(1,m):
        a = str(int(s[i-1][j]) + int(s[i][j-1]))
        while len(a) < 6:
            a = " "+a
        s[i].append(a)
for i in s:
    print("".join(i))
