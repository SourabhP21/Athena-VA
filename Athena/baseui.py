from tkinter import *
import PIL.Image, PIL.ImageTk
from PIL import Image
from prbase import *

def update(ind):
    frame = frames[(ind)%10]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

window = Tk()
window.configure(bg='black')
window.geometry("500x710")
global var

var = StringVar()

label1 = Label(window, textvariable = var, bg = 'black')
label1.config(font=("Courier", 12)) 
label1.config(fg="white")
label1.config(pady=1.5)
label1.config(height=8)
label1.config(width=40)
label1.config(wraplength=350)
label1.config(justify=CENTER)
var.set("Hey There!\n Press START to begin..")
label1.pack()

frames = [PhotoImage(file='elements/circle1.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('Athena')

label = Label(window, width = 380, height = 400)
label.config(bg="black")
label.config(padx=25)
label.config(pady=25)
label.pack()
window.after(0, update, 0)

btn1 = Button(text = 'START',command=begin, width = 10, relief="ridge", bg = '#2980B9')
btn1.config(font=("Courier", 12))
btn1.config(fg="white")
btn1.pack()
btn1.place(x=120,y=630)
btn2 = Button(text = 'EXIT',command=window.destroy, width = 10, relief="ridge", bg = '#E74C3C')
btn2.config(font=("Courier", 12))
btn2.config(fg="white")
btn2.pack()
btn2.place(x=270,y=630)

window.mainloop()