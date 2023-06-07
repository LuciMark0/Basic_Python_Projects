import tkinter as tk
from tkinter import messagebox
from threading import Thread
import time

def countdown():
    try:
        minutes = int(mne.get()) if mne.get() else 0
        seconds = int(sce.get()) if sce.get() else 0
    except ValueError:
        timer = "Enter a Number!"
        clock.config(text=timer)
        return

    t = minutes * 60 + seconds

    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        try:
            clock.config(text=timer)
            root.update()
        except tk.TclError:
            # The widget might have been destroyed, exit the loop gracefully
            break
        t -= 1
        if t < 0:
            messagebox.showinfo("Time Countdown", "Time's up")
            break
        else:
            # Delay the next update by 1 second using a separate thread
            time_thread = Thread(target=time.sleep, args=(1,))
            time_thread.start()
            time_thread.join()

root = tk.Tk()
root.geometry("300x150")
root.title("Countdown Timer")

clock = tk.Label(root, background="black", foreground="white", width=20, font=("Arial", 20), text="00:00", height=2)
clock.grid(row=1, column=1, columnspan=4)

mnl = tk.Label(root, font=("Courier 14 bold", 12), text="Minute:")
mnl.grid(row=2, column=1)

mne = tk.Entry(root, width=24)
mne.grid(row=2, column=2, columnspan=3)

scl = tk.Label(root, font=("Courier 14 bold", 12), text="Second:")
scl.grid(row=3, column=1)

sce = tk.Entry(root, width=24)
sce.grid(row=3, column=2, columnspan=3)

start = tk.Button(root, font=("Courier 14 bold", 12), width=10, command=countdown, text="Start")
start.grid(row=4, column=3, columnspan=2)


root.mainloop()

