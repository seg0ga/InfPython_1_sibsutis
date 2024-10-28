a = int(input())
k = 0
for i in range(a):
    s = input().split()
    if int(s[1])-int(s[0]) >= 2:
        k+=1
print(k)
