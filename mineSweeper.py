import tkinter as tk
import random


difficulty = int(input("enter a number: "))

def field_prep(dif):
    field = "" + " "*3

    for i in range(dif):
        if i < 10:
            field += str(i) + " "*2
        else:
            field += str(i) + " "
    rowlen = len(field)
    field += "\n"+"-"*rowlen + "\n"

    for i in range(dif):
        if i < 10:
            field += str(i) + " " + "|. "*dif + "|\n"
        else:
            field += str(i) + "|. "*dif + "|\n"
    
    field += "-"*rowlen
    return field

def field_mines_prep():
    field = field_prep(difficulty)
    fieldgui = list(field.replace(".","·"))

    firstPlace = field.find(".")
    field = field.replace(".","0")
    # determine the fields exact locaiton
    places = []
    down = difficulty*3 + 4
    for _ in range(difficulty):
        fp = firstPlace
        for _ in range(difficulty):                
                places.append(fp)
                fp += 3
        firstPlace += down
    placesf = places[:]
    field = list(field)
    # Mines' placement
    minecount = difficulty**2*10//64
    random.shuffle(places)
    minesloc = places[:minecount]
    for mine in minesloc:
        field[mine] = "*"
    
    # Mines around counter
    nearMines = []
    nearLocs = [3, down, down+3, down-3]

    for mine in minesloc:
        for loc in nearLocs:
            nearMines.append(mine+loc)
            nearMines.append(mine-loc)

    for i in nearMines:
        if i in places and field[i].isdigit():
            field[i] = str(int(field[i])+1)
    
    def mechanincs(location):
        x = location
        print(x)
        # after digging field appears on fieldgui
        if field[x] == "*":
            for i in minesloc:
                fieldgui[i] = field[i]
            print("".join(field))
            print("You Died!")
            exit()
        elif field[x] != "0":
            fieldgui[x] = field[x]
        else:
            nearnumbers = [x]
            for num in nearnumbers:
                for loc in nearLocs:
                    if num+loc in places and field[num+loc].isdigit() and not num+loc in nearnumbers and field[num] == "0":
                        nearnumbers.append(num+loc)
                    if num-loc in places and field[num-loc].isdigit() and not num-loc in nearnumbers and field[num] == "0" :
                        nearnumbers.append(num-loc)
            for i in nearnumbers:
                fieldgui[i] = field[i]

        
        print("".join(fieldgui))
        if fieldgui.count("·") == minecount:
            print("You Win!")
            exit()

    def interface(bcount,field,places):
        window = tk.Tk()
        window.title("Mine Sweeper")

        geometry = (bcount)*50
        window.geometry(f"{geometry}x{geometry}")
        window.resizable(0, 0)
        def dig_helper(location):
            mechanincs(places[location])
            interface_dig(location,field,buttons,places)
        buttons = []
        for i in range(bcount**2):
            x = tk.Button(window,text="",command=lambda i=i: dig_helper(i),width=1,font=("Arial",22),relief=tk.RAISED)
            buttons.append(x)
            x.grid(row=i//bcount,column=i%bcount)
        window.mainloop()
        

    def interface_dig(location,field,buttons,places):
        if field[places[location]] != "0":
            buttons[location].configure(text = field[places[location]])
        else:
            for i in range(len(buttons)):
                buttons[i].configure(text = field[places[i]])
    interface(difficulty,fieldgui,placesf)
    print("".join(fieldgui))
    


def digging_field(colLen,firstplace):
    coor = input("Where would you like to dig? Input as row, col: ")
    coor = coor.split(",")
    return firstplace+colLen*(int(coor[1]))+int(coor[0])*3



field_mines_prep()
