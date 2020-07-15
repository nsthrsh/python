from tkinter import *
import tkinter.colorchooser
import fontchooser

def triangle():
    canvas.coords(r,(0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    canvas.itemconfig(t, fill=color(), outline='white')
    canvas.coords(t, (50, 200, 340, 200, 110, 60))
    text.delete(1.0, END)
    text.insert(1.0, 'Зображення трикутника')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=font(),foreground='black')
def rectangle():
    canvas.coords(t,(0, 0, 0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    canvas.itemconfig(r, fill=color(), outline='white')
    canvas.coords(r, (80, 50, 320, 200))
    text.delete(1.0, END)
    text.insert(1.0, 'Зображення прямокутника')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=font(),foreground='black')
def circle():
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(r, (0, 0, 0, 0))
    canvas.itemconfig(c, fill=color(), outline='white')
    canvas.coords(c, (120, 70, 260, 210))
    text.delete(1.0, END)
    text.insert(1.0, 'Зображення кола')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=font(), foreground='black')
def clear():
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    text.delete(1.0, END)

def color():
    (rgb, hx) = tkinter.colorchooser.askcolor()
    return hx
def font():
    x=fontchooser.askfont()
    return x

win = Tk()
canvas = Canvas(width=400, height=300, bg='#fff')
text = Text(width=55, height=5, bg='#fff', wrap=WORD)
t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
r = canvas.create_rectangle(0, 0, 0, 0)
c = canvas.create_oval(0, 0, 0, 0)
b_triangle = Button(text="Трикутник", width=15, command=triangle)
b_rectangle = Button(text="Прямокутник", width=15, command=rectangle)
b_circle = Button(text="Коло", width=15, command=circle)
b_clear = Button(text="Очистити", width=15,command=clear)

b_triangle.grid(row=0, column=0)
b_rectangle.grid(row=1, column=0)
b_circle.grid(row=2, column=0)
b_clear.grid(row=4, column=0)
canvas.grid(row=0, column=1, rowspan=10)
text.grid(row=11, column=1, rowspan=3)
win.mainloop()
