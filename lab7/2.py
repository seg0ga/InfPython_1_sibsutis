dict = {"aeilnorstu":1,
        "dg":2,
        "bcmp":3,
        "fhvwy":4,
        "k":5,
        "jx":8,
        "qz":10}
score = 0
st = input()
for i in st.lower():
    for j in dict:
        if i in j:
            score+=dict.get(j)
print(score)
