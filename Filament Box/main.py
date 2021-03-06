import tkinter as tk
from os import system

def status():
	system("python3 status.py")
def conf():
	system("python3 config.py")
def info():
	system("python3 info.py")
def sys():
	system("python3 system.py")
def control():
	system("python3 control.py")

window = tk.Tk()
window.geometry("480x320")
window.title("FILAMENT BOX")
window.configure(bg="#222222")
#window.attributes('-fullscreen', True)

btnheight=10
btnwidth=22
backgroundColor="#222"

statusbtnImg=tk.PhotoImage(file="main_screen_assets/statusbtn/statusbtn1.png")
confbtnImg=tk.PhotoImage(file="main_screen_assets/confbtn/confbtn1.png")
infobtnImg=tk.PhotoImage(file="main_screen_assets/infobtn/infobtn1.png")
sysbtnImg=tk.PhotoImage(file="main_screen_assets/systembtn/sysbtn1.png")
controlbtnImg=tk.PhotoImage(file="main_screen_assets/controlbtn/controlbtn1.png")
aboutbtnImg=tk.PhotoImage(file="main_screen_assets/aboutbtn/aboutbtn1.png")

statusbtn = tk.Button(window, image=statusbtnImg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=status)
statusbtn.grid(column=0,row=0)

confbtn = tk.Button(window, image=confbtnImg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=conf)
confbtn.grid(column=1,row=0)

infobtn = tk.Button(window, image=infobtnImg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=info)
infobtn.grid(column=2,row=0)

systembtn = tk.Button(window, image=sysbtnImg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=sys)
systembtn.grid(column=0,row=1)

controlbtn = tk.Button(window, image=controlbtnImg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor, command=control)
controlbtn.grid(column=1,row=1)

aboutbtn = tk.Button(window, image=aboutbtnImg, bd=0, highlightthickness=0, bg=backgroundColor, activebackground=backgroundColor)
aboutbtn.grid(column=2,row=1)


window.mainloop()
