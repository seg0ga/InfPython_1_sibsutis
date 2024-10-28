z = int(input())
s = []
a = "1"
while a != "":
    a = input()
    if a != "" :s.append(int(a))
s.append(z)
s.sort()
k = len(s)
for i in range(0,len(s)-1):
    if s[i] == z:
        print(k)
        break
    k-=1
