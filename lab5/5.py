n = int(input("Введите n: "))
m = int(input("Введите m: "))
s = []
s_new = []
for i in range(n):
    s.append([])
    for j in range(m):
        print(f"Введите [{i+1}][{j+1}]: ")
        s[i].append(input())
for i in range(m):
    s_new.append([])
    for j in range(n):
        s_new[i].append(s[j][i])
for i in s_new:
    print(" ".join(i))
