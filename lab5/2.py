import random as r

while True:
    m = []
    for i in range(3):
        m.append([0] * 3)

    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            m[i][j] = r.choice(number)
            number.remove(m[i][j])
    if m[2][0] + m[1][1] + m[0][2] == 15 and \
            m[0][0] + m[1][1] + m[2][2] == 15 and \
            m[0][0] + m[0][1] + m[0][2] == 15 and \
            m[1][0] + m[1][1] + m[1][2] == 15 and \
            m[2][0] + m[2][1] + m[2][2] == 15 and \
            m[0][0] + m[1][0] + m[2][0] == 15 and \
            m[0][1] + m[1][1] + m[2][1] == 15 and \
            m[0][2] + m[1][2] + m[2][2] == 15:
        for i in range(3):
            for j in range(3):
                print(m[i][j], end=" ")
            print()
        break
