a = int(input("Введите сторону a"))
b = int(input("Введите сторону b"))
c = int(input("Введите сторону c"))
if a+b<c or a+c<b or b+c<a:
    print("Ошибка")
else:
    if a==b and b==c and a==c:
        print("Равносторонний")
    elif a==b or b==c or a==c:
        print("Равнобедренный")
    else:
        print("Разносторонний")
