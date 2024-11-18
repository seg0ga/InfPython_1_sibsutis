import PySimpleGUI as sg

sg.theme("DarkTeal12")
layout = [
    [sg.Text("Эрудит",justification="center",font="10px")],
    [sg.Image(filename="aboba.png",subsample=2)],
    [sg.Text("Введите слово:",expand_x=True,auto_size_text=True,justification="center",font="15px")],
    [sg.InputText(size=20,font="13px")],
    [sg.Button("Подсчет очков",key="-function-",size=30,font="15px")],
    [sg.Text("",key="-text-",justification="center",font="25px")]]


window = sg.Window("Рейтинг по физике",layout,element_justification="center",size=(450,500))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-function-":
        dict = {"aeilnorstu": 1,
                "dg": 2,
                "bcmp": 3,
                "fhvwy": 4,
                "k": 5,
                "jx": 8,
                "qz": 10}
        score = 0
        st = values[1]
        for i in st.lower():
            for j in dict:
                if i in j:
                    score += dict.get(j)
        window["-text-"].update(f"Количество очков: {score}")

window.close()
