import PySimpleGUI as sg
import random as r

sg.theme("GreenMono")
layout = [
    [sg.Text("Генератор оценок по физике",justification="center",font="10px")],
    [sg.Image(filename="tenor.png",subsample=2)],
    [sg.Text("  Левый предел",expand_x=True,auto_size_text=True,justification="left",font="15px"),sg.Text("Правый предел",font="15px",expand_x=True,justification="right")],
    [sg.InputText(size=14,font="13px"), sg.InputText(size=14,font="13px")],
    [sg.Button("Генерация",key="-function-",size=30,font="15px")],
    [sg.Text("",key="-text-",justification="center",font="25px")]]


window = sg.Window("Рейтинг по физике",layout,element_justification="center",size=(350,435))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-function-":
        try:
            if (int(values[1])>int(values[2])):
                window["-text-"].update(f"Неверное значение")
            else:
                rand = r.randint(int(values[1]), int(values[2]))
                window["-text-"].update(f"Результат: {rand}")
        except ValueError:
            window["-text-"].update(f"Ошибка")

window.close()
