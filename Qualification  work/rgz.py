import PySimpleGUI as sg
import random as r

def who_winner(id_pc,id_pl):
    if id_pc==id_pl:
        return 2
    elif (id_pc==1 and id_pl==2) or (id_pc==2 and id_pl==3) or (id_pc==3 and id_pl==1):
        return 1
    else:
        return 0
flag=True

layout= [[sg.Text("Камень-ножницы-бумага", font="Arial 28")],
        [sg.Text("Введите Ваше имя:", font="Arial 20"), sg.Input(font="Arial 20", size=(10, 0), key="user")],
         [sg.Text("Количество раундов:", font="Arial 20"), sg.Input(font="Arial 20", size=(10, 0), key="count")],
         [sg.Button("ЗАПУСК",key="-function-",size=25,font="Arial 20")]]
window = sg.Window("",layout,element_justification="center",size=(475,225))
event,values=window.read()
if event == sg.WIN_CLOSED:
    flag=False
else:
    try:
        count=int(values["count"])
        if count <= 0:
            flag = False
            window.close()
            zzz = sg.popup("Неверные данные", font=("Arial", 20, "bold"), button_justification="center",
                           custom_text="И ЧО?")
    except ValueError:
        flag=False
        window.close()
        zzz = sg.popup("Неверные данные", font=("Arial", 20, "bold"), button_justification="center", custom_text="И ЧО?")
    user=values["user"]


window.close()

if flag==True:
    result = open("result.txt","w",encoding="utf8")
    res = ["№  Компьютер vs Игрок\n"]
    k = open("base64.txt","r")
    s = k.readlines()
    sg.theme("TealMono")
    paper_base64 = s[0]
    rock_base64 = s[1]
    scissors_base64 = s[2]
    k.close()
    pc_image = [[sg.Text("Ход компьютера", font=("Arial", 25,"bold"))],[sg.Text(" ", font="Arial 25")],[sg.Image("global.png",subsample=2,key="photo1")]]
    p_image = [[sg.Text("Ваш ход", font=("Arial", 25,"bold"))],[sg.Text(" ", font="Arial 25")],[sg.Image("global.png",subsample=2,key="photo2")]]
    p_input = [
        [sg.Text("СЧЕТ" ,font=("Arial", 40,"bold"))],
        [sg.Text(f"PC vs {user}" ,font=("Arial", 25,"bold"))],
        [sg.Text("0:0" ,font=("Arial", 25,"bold"),key="schet")],
        [sg.Button(" ", image_data= paper_base64, font="Arial 20")],
        [sg.Button("  ", image_data= rock_base64, font="Arial 20")],
        [sg.Button("   ", image_data= scissors_base64, font="Arial 20")],]
    flag=True
    layout = [
        [sg.Column(pc_image,element_justification="center"), sg.Column(p_image,element_justification="center"), sg.VSeperator(), sg.Column(p_input, element_justification='center')]]
    window = sg.Window("", layout)
    z = 1
    player = 0
    pc = 0
    while z<=count:
        z+=1
        event, value = window.read()
        photo = ""
        id = r.randint(1, 3)
        if id==1: photo = "paper.png"
        elif id==2: photo = "rock.png"
        else:photo = "scissors.png"
        if event == sg.WIN_CLOSED:
            flag=False
            sg.popup("Вы сдались :(", font=("Arial", 20, "bold"), button_justification="center",custom_text="ЁМАЁ",title="")
            break
        elif event == " ":
            window["photo1"].update(photo,subsample=2)
            window["photo2"].update("paper.png",subsample=2)
            if who_winner(id,1)==0:player+=1
            elif who_winner(id,1)==1: pc+=1
            else:True
        elif event == "  ":
            window["photo1"].update(photo, subsample=2)
            window["photo2"].update("rock.png",subsample=2)
            if who_winner(id,2)==0:player+=1
            elif who_winner(id,2)==1: pc+=1
            else:True
        elif event == "   ":
            window["photo1"].update(photo, subsample=2)
            window["photo2"].update("scissors.png",subsample=2)
            if who_winner(id,3)==0:player+=1
            elif who_winner(id,3)==1: pc+=1
            else:True
        window["schet"].update(f"{pc}:{player}")
        res.append(f"{z-1}  | {pc}:{player}\n")
    for i in res:
        result.write(i)
    window.close()
    result.close()
    if flag==True:
        if player>pc:
            sg.popup(f"Поздравляем, Вы победили бездушную машину со счетом  {pc}:{player}",font=("Arial", 20,"bold"),button_justification="center",custom_text="Ура", title="")
        elif pc>player:
            sg.popup(f"Жаль, но Вы не смогли одолеть бездушную машину со счетом {pc}:{player}",font=("Arial", 20,"bold"),button_justification="center",custom_text="Жаль",title="")
        else:
            sg.popup("Ничья",font=("Arial", 20,"bold"),button_justification="center",custom_text="Бывает, что поделать",title="")
