a = input().split(" ")
b = a[-1].split(":")
if len(a) == 2:
    c = a[0].split("-")
else:
    z = ""
    for i in a[0:-1]:
        z+=i + " "
    c = z.split("-")
if int(b[0]) > int(b[1]):
    print(c[0])
elif int(b[0]) < int(b[1]):
    print(c[1])
else:
    print("Ничья")
