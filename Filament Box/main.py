from cgitb import grey
import tkinter as tk

window = tk.Tk()
window.geometry("480x320")
window.title("FILAMENT BOX")

btnheight=10
btnwidth=22
backgroundColor="#222"

statusbtnImg=tk.PhotoImage(file="statusbtn/statusbtn1.png")
confbtnImg=tk.PhotoImage(file="confbtn/confbtn1.png")
infobtnImg=tk.PhotoImage(file="infobtn/infobtn1.png")
sysbtnImg=tk.PhotoImage(file="systembtn/sysbtn1.png")
controlbtnImg=tk.PhotoImage(file="controlbtn/controlbtn1.png")
aboutbtnImg=tk.PhotoImage(file="aboutbtn/aboutbtn1.png")
buttonImg=tk.PhotoImage(file="button.png")

statusbtn = tk.Button(window, image=statusbtnImg, borderwidth=0, bg=backgroundColor, activebackground=backgroundColor)
statusbtn.grid(column=0,row=0)

confbtn = tk.Button(window, image=confbtnImg, borderwidth=0, bg=backgroundColor, activebackground=backgroundColor)
confbtn.grid(column=1,row=0)

infobtn = tk.Button(window, image=infobtnImg, borderwidth=0, bg=backgroundColor, activebackground=backgroundColor)
infobtn.grid(column=2,row=0)

systembtn = tk.Button(window, image=sysbtnImg, borderwidth=0, bg=backgroundColor, activebackground=backgroundColor)
systembtn.grid(column=0,row=1)

controlbtn = tk.Button(window, image=controlbtnImg, borderwidth=0, bg=backgroundColor, activebackground=backgroundColor)
controlbtn.grid(column=1,row=1)

aboutbtn = tk.Button(window, image=aboutbtnImg, borderwidth=0, bg=backgroundColor, activebackground=backgroundColor)
aboutbtn.grid(column=2,row=1)


window.mainloop()