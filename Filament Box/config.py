import tkinter as tk
from tkinter import font

def exitStatus(e):
    window.destroy()

def replaceNum():
    file = open('offline_data/loaded_filaments.txt', 'w')
    file.close()
    with open('offline_data/loaded_filaments.txt', 'w') as f:
        f.write(str(filnum1)+"\n"+str(filnum2)+"\n"+str(filnum3)+"\n")
def ups1():
    global filnum1
    global num1
    filnum1 += 1
    num1.set(filnum1)
    replaceNum()
def downs1():
    global filnum1
    global num1
    filnum1 -= 1
    num1.set(filnum1)
    replaceNum()
def ups2():
    global filnum2
    global num2
    filnum2 += 1
    num2.set(filnum2)
    replaceNum()
def downs2():
    global filnum2
    global num2
    filnum2 -= 1
    num2.set(filnum2)
    replaceNum()
def ups3():
    global filnum3
    global num3
    filnum3 += 1
    num3.set(filnum3)
    replaceNum()
def downs3():
    global filnum3
    global num3
    filnum3 -= 1
    num3.set(filnum3)
    replaceNum()

with open("offline_data/loaded_filaments.txt", "r") as file:
    content = file.read()
    filnum1 = int(content.split('\n', 3)[0])
    filnum2 = int(content.split('\n', 3)[1])
    filnum3 = int(content.split('\n', 3)[2])

window = tk.Tk()
window.geometry("480x320")
window.title("FILAMENT BOX")
window.configure(bg="#222222")
#window.attributes('-fullscreen', True)

backgroundColor="#222"

background=tk.PhotoImage(file="status_screen_assets/background.png")
backgroundwidget = tk.Label(window, bd=0, highlightthickness=0, image=background)
backgroundwidget.pack(padx=0, pady=0)

#slot1
num1 = tk.StringVar()
num1.set(str(filnum1))

slot1num=tk.Label(window, textvariable=num1, font=("Arial", 40), fg="red", bg="#2a2a2a")
slot1num.place(x=60, y=35)

upbtnimg=tk.PhotoImage(file="config_screen_assets/up.png")
up1slot=tk.Button(window, bd=0, highlightthickness=0, activebackground="#2a2a2a", image=upbtnimg, command=ups1)
up1slot.place(x=80, y=100)

downbtnimg=tk.PhotoImage(file="config_screen_assets/down.png")
down1slot=tk.Button(window, bd=0, highlightthickness=0, activebackground="#2a2a2a", image=downbtnimg, command=downs1)
down1slot.place(x=10, y=100)

spoolimg=tk.PhotoImage(file="config_screen_assets/filament.png")
spool1=tk.Label(window, bd=0, highlightthickness=0, image=spoolimg)
spool1.place(x=37,y=200)


#slot2
num2 = tk.StringVar()
num2.set(str(filnum2))

slot2num=tk.Label(window, textvariable=num2, font=("Arial", 40), fg="red", bg="#2a2a2a")
slot2num.place(x=222, y=35)

up2slot=tk.Button(window, bd=0, highlightthickness=0, activebackground="#2a2a2a", image=upbtnimg, command=ups2)
up2slot.place(x=241, y=100)

down2slot=tk.Button(window, bd=0, highlightthickness=0, activebackground="#2a2a2a", image=downbtnimg, command=downs2)
down2slot.place(x=171, y=100)

spool2=tk.Label(window, bd=0, highlightthickness=0, image=spoolimg)
spool2.place(x=198,y=200)


#slot3
num3 = tk.StringVar()
num3.set(str(filnum3))

slot1num=tk.Label(window, textvariable=num3, font=("Arial", 40), fg="red", bg="#2a2a2a")
slot1num.place(x=382, y=35)

up1slot=tk.Button(window, bd=0, highlightthickness=0, activebackground="#2a2a2a", image=upbtnimg, command=ups3)
up1slot.place(x=402, y=100)

down1slot=tk.Button(window, bd=0, highlightthickness=0, activebackground="#2a2a2a", image=downbtnimg, command=downs3)
down1slot.place(x=332, y=100)

spool3=tk.Label(window, bd=0, highlightthickness=0, image=spoolimg)
spool3.place(x=359,y=200)


window.bind('<Escape>', lambda e: exitStatus(e))

window.mainloop()
