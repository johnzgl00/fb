import tkinter as tk

with open("offline_data/system.txt", "r") as file:
    content = file.read()
    temp = content.split('\n', 4)[0]
    fan = content.split('\n', 4)[1]
    cpu = content.split('\n', 4)[2]
    ram = content.split('\n', 4)[3]
    power = content.split('\n', 4)[4]

def refresh():
    with open("offline_data/system.txt", "r") as file:
        content = file.read()
        temp = content.split('\n', 4)[0]
        fan = content.split('\n', 4)[1]
        cpu = content.split('\n', 4)[2]
        ram = content.split('\n', 4)[3]
        power = content.split('\n', 4)[4]
    tempvar.set(temp)
    cpuvar.set(cpu)
    fanvar.set(fan)
    ramvar.set(ram)
    powervar.set(power)
def exitStatus(e):
    window.destroy()

window = tk.Tk()
window.geometry("480x320")
window.title("FILAMENT BOX")
window.configure(bg="#222222")
window.attributes('-fullscreen', True)

backgroundColor="#222"

background=tk.PhotoImage(file="system_screen_assets/background.png")
backgroundwidget = tk.Label(window, bd=0, highlightthickness=0, image=background)
backgroundwidget.place(x=0,y=0)

tempvar=tk.StringVar()
tempvar.set(temp)
templ=tk.Label(window, textvariable=tempvar, font=("Arial", 30), fg="red", bg="#2a2a2a")
templ.place(x=40,y=20)

fanvar=tk.StringVar()
fanvar.set(fan)
fanl=tk.Label(window, textvariable=fanvar, font=("Arial", 30), fg="red", bg="#2a2a2a")
fanl.place(x=202,y=20)

cpuvar=tk.StringVar()
cpuvar.set(cpu)
cpul=tk.Label(window, textvariable=cpuvar, font=("Arial", 30), fg="red", bg="#2a2a2a")
cpul.place(x=363,y=20)

ramvar=tk.StringVar()
ramvar.set(ram)
raml=tk.Label(window, textvariable=ramvar, font=("Arial", 30), fg="red", bg="#2a2a2a")
raml.place(x=40,y=180)

powervar=tk.StringVar()
powervar.set(power)
powerl=tk.Label(window, textvariable=powervar, font=("Arial", 30), fg="red", bg="#2a2a2a")
powerl.place(x=178,y=180)

refreshimg=tk.PhotoImage(file="system_screen_assets/refreshbtn.png")
refreshbtn = tk.Button(window, image=refreshimg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=refresh)
refreshbtn.place(x=322,y=162)

window.bind('<Escape>', lambda e: exitStatus(e))

window.mainloop()