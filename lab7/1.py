dict = {".,?!:":1,
        "abc":2,
        "def":3,
        "ghi":4,
        "jkl":5,
        "mno":6,
        "pqrs":7,
        "tuv":8,
        "wxyz":9,
        " ":0}
answer = ""
st = input()
for i in st.lower():
    for j in dict:
        n = 0
        if i in j:
            for k in j:
                n+=1
                if i == k:
                    break
        answer+=str(dict.get(j))*n
print(answer)
