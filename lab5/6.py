n = int(input())
s = []
k = n-1
for i in range(n):
    s.append(input().split())
for i in range(n):
    z = s[i][i]
    s[i][i] = s[k][i]
    s[k][i] = z
    k-=1
for j in s:
    print(" ".join(j))
