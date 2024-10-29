digit = []
alpha = []

s = input().split()

while len(s) != 0:
    if str(s[0]).isdigit():
        digit.append(s[0])
    else:
        alpha.append(s[0])
    s.pop(0)
print(" ".join(digit))
print(" ".join(alpha))
