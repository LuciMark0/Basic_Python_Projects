import tkinter as tk
import pyperclip as pc
import random

# Prepare password character choices
symbols = "^@$&!%#*"
numbers = "0123456789"
alphabetL = "abcdefghijklmnopqrstuvwxyz"
alphabetU = alphabetL.upper()

def generator():
    # Generating the password and updating the label text
    password = ""
    if au.get():
        password += alphabetU
    if al.get():
        password += alphabetL
    if n.get():
        password += numbers
    if s.get():
        password += symbols

    gnpassword = "".join(random.choice(password) for _ in range(int(scaleL.get())))
    passwordM.config(text=gnpassword)

def copy_password():
    # Copying the generated password to the clipboard
    pc.copy(passwordM.cget("text"))

root = tk.Tk()
root.geometry("300x300")
root.title("Password Generator")

au = tk.IntVar()
al = tk.IntVar()
n = tk.IntVar()
s = tk.IntVar()
scaleL = tk.DoubleVar()

passwordM = tk.Label(root, background="black", foreground="white", width=30, font=("Courier 14 bold", 12), text="")
passwordM.grid(row=1, column=1, columnspan=4)

copy = tk.Button(root, text="Copy", font=("Courier 14 bold", 12), width=8, command=copy_password)
copy.grid(row=2, column=2)

generate = tk.Button(root, text="Generate", font=("Courier 14 bold", 12), command=generator)
generate.grid(row=2, column=3)

scaleLabel = tk.Label(root, text="Length:", font=("Courier 14 bold", 12))
scaleLabel.grid(row=3, column=2)
scale = tk.Scale(root, variable=scaleL, from_=1, to=100, orient=tk.HORIZONTAL)
scale.grid(row=3, column=3)

checkAU = tk.Checkbutton(root, text="Uppercase", font=("Courier 14 bold", 12), variable=au, onvalue=1, offvalue=0)
checkAU.grid(row=4, column=2, columnspan=2)

checkAL = tk.Checkbutton(root, text="Lowercase", font=("Courier 14 bold", 12), variable=al, onvalue=1, offvalue=0)
checkAL.grid(row=5, column=2, columnspan=2)

checkN = tk.Checkbutton(root, text="Numbers", font=("Courier 14 bold", 12), variable=n, onvalue=1, offvalue=0)
checkN.grid(row=6, column=2, columnspan=2)

checkS = tk.Checkbutton(root, text="Symbols", font=("Courier 14 bold", 12), variable=s, onvalue=1, offvalue=0)
checkS.grid(row=7, column=2, columnspan=2)

root.mainloop()