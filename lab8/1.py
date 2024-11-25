n = int(input())
sostav = {}
captain = []
woman_child = []
man = []
def printsostav(a):
    for i in a:
        print(i)

for i in range(n):
    a = input().split()
    sostav[a[0]]=a[1]
for i in sostav:
    if sostav.get(i) == "captain":
        captain.append(i)
    elif sostav.get(i) == "woman" or sostav.get(i) == "child":
        woman_child.append(i)
    elif sostav.get(i) == "man":
        man.append(i)
    else:continue

printsostav(woman_child)
printsostav(man)
printsostav(captain)
