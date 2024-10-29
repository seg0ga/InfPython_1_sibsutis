z = int(input())
s_1 = input().split()
s = []
for  i in s_1:
    s.append(int(i))
s.append(z)
s.sort()
k = len(s)
for i in range(0,len(s)-1):
    if s[i] == z:
        print(k)
        break
    k-=1
