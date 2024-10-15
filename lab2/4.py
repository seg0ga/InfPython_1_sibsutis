n = int(input())
l = n-1
k = 1
for i in range(n):
    print(" "*l,"#"*k)
    l-=1
    k += 2
print(" "*(n-1),"#")
