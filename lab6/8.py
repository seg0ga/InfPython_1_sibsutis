z = input()
z = z.split(" ")
matrix = []
flag = True
for i in range(int(z[0])):
    if i%2 == 0:
        matrix.append("# "*int(z[1]))
    else:
        if flag == True:
            st = ". " * (int(z[1])-1) + "# "
            flag = False
        else:
            st = "# " + ". " * (int(z[1]) -1)
            flag = True
        matrix.append(st)
for i in matrix:
    print(i)
