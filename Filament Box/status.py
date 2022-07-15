import tkinter as tk
import keyboard

def exitStatus(e):
    window.destroy()

with open("loaded_filaments.txt", "r") as file:
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
backgroundwidget.place(x=0,y=0)

fil1=tk.PhotoImage(file="status_screen_assets/filaments/fil"+str(filnum1)+".png")
fil2=tk.PhotoImage(file="status_screen_assets/filaments/fil"+str(filnum2)+".png")
fil3=tk.PhotoImage(file="status_screen_assets/filaments/fil"+str(filnum3)+".png")

slot1 = label1=tk.Label(window, bd=0, highlightthickness=0, image=fil1)
slot1.grid(column=0,row=0)
slot2 = label1=tk.Label(window, bd=0, highlightthickness=0, image=fil2)
slot2.grid(column=1,row=0)
slot3 = label1=tk.Label(window, bd=0, highlightthickness=0, image=fil3)
slot3.grid(column=2,row=0)

window.bind('<Escape>', lambda e: exitStatus(e))

window.mainloop()

            

