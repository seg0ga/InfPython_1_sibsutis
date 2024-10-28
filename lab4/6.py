import random as r
k = 3
var = "ОР"
s = [r.choice(var),r.choice(var),r.choice(var)]

while True:
    if s[-1] == s[-2] and s[-1] == s[-3]:
        print(f"{" ".join(s)} (Попыток: {k})")
        break
    else:
        k+=1
        s.append(r.choice(var))
