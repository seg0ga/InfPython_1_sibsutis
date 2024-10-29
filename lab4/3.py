s = input().split()
m = ""
for i in range(1,len(s)):
    if s[i] > s[i-1]:
        m+= str(s[i]) + " "
print(m)
