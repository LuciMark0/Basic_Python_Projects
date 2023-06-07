from threading import Timer
import tkinter as tk
import random

turn = 14

root = tk.Tk()
root.geometry("610x300")
root.title("2048")

def randnum():
    mtpl = []
    for field in fieldlist:
        if field.cget("text") == " ":
            mtpl.append(field)
    if len(mtpl) > 0:
        random.choice(mtpl).configure(text="2")
    root.update()
    Timer(0.1,checkGame).start()

def restart():
    check_score(fieldlist)
    for i in fieldlist:
        i.configure(text=" ")
    randnum()
    randnum()


def checkGame():
    global turn
    movc = []
    print(turn)
    if turn == 0 or turn == 1:
        turn = 0
        for i in fieldlist:
            if i.cget("text") == " ":
                turn += 1
        if turn == 0:
            movc.append(horizontal("rightc"))
            movc.append(horizontal("leftc"))
            movc.append(vertical("upc"))
            movc.append(vertical("downc"))
            print(movc)
            if not "True" in movc:
                sign.configure(text="You Died")
                root.update()
                check_score(fieldlist)
                

def check_score(fieldlist):
    score = 0
    for i in fieldlist:
        if i.cget("text") != " ":
            score += int(i.cget("text"))
    Timer(2,lambda: sign.configure(text=f"Last High Score: {score}")).start()

def horizontal(way):
    global turn
    checkh=[]
    check = False
    x = [fieldlist,fieldlist[::-1]]
    if "right" in way:
        x = x[0]
    else:
        x = x[1]
    for _ in range(3):
        for place in range(2,-1,-1):
            for hori in range(place,len(x),4):
                if x[hori].cget("text") == " ":
                    continue
                elif x[hori+1].cget("text") == " ":
                    check = True
                    if not "c" in way:
                        x[hori+1].configure(text=x[hori].cget("text"))
                        x[hori].configure(text=" ")
                elif x[hori+1].cget("text") == x[hori].cget("text") and not hori in checkh:
                    check = True
                    checkh.append(hori)
                    if not "c" in way:
                        x[hori+1].configure(text=int(x[hori].cget("text"))+int(x[hori+1].cget("text")))
                        x[hori].configure(text=" ")
    if "c" in way:
        return str(check)  
    elif check:
        if turn > 0:
            turn -= 1
        root.update()
        Timer(0.2,randnum).start()
    
def vertical(way):
    global turn
    checkh=[]
    check = False
    x = [fieldlist,fieldlist[::-1]]
    if "down" in way:
        x = x[0]
    else:
        x = x[1]
    for _ in range(3):
        for place in range(0,4):
            for verti in range(place,len(x)-4,4):
                if x[verti].cget("text") == " ":
                    continue
                elif x[verti+4].cget("text") == " ":
                    check = True
                    if not "c" in way:
                        x[verti+4].configure(text=x[verti].cget("text"))
                        x[verti].configure(text=" ")
                elif x[verti+4].cget("text") == x[verti].cget("text") and not verti in checkh:
                    check = True
                    checkh.append(verti)
                    if not "c" in way:      
                        x[verti+4].configure(text=int(x[verti].cget("text"))+int(x[verti+4].cget("text")))
                        x[verti].configure(text=" ")
    if "c" in way:
        return str(check)
    elif check:
        if turn > 0 :
            turn -= 1
        root.update()
        Timer(0.2,randnum).start()
            

# create game area 4x4
fieldlist = []
colours = ["black","gray"]
for row_ in range(4):
    for column_ in range(4):
        field = tk.Label(text=" ",font=("Courier 14 bold",15),width=7,height=3, background=colours[0], foreground=colours[1])
        fieldlist.append(field)
        field.grid(column=column_,row=row_)
        colours = colours[::-1]
    colours = colours[::-1]


guiframe=tk.Label(background="white",height=17)
guiframe.grid(row=0,column=4,rowspan=4)

btnup= tk.Button(text="Up",height=3,font=("Courier 14 bold",12),width=3,command=lambda: vertical("up"))
btnup.grid(row=1,column=6)
btnup= tk.Button(text="Down",height=3,font=("Courier 14 bold",12),width=4,command=lambda: vertical("down"))
btnup.grid(row=2,column=6)
btnup= tk.Button(text="Left",height=3,font=("Courier 14 bold",12),width=4,command=lambda: horizontal("left"))
btnup.grid(row=2,column=5)
btnup= tk.Button(text="Right",height=3,font=("Courier 14 bold",12),width=4,command=lambda: horizontal("right"))
btnup.grid(row=2,column=7)


sign = tk.Label(text="",height=3,width=22,background="black",foreground="white",font=("Courier 14 bold",12))
sign.grid(row=0,column=5,columnspan=3)

btnrest = tk.Button(text="Restart",command=lambda: restart())
btnrest.grid(row=3,column=6)


randnum()
randnum()
root.mainloop()