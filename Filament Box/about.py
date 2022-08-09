import tkinter as tk

def exitStatus(e):
    window.destroy()

window = tk.Tk()
window.geometry("480x320")
window.title("FILAMENT BOX")
window.configure(bg="#222222")
window.attributes('-fullscreen', True)
backgroundColor="#222"

background=tk.PhotoImage(file="about_screen_assets/background.png")
backgroundwidget = tk.Label(window, bd=0, highlightthickness=0, image=background)
backgroundwidget.place(x=0,y=0)

window.bind('<Escape>', lambda e: exitStatus(e))

window.mainloop()