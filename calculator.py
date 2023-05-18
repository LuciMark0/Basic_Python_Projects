import tkinter as tk

fieldText = ""

def add_to_field(sth):
    global fieldText
    fieldText = fieldText+str(sth)
    field.configure(text=fieldText)


def calculate():
    global fieldText
    if fieldText != "":
        result = str(eval(fieldText))
        fieldText = result
        field.configure(text=result)

def clear():
    global fieldText
    fieldText = ""
    field.configure(text=fieldText)

window = tk.Tk()
window.title("Calculator")
#window.geometry("410x280")
window.geometry("455x362")
window.resizable(0, 0)

window.resizable(False, False)

window.resizable(width=False, height=False)
field = tk.Label(window,height=2,width=29,font=("Arial",20),text=fieldText,background="black",foreground="white")
field.grid(row=1,column=0,columnspan=5)

btn1 = tk.Button(window,text="1",command=lambda: add_to_field(1),width=4,font=("Arial",22))
btn1.grid(row=4,column=1)

btn2 = tk.Button(window,text="2",command=lambda: add_to_field(2),width=4,font=("Arial",22))
btn2.grid(row=4,column=2)

btn3 = tk.Button(window,text="3",command=lambda: add_to_field(3),width=4,font=("Arial",22))
btn3.grid(row=4,column=3)

btn4 = tk.Button(window,text="4",command=lambda: add_to_field(4),width=4,font=("Arial",22))
btn4.grid(row=3,column=1)

btn5 = tk.Button(window,text="5",command=lambda: add_to_field(5),width=4,font=("Arial",22))
btn5.grid(row=3,column=2)

btn6 = tk.Button(window,text="6",command=lambda: add_to_field(6),width=4,font=("Arial",22))
btn6.grid(row=3,column=3)

btn7 = tk.Button(window,text="7",command=lambda: add_to_field(7),width=4,font=("Arial",22))
btn7.grid(row=2,column=1)

btn8 = tk.Button(window,text="8",command=lambda: add_to_field(8),width=4,font=("Arial",22))
btn8.grid(row=2,column=2)

btn9 = tk.Button(window,text="9",command=lambda: add_to_field(9),width=4,font=("Arial",22))
btn9.grid(row=2,column=3)

btn0 = tk.Button(window,text="0",command=lambda: add_to_field(0),width=4,font=("Arial",22))
btn0.grid(row=5,column=1)

#-----------------------------------

btnPlus = tk.Button(window,text="+",command=lambda: add_to_field("+"),width=4,font=("Arial",22))
btnPlus.grid(row=4,column=4)

btnMinus = tk.Button(window,text="-",command=lambda: add_to_field("-"),width=4,font=("Arial",22))
btnMinus.grid(row=5,column=4)

btnTimes = tk.Button(window,text="*",command=lambda: add_to_field("*"),width=4,font=("Arial",22))
btnTimes.grid(row=3,column=4)

btnDivision = tk.Button(window,text="/",command=lambda: add_to_field("/"),width=4,font=("Arial",22))
btnDivision.grid(row=2,column=4)

btnClear = tk.Button(window,text="Clear",command=lambda: clear(),width=4,font=("Arial",22))
btnClear.grid(row=5,column=3)

btnDecimal = tk.Button(window,text=".",command=lambda: add_to_field("."),width=4,font=("Arial",22))
btnDecimal.grid(row=5,column=2)

btnOpr = tk.Button(window,text="(",command=lambda: add_to_field("("),width=4,font=("Arial",22))
btnOpr.grid(row=6,column=1)

btnCpr = tk.Button(window,text=")",command=lambda: add_to_field(")"),width=4,font=("Arial",22))
btnCpr.grid(row=6,column=2)

btnEqual = tk.Button(window,text="=",command=lambda: calculate(),width=10,font=("Arial",22))
btnEqual.grid(row=6,column=3,columnspan=2)



window.mainloop()