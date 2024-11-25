a = input()
if len(a)%2==1:
    print("-")
else:
    if a[0] != "Q":
        print("-")
    else:
        if a.count("Q")==a.count("A"):
            print("+")
        else: print("-")
