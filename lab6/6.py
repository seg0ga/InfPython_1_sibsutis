choise = int(input("Дешифровка - 1/Шифрование - 2"))
if choise == 1:
    k = open("for6.txt","r")
    z = k.readline().split(" ")
    fin_str = ""
    for i in z:
        fin_str += i[::-1]+ " "
    print(fin_str)
    k.close()
elif choise == 2:
    string = input("Введите строку для шифрования").split(" ")
    new_string = ""
    for i in string:
        new_string+= i[::-1]+ " "
    k = open("answer.txt","w")
    k.write(new_string)
    k.close()
