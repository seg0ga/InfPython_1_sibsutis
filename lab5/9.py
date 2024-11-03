import random as r
s = [[".",".",".","."],
     [".",".",".","."],
     [".",".",".","."],
     [".",".",".","."]]
count_boats = 0
flag_bomb = 1
steps = 0
boats = []
while len(boats) < 4:
    k = str(r.randint(1,4))+str(r.randint(1,4))
    if k not in boats:
        boats.append(k)
bomb = ""
while True:
    k = str(r.randint(1,4))+str(r.randint(1,4))
    if k not in boats:
        bomb+=k
        break
while True:
    steps += 1
    z = "".join(input().split())
    if z == bomb:
        print("Вы попали в бомбу")
        break
    if z in boats:
        s[int(z[0])-1][int(z[1])-1]="X"
        count_boats+=1
    for i in s:
        print(" ".join(i))
    if count_boats == 4:
        print("Вы победили!")
        print(steps)
        break
