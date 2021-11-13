import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()

window.title("The patients' Petri Net")
frame = Frame(window, bd = 10, bg = "silver")
frame.pack(side = TOP)
frame2 = Frame(window, bd = 10, bg = "silver")
frame2.pack(side = RIGHT)
frame_input = Frame(window, bd = 10, bg = "silver")
frame_input.pack(side = LEFT)

canvas = tk.Canvas(frame, bd = 1, height = 250, width = 1000)
canvas.pack()
canvas2 = tk.Canvas(frame2, bd = 1, height = 300, width = 500)
canvas2.pack()
canvas_input = tk.Canvas(frame_input, bd = 1, height = 300, width = 500)
canvas_input.pack()
window.geometry("1000x550")

def create_circle(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill = "silver")

create_circle(100, 100, 30, canvas)
create_circle(500, 100, 30, canvas)
create_circle(900, 100, 30, canvas)

canvas.create_line(130, 100, 260, 100, arrow = tk.LAST)
canvas.create_line(260, 100, 470, 100, arrow = tk.LAST)
canvas.create_line(530, 100, 660, 100, arrow = tk.LAST)
canvas.create_line(670, 100, 870, 100, arrow = tk.LAST)

canvas.create_text(100, 140, fill = "dimgrey", font = "Arial 14", text = "wait")
canvas.create_text(500, 140, fill = "dimgrey", font = "Arial 14", text = "inside")
canvas.create_text(900, 140, fill = "dimgrey", font = "Arial 14", text = "done")

def startclick():
    pass

def changeclick():
    pass

def enter():
    a = int(input_wait.get())
    b = int(input_inside.get())
    c = int(input_done.get())
    input_wait.delete(0, END)
    input_inside.delete(0, END)
    input_done.delete(0, END)

    if a < 0 or b < 0 or c < 0:
        messagebox.showerror("Exception!!!", "The numbers of tokens must be positive.")
        return
    
    free = Text(frame, font = "Arial 10", bg = "silver", width = 6, height = 1, fg = "navy")
    free.pack()
    free.insert(END, a)
    free.config(state = "disabled")
    free.place(x = 78, y = 90)

    inside = Text(frame, font = "Arial 10", bg = "silver", width = 6, height = 1, fg = "navy")
    inside.pack()
    inside.insert(END, b)
    inside.config(state = "disabled")
    inside.place(x = 478, y = 90)

    done = Text(frame, font = "Arial 10", bg = "silver", width = 6, height = 1, fg = "navy")
    done.pack()
    done.insert(END, c)
    done.config(state = "disabled")
    done.place(x = 878, y = 90)

transition1 = Button(frame, text = "start", font = "Arial 14", fg = "steelblue", bg = "aqua", padx = 10, pady = 10, command = startclick)
transition1.pack()
transition1.place(x = 260, y = 75)
transition2 = Button(frame, text = "change", font = "Arial 14", fg = "steelblue", bg = "aqua", padx = 10, pady = 10, command = changeclick)
transition2.pack()
transition2.place(x = 660, y = 75)

L_input = Label(frame_input, text = "Input the number of tokens in each place: ", font = "Arial 14")
L_input.pack()
L_input.place(x = 50, y = 10)

L_wait = Label(frame_input, text = "Wait: ", font = "Arial 14")
L_wait.pack()
L_wait.place(y = 50)

L_inside = Label(frame_input, text = "Inside: ", font = "Arial 14")
L_inside.pack()
L_inside.place(y = 100)

L_done = Label(frame_input, text = "Done: ", font = "Arial 14")
L_done.pack()
L_done.place(y = 150)

input_wait = Entry(frame_input, width = 60, bg = "snow")
input_wait.pack()
input_wait.place(x = 70, y = 55)

input_inside = Entry(frame_input, width = 60, bg = "snow")
input_inside.pack()
input_inside.place(x = 70, y = 105)

input_done = Entry(frame_input, width = 60, bg = "snow")
input_done.pack()
input_done.place(x = 70, y = 155)

Enter_token = Button(frame_input, text = "Enter", font = "Arial 14", fg = "royalblue", bg = "lavender", padx = 5, pady = 5, command = enter)
Enter_token.pack()
Enter_token.place(x = 360, y = 190)

window.mainloop()