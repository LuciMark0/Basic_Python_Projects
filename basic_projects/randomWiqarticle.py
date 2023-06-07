import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk

# taking a title from page
response = requests.get(url="https://en.wikipedia.org/wiki/Special:Random")
title = BeautifulSoup(response.content, 'html.parser').find(id="firstHeading")

def refresh():
    #writing title to label text
    global response
    response = requests.get(url="https://en.wikipedia.org/wiki/Special:Random")
    title = BeautifulSoup(response.content, 'html.parser').find(id="firstHeading")
    titletk.configure(text=title.string)

root = tk.Tk()
root.geometry("300x150")
root.title("Random Wikipedia Title")

titletk= tk.Label(background="black",foreground="white",width=30,font=("Courier 14 bold",12),height=2,text=title.string)
titletk.grid(row=0,column=0,columnspan=3)

#opening the title's page when pressed a that button
btngo= tk.Button(width=10,text="Read",command=lambda: webbrowser.open(f'{response.url}'))
btngo.grid(row=1,column=1)

#Refreshing the title
btnre= tk.Button(width=10,text="Refresh",command=lambda: refresh())
btnre.grid(row=1,column=2)

root.mainloop()