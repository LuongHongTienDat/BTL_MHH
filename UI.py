import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

window = tk.Tk()
window.resizable(False, False)

window.title("The patients' Petri Net")
frame = Frame(window, bd = 10, bg = "silver")
frame.pack(side = TOP)
frame2 = Frame(window, bd = 10, bg = "silver")
frame2.pack(side = RIGHT)
frame_input = Frame(window, bd = 10, bg = "silver")
frame_input.pack(side = LEFT)

canvas = tk.Canvas(frame, bd = 1, height = 250, width = 1000)
canvas.pack()
canvas2 = tk.Canvas(frame2, bd = 1, height = 280, width = 500)
canvas2.pack()
canvas_input = tk.Canvas(frame_input, bd = 1, height = 280, width = 500)
canvas_input.pack()
window.geometry("1000x530")

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
    wait.config(state = "normal")
    inside.config(state = "normal")

    a = int(wait.get("1.0", END))

    if a == 0:
        messagebox.showerror("Error!!!", "There are no tokens in place [wait].")
        return

    b = int(inside.get("1.0", END))
    c = int(done.get("1.0", END))

    wait.delete("1.0", END)
    inside.delete("1.0", END)

    a = a - 1
    b = b + 1

    wait.tag_configure("tag_name", justify='center')
    wait.insert(END, a)
    wait.tag_add("tag_name", "1.0", "end")

    inside.tag_configure("tag_name", justify='center')
    inside.insert(END, b)
    inside.tag_add("tag_name", "1.0", "end")

    wait.config(state = "disabled")
    inside.config(state = "disabled")

    mk = "\n[" + str(a) + ".wait, " + str(b) + ".inside, " + str(c) + ".done]";
    text_area.config(state = "normal")
    text_area.insert(INSERT, mk)
    text_area.config(state = "disabled")

def changeclick():
    inside.config(state = "normal")
    done.config(state = "normal")

    b = int(inside.get("1.0", END))

    if b == 0:
        messagebox.showerror("Error!!!", "There are no tokens in place [change].")
        return

    c = int(done.get("1.0", END))
    a = int(wait.get("1.0", END))

    inside.delete("1.0", END)
    done.delete("1.0", END)

    b = b - 1
    c = c + 1

    inside.tag_configure("tag_name", justify='center')
    inside.insert(END, b)
    inside.tag_add("tag_name", "1.0", "end")

    done.tag_configure("tag_name", justify='center')
    done.insert(END, c)
    done.tag_add("tag_name", "1.0", "end")

    inside.config(state = "disabled")
    done.config(state = "disabled")

    mk = "\n[" + str(a) + ".wait, " + str(b) + ".inside, " + str(c) + ".done]";
    text_area.config(state = "normal")
    text_area.insert(INSERT, mk)
    text_area.config(state = "disabled")

def enter():
    a = input_wait.get()
    b = input_inside.get()
    c = input_done.get()

    input_wait.delete(0, END)
    input_inside.delete(0, END)
    input_done.delete(0, END)

    if a.isnumeric() == False or b.isnumeric() == False or c.isnumeric() == False:
        messagebox.showerror("Error!!!", "Your input is not a positive number.")
        return

    wait.config(state = "normal")
    inside.config(state = "normal")
    done.config(state = "normal")

    wait.delete("1.0", END)
    inside.delete("1.0", END)
    done.delete("1.0", END)

    a = int(a)
    b = int(b)
    c = int(c)
    
    wait.tag_configure("tag_name", justify='center')
    wait.pack()
    wait.insert(END, a)
    wait.tag_add("tag_name", "1.0", "end")
    wait.config(state = "disabled")
    wait.place(x = 78, y = 90)

    inside.tag_configure("tag_name", justify='center')
    inside.pack()
    inside.insert(END, b)
    inside.tag_add("tag_name", "1.0", "end")
    inside.config(state = "disabled")
    inside.place(x = 478, y = 90)

    done.tag_configure("tag_name", justify='center')
    done.pack()
    done.insert(END, c)
    done.tag_add("tag_name", "1.0", "end")
    done.config(state = "disabled")
    done.place(x = 878, y = 90)

    mk = "[" + str(a) + ".wait, " + str(b) + ".inside, " + str(c) + ".done]";
    text_area.config(state = "normal")
    text_area.delete("1.0", END)
    text_area.insert(INSERT, "Marking obtained after firing:\n")
    text_area.insert(INSERT, mk)
    text_area.config(state = "disabled")

def clear():
    text_area.config(state = "normal")
    text_area.delete("1.0", END)
    text_area.config(state = "disabled")

wait = Text(frame, font = "Arial 10", bg = "silver", width = 6, height = 1, fg = "navy")
inside = Text(frame, font = "Arial 10", bg = "silver", width = 6, height = 1, fg = "navy")
done = Text(frame, font = "Arial 10", bg = "silver", width = 6, height = 1, fg = "navy")

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

input_wait = Entry(frame_input, width = 55, bg = "snow")
input_wait.pack()
input_wait.place(x = 70, y = 55)

input_inside = Entry(frame_input, width = 55, bg = "snow")
input_inside.pack()
input_inside.place(x = 70, y = 105)

input_done = Entry(frame_input, width = 55, bg = "snow")
input_done.pack()
input_done.place(x = 70, y = 155)

Enter_token = Button(frame_input, text = "Enter", font = "Arial 14", fg = "royalblue", bg = "lavender", padx = 5, pady = 5, command = enter)
Enter_token.pack()
Enter_token.place(x = 380, y = 185)

text_area = scrolledtext.ScrolledText(frame2, wrap = tk.WORD, width = 54, height = 12, font = ("Times New Roman", 13))
text_area.pack()
text_area.place(y = 0)
text_area.config(state = "disabled")

Clear = Button(frame2, text = "Clear", font = "Arial 14", fg = "royalblue", bg = "lavender", padx = 5, pady = 5, command = clear)
Clear.pack()
Clear.place(x = 425, y = 185)

window.mainloop()
