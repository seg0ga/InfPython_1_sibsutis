s = []
a = 1
while a!= 0:
    a = int(input())
    if a == 0:
        break
    if a>0:
        s.append(a)
if len(s) < 2:
    print("Некого сравнивать")
else:
    print("Самый большой рост - ",max(s))
    print("Самый маленький рост - ",min(s))
