import tkinter as tk
from tkinter import *

n = int(input("Input the tokens: "))

window = tk.Tk()
window.resizable(False, False)
window.title("Transition system")

frame = Frame(window, bd = 10, bg = "silver")
frame.pack()

canvas = tk.Canvas(frame, bd = 1, height = 600, width = 600)
canvas.pack()
window.geometry("600x600")

a = temp = n
b = c = 0

space = 600 / (n + 3)

for i in range(n + 1):
    for j in range(temp + 1):
        mk = "[" + str(a) + ", " + str(b) + ", " + str(c) + "]";
        canvas.create_text(space * (j + 1) + space / 2 * i, space * (i + 1), 
                            fill = "midnightblue", font = ("Arial", 16 - n), text = mk)

        if j < temp:
            a -= 1
            b += 1
            canvas.create_line(space * (j + 1) + space / 2 * i + (16 - n) * 2.1, space * (i + 1), 
                                space * (j + 2) + space / 2 * i - (16 - n) * 2.1, space * (i + 1), 
                                arrow = tk.LAST, fill = "violet")
            canvas.create_line(space * (j + 1) + space / 2 * (i + 1), space * (i + 2) - (16 - n) * 0.8, 
                                space * (j + 1) + space / 2 * i, space * (i + 1) + (16 - n) * 0.8, 
                                arrow = tk.LAST, fill = "olive")
        
        if j > 0:
            canvas.create_line(space * (j + 1) + space / 2 * i, space * (i + 1) + (16 - n) * 0.8, 
                                space * j + space / 2 * (i + 1), space * (i + 2) - (16 - n) * 0.8,
                                arrow = tk.LAST, fill = "navy")

    a, b = b, a
    a -= 1
    c += 1
    temp -= 1

legend_text = """
-------------------
 [start]:                      
 [change]:                 
 [end]:                       
-------------------"""

legend_frame = LabelFrame(canvas, text = 'Transition', padx = 5, pady = 5)
legend_label = Label(legend_frame, text = legend_text)
legend_label.pack()

La1 = Label(legend_frame, text = "------>", fg = "violet")
La1.pack()
La1.place(x = 60, y = 30)

La2 = Label(legend_frame, text = "------>", fg = "navy")
La2.pack()
La2.place(x = 60, y = 45)

La3 = Label(legend_frame, text = "------>", fg = "olive")
La3.pack()
La3.place(x = 60, y = 60)

canvas.create_window(450, 500, window = legend_frame, anchor = W)

window.mainloop()
