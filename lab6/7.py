import random as r
k = open("for7.txt","r",encoding="utf8")
z = k.readlines()
while True:
    password = ""
    first = (r.choice(z)[:-1]).capitalize()
    second = (r.choice(z)[:-1]).capitalize()
    if len(first) >= 3 and len(second) >= 3:
        password += first + second
    else: break
    if len(password) >= 8 and len(password) <= 10:
        print(password)
        break
k.close()
