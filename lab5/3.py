treasure_map = []
n = int(input("Количество сокровищ: \n"))
print("Координаты сокровищ: ")
for i in range(n):
    treasure_map.append(input().split())
sanya = [input("Координаты Александра: \n").split()]
x = 0
y = 0
min_len = 666
for i in treasure_map:
    k = (int(i[0])**2 + int(i[1])**2)**0.5
    if k < min_len:
        min_len = k
        x = i[0]
        y = i[1]
print(int(x),int(y))
