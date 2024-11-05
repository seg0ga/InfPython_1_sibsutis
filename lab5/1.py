def func(x):
    return x ** 2 / (10 + x ** 3)

def integral(n):
    a = -2
    b = 5
    f = []
    i = a
    h = (b - a) / n
    while i < b:
        f.append(func(i))
        i += h
    sum = (f[0] + f[-1])/2
    for i in f[1:-1]:
        sum += i
    sum*=h
    print(f"{sum:.2f}")

n = [10,100,1000]
for i in n:
    integral(i)
