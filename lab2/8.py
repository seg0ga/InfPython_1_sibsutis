bin = input()
dec = 0
step = 0
for i in range(len(bin)-1,-1,-1):
    if bin[i] == "1":
        dec+= 2**step
    step+=1
print(dec)
