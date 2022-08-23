import tkinter as tk
from turtle import title

with open("loaded_filaments.txt", "r") as file:
    content = file.read()
    title1 = content.split('\n', 3)[0]
    title2 = content.split('\n', 3)[1]
    title3 = content.split('\n', 3)[2]

with open("env.txt", "r") as file:
    content = file.read()
    temp = content.split('\n', 3)[0]
    hum = content.split('\n', 3)[1]


window= tk.Tk()
window.geometry("480x320")
window.configure(bg="#fff")
#window.attributes('-fullscreen', True)

title1str=tk.StringVar()
title1str.set(str(title1))
title2str=tk.StringVar()
title2str.set(str(title2))
title3str=tk.StringVar()
title3str.set(str(title3))

tempstr=tk.StringVar()
tempstr.set(str(temp))
humstr=tk.StringVar()
humstr.set(str(hum))

background=tk.PhotoImage(file="assets/background.png")
bg=tk.Label(window, bd=0, highlightthickness=0, image=background)
bg.pack(padx=0, pady=0)

spool1=tk.Label(window, textvariable=title1str, font=("Bansrift", 35), fg="black", bg="#fff")
spool1.place(x=90, y=11)
spool2=tk.Label(window, textvariable=title2str, font=("Bansrift", 35), fg="black", bg="#fff")
spool2.place(x=90, y=91)
spool3=tk.Label(window, textvariable=title3str, font=("Bansrift", 35), fg="black", bg="#fff")
spool3.place(x=90, y=171)

temps=tk.Label(window, textvariable=tempstr, font=("Bansrift", 35), fg="black", bg="#fff")
temps.place(x=90, y=251)
hums=tk.Label(window, textvariable=humstr, font=("Bansrift", 35), fg="black", bg="#fff")
hums.place(x=285, y=251)

window.mainloop()
