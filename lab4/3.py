s = []
a = 1
m = ""
while a != "":
    a = input()
    if a != "": s.append(int(a))
for i in range(1,len(s)):
    if s[i] > s[i-1]:
        m+= str(s[i]) + " "
print(m)
