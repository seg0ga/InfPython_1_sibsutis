import random
def game():
    secret = random.randint(1, 10)

    print("Хорошо, я загадал число. Попробуй его отгадать")
    k = 1
    while 1:
        num = int(input(f"{k} "))
        k += 1

        if num == secret:
            print("Поздравляю! Вы угадали!")
            break
        else:
            if num > secret:
                print("Нее, ты не угадал. Попробуй снова. Число меньше.")
            else:
                print("Нее, ты не угадал. Попробуй снова. Число больше.")
    z = input("Хотите сыграть еще раз?(д/н)")
    if z == "д":
        game()

game()
