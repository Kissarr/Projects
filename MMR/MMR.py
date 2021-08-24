from tkinter import *

root = Tk()
root.title("Dota2 MMR Clicker")
root.geometry("244x244")
root.resizable(True, True)
root.configure(bg="gray22")

title = Label(root, text='Твой ММР', bg="Gray22", fg="red", font=40)
title.pack()

x = 0


def cam():
    global x
    x += 1
    btn["text"] = x
    if x >= 20:
        x = "You gay"
        btn["text"] = x


btn = Button(root, text="Play", bg="red", command=cam)
btn.pack()

root.mainloop()
