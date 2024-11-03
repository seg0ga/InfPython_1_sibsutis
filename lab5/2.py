import random as r
magic_kv = [["2","7","6"],
            ["9","5","1"],
            ["4","3","8"]]

if r.randint(0,1):
    s = magic_kv[0]
    magic_kv[0]=magic_kv[2]
    magic_kv[2]=s
if r.randint(0,1):
    s = [magic_kv[0][2],magic_kv[1][2],magic_kv[2][2]]
    for i in range(3):
        magic_kv[i][2]=magic_kv[i][0]
        magic_kv[i][0] = s[i]

for i in magic_kv:
    print(" ".join(i))
