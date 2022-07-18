import tkinter as tk

with open("offline_data/info.txt", "r") as file:
    content = file.read()
    temp = content.split('\n', 3)[0]
    humidity = content.split('\n', 3)[1]
    fil = content.split('\n', 3)[2]
    light = content.split('\n', 3)[3]

def refresh():
    with open("offline_data/info.txt", "r") as file:
        content = file.read()
        temp = content.split('\n', 3)[0]
        humidity = content.split('\n', 3)[1]
        fil = content.split('\n', 3)[2]
        light = content.split('\n', 3)[3]
    tempvar.set(temp)
    filvar.set(fil)
    humvar.set(humidity)
    lightvar.set(light)
def exitStatus(e):
    window.destroy()

window = tk.Tk()
window.geometry("480x320")
window.title("FILAMENT BOX")
window.configure(bg="#222222")
#window.attributes('-fullscreen', True)

backgroundColor="#222"

background=tk.PhotoImage(file="info_screen_assets/background.png")
backgroundwidget = tk.Label(window, bd=0, highlightthickness=0, image=background)
backgroundwidget.place(x=0,y=0)

tempvar=tk.StringVar()
tempvar.set(temp)
temp=tk.Label(window, textvariable=tempvar, font=("Arial", 30), fg="red", bg="#2a2a2a")
temp.place(x=40,y=20)

humvar=tk.StringVar()
humvar.set(humidity)
hum=tk.Label(window, textvariable=humvar, font=("Arial", 30), fg="red", bg="#2a2a2a")
hum.place(x=200,y=20)

filvar=tk.StringVar()
filvar.set(fil)
fil=tk.Label(window, textvariable=filvar, font=("Arial", 30), fg="red", bg="#2a2a2a")
fil.place(x=352,y=20)

lightvar=tk.StringVar()
lightvar.set(light)
light=tk.Label(window, textvariable=lightvar, font=("Arial", 30), fg="red", bg="#2a2a2a")
light.place(x=25,y=180)

navar=tk.StringVar()
navar.set("N/A")
na=tk.Label(window, textvariable=navar, font=("Arial", 30), fg="red", bg="#2a2a2a")
na.place(x=205,y=180)

refreshimg=tk.PhotoImage(file="info_screen_assets/refreshbtn.png")
refreshbtn = tk.Button(window, image=refreshimg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=refresh)
refreshbtn.place(x=322,y=162)

window.bind('<Escape>', lambda e: exitStatus(e))

window.mainloop()