n = int(input())
s = []
for i in range(n):
    s.append([])
    print(f"Введите {i+1} ряд: ")
    s[i].append("".join(input().split()))
f = int(input())
k = 0
for j in s:
    k += 1
    if ("0"*f) in j[0]:
        print(k)
        break
