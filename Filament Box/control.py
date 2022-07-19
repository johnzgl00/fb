import tkinter as tk
from os import system

def exitStatus(e):
    window.destroy()
def shutdown():
    system("sudo shutdown now")
def restart():
    system("sudo shutdown -r now")
def lights():
    print("toggle lights")
def fan():
    print("toggle fan")
def update():
    print("update")

window = tk.Tk()
window.geometry("480x320")
window.title("FILAMENT BOX")
window.configure(bg="#222222")
#window.attributes('-fullscreen', True)

backgroundColor="#222"

background=tk.PhotoImage(file="control_screen_assets/background.png")
backgroundwidget = tk.Label(window, bd=0, highlightthickness=0, image=background)
backgroundwidget.place(x=0,y=0)

shutdownbtnImg=tk.PhotoImage(file="control_screen_assets/shutdownbtn.png")
shutdownbtn = tk.Button(window, image=shutdownbtnImg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=shutdown)
shutdownbtn.grid(column=0,row=0)

restartbtnImg=tk.PhotoImage(file="control_screen_assets/restartbtn.png")
restartbtn = tk.Button(window, image=restartbtnImg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=restart)
restartbtn.grid(column=0,row=1)

lightbtnImg=tk.PhotoImage(file="control_screen_assets/lightsbtn.png")
lightbtn = tk.Button(window, image=lightbtnImg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=lights)
lightbtn.grid(column=0,row=2)

fanbtnImg=tk.PhotoImage(file="control_screen_assets/fanbtn.png")
fanbtn = tk.Button(window, image=fanbtnImg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=fan)
fanbtn.grid(column=0,row=3)

updatebtnImg=tk.PhotoImage(file="control_screen_assets/updatebtn.png")
updatebtn = tk.Button(window, image=updatebtnImg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=update)
updatebtn.grid(column=0,row=4)

window.bind('<Escape>', lambda e: exitStatus(e))

window.mainloop()
