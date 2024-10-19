import random

a = int(input("Введите длину пароля: "))
big = "QWERTYUIOPASDFGHJKLZXCVBNM"
low = "qwertyuiopasdfghjklzxcvbnm"
digits = "0123456789"
spec = "[];'|<>?/*&^%$#@!"
all = ""
password = ""
if input("Нужны ли заглавные буквы? ").lower() == "да":
    all+=big
if input("Нужны ли строчные буквы? ").lower() == "да":
    all+=low
if input("Нужны ли цифры? ").lower() == "да":
    all+=digits
if input("Нужны ли спец. символы? ").lower() == "да":
    all+=spec
if len(all) == 0:
    print("ЕМАЕ")
else:
    for  i in range(a):
        password += random.choice(all)
    print(password)
