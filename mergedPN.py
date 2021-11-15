import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

window = tk.Tk()
window.resizable(False, False)

window.title("The patients' Petri Net")
frame = Frame(window, bd=10, bg="silver")
frame.pack(side=TOP)
frame2 = Frame(window, bd=10, bg="silver")
frame2.pack(side=RIGHT)
frame_input = Frame(window, bd=10, bg="silver")
frame_input.pack(side=LEFT)

canvas = tk.Canvas(frame, bd=1, height=380, width=1000)
canvas.pack()
canvas2 = tk.Canvas(frame2, bd=1, height=280, width=500)
canvas2.pack()
canvas_input = tk.Canvas(frame_input, bd=1, height=280, width=500)
canvas_input.pack()
window.geometry("1000x640")


def create_circle(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill="silver")


create_circle(100, 200, 30, canvas)  #wait
create_circle(500, 320, 30, canvas)  #inside
create_circle(900, 200, 30, canvas) #done

create_circle(295, 75, 30, canvas)  #free
create_circle(500, 200, 30, canvas)  #busy
create_circle(705, 75, 30, canvas)  #docu




canvas.create_line(130, 200, 260, 200, arrow=tk.LAST)
canvas.create_line(260, 200, 470, 200, arrow=tk.LAST)
canvas.create_line(530, 200, 660, 200, arrow=tk.LAST)
canvas.create_line(670, 200, 870, 200, arrow=tk.LAST)

canvas.create_line(705, 175, 705, 105, arrow=tk.LAST)
canvas.create_line(675, 75, 530, 75, arrow=tk.LAST)   #docu->end
canvas.create_line(465, 75, 325, 75, arrow=tk.LAST)  #end->free
canvas.create_line(295, 105, 295, 175, arrow=tk.LAST)  #free->start

canvas.create_line(295, 230, 295, 320)  #down
canvas.create_line(295, 320, 470, 320, arrow=tk.LAST)
canvas.create_line(530, 320, 705, 320)
canvas.create_line(705, 320, 705, 230, arrow=tk.LAST)





canvas.create_text(100, 240, fill="dimgrey", font="Arial 14", text="wait")
canvas.create_text(500, 240, fill="dimgrey", font="Arial 14", text="busy")
canvas.create_text(900, 240, fill="dimgrey", font="Arial 14", text="done")
canvas.create_text(295, 30, fill="dimgrey", font="Arial 14", text="free")
canvas.create_text(500, 360, fill="dimgrey", font="Arial 14", text="inside")
canvas.create_text(705, 30, fill="dimgrey", font="Arial 14", text="docu")


def startclick():
    wait.config(state="normal")
    free.config(state="normal")
    busy.config(state="normal")
    inside.config(state="normal")



    a = int(wait.get("1.0", END))
    b = int(free.get("1.0", END))

    if a == 0 or b==0:
        messagebox.showerror("Error!!!", "Transition 'start' is not enabled")
        return

    c = int(inside.get("1.0", END))
    d = int(busy.get("1.0", END))

    wait.delete("1.0", END)
    inside.delete("1.0", END)
    free.delete("1.0", END)
    busy.delete("1.0", END)

    a = a - 1
    b = b - 1
    c = c + 1
    d = d + 1

    wait.tag_configure("tag_name", justify='center')
    wait.insert(END, a)
    wait.tag_add("tag_name", "1.0", "end")

    inside.tag_configure("tag_name", justify='center')
    inside.insert(END, c)
    inside.tag_add("tag_name", "1.0", "end")

    free.tag_configure("tag_name", justify='center')
    free.insert(END, b)
    free.tag_add("tag_name", "1.0", "end")

    busy.tag_configure("tag_name", justify='center')
    busy.insert(END, d)
    busy.tag_add("tag_name", "1.0", "end")

    wait.config(state="disabled")
    inside.config(state="disabled")

    e=int(done.get("1.0", END))
    f=int(docu.get("1.0", END))
    mk = "\n[" + str(a) + ".wait, " + str(c) + ".inside, "  + str(e)+ ".done, " + str(b) + ".free, " + str(d) + ".busy, " + str(f) + ".docu]";
    text_area.config(state="normal")
    text_area.insert(INSERT, mk)
    text_area.config(state="disabled")


def changeclick():
    inside.config(state="normal")
    done.config(state="normal")
    docu.config(state="normal")
    busy.config(state="normal")

    a = int(inside.get("1.0", END))
    b = int(busy.get("1.0", END))

    if a==0 or b==0:
        messagebox.showerror("Error!!!", "Transition 'change' is not enabled.")
        return

    c = int(done.get("1.0", END))
    d = int(docu.get("1.0", END))

    inside.delete("1.0", END)
    done.delete("1.0", END)
    busy.delete("1.0", END)
    docu.delete("1.0", END)

    a = a - 1
    b = b - 1
    c = c + 1
    d = d + 1

    inside.tag_configure("tag_name", justify='center')
    inside.insert(END, a)
    inside.tag_add("tag_name", "1.0", "end")

    done.tag_configure("tag_name", justify='center')
    done.insert(END, c)
    done.tag_add("tag_name", "1.0", "end")

    busy.tag_configure("tag_name", justify='center')
    busy.insert(END, b)
    busy.tag_add("tag_name", "1.0", "end")

    docu.tag_configure("tag_name", justify='center')
    docu.insert(END, d)
    docu.tag_add("tag_name", "1.0", "end")

    inside.config(state="disabled")
    done.config(state="disabled")
    busy.config(state="disabled")
    docu.config(state="disabled")

    e = int(wait.get("1.0", END))
    f = int(free.get("1.0", END))
    mk = "\n[" + str(e) + ".wait, " + str(a) + ".inside, " + str(c) + ".done, " + str(f) + ".free, " + str(b) + ".busy, " + str(d) + ".docu]";
    text_area.config(state="normal")
    text_area.insert(INSERT, mk)
    text_area.config(state="disabled")

def endclick():
    free.config(state="normal")
    docu.config(state="normal")

    a = int(free.get("1.0", END))
    b = int(docu.get("1.0", END))

    if b==0 :
        messagebox.showerror("Error!!!", "Transition 'end' is not enabled.")
        return

    free.delete("1.0", END)
    docu.delete("1.0", END)

    a = a + 1
    b = b - 1

    free.tag_configure("tag_name", justify='center')
    free.insert(END, a)
    free.tag_add("tag_name", "1.0", "end")

    docu.tag_configure("tag_name", justify='center')
    docu.insert(END, b)
    docu.tag_add("tag_name", "1.0", "end")


    free.config(state="disabled")
    docu.config(state="disabled")

    c = int(wait.get("1.0", END))
    d = int(inside.get("1.0", END))
    e = int(done.get("1.0", END))
    f = int(busy.get("1.0", END))
    mk = "\n[" + str(c) + ".wait, " + str(d) + ".inside, " + str(e) + ".done, " + str(a) + ".free, " + str(f) + ".busy, " + str(b) + ".docu]";
    text_area.config(state="normal")
    text_area.insert(INSERT, mk)
    text_area.config(state="disabled")


def enter():
    a = input_wait.get()
    b = input_free.get()
    input_wait.delete(0, END)
    input_free.delete(0, END)
    if a.isnumeric() == False or b.isnumeric() == False:
        messagebox.showerror("Error!!!", "Your input is not a positive number.")
        return

    wait.config(state="normal")
    free.config(state="normal")

    wait.delete("1.0", END)
    free.delete("1.0", END)
    busy.delete("1.0", END)
    inside.delete("1.0", END)
    done.delete("1.0", END)
    docu.delete("1.0", END)


    a = int(a)
    b = int(b)

    wait.tag_configure("tag_name", justify='center')
    wait.pack()
    wait.insert(END, a)
    wait.tag_add("tag_name", "1.0", "end")
    wait.config(state="disabled")
    wait.place(x=78, y=190)

    inside.tag_configure("tag_name", justify='center')
    inside.pack()
    inside.insert(END, 0)
    inside.tag_add("tag_name", "1.0", "end")
    inside.config(state="disabled")
    inside.place(x=478, y=311)

    done.tag_configure("tag_name", justify='center')
    done.pack()
    done.insert(END, 0)
    done.tag_add("tag_name", "1.0", "end")
    done.config(state="disabled")
    done.place(x=878, y=191)

    free.tag_configure("tag_name", justify='center')
    free.pack()
    free.insert(END, b)
    free.tag_add("tag_name", "1.0", "end")
    free.config(state="disabled")
    free.place(x=273, y=66)

    busy.tag_configure("tag_name", justify='center')
    busy.pack()
    busy.insert(END, 0)
    busy.tag_add("tag_name", "1.0", "end")
    busy.config(state="disabled")
    busy.place(x=478, y=191)

    docu.tag_configure("tag_name", justify='center')
    docu.pack()
    docu.insert(END, 0)
    docu.tag_add("tag_name", "1.0", "end")
    docu.config(state="disabled")
    docu.place(x=683, y=66)

    mk = "[" + str(a) + ".wait, " + str(0) + ".inside, " + str(0) + ".done, " + str(b) + ".free, " + str(0) + ".busy, "+ str(0) + ".docu]";
    text_area.config(state="normal")
    text_area.delete("1.0", END)
    text_area.insert(INSERT, " Initial marking:\n")
    text_area.insert(INSERT, mk)
    text_area.insert(INSERT, "\n Markings after firing:")
    text_area.config(state="disabled")


def clear():
    text_area.config(state="normal")
    text_area.delete("1.0", END)
    text_area.config(state="disabled")


wait = Text(frame, font="Arial 10", bg="silver", width=6, height=1, fg="navy")
inside = Text(frame, font="Arial 10", bg="silver", width=6, height=1, fg="navy")
done = Text(frame, font="Arial 10", bg="silver", width=6, height=1, fg="navy")
free = Text(frame, font="Arial 10", bg="silver", width=6, height=1, fg="navy")
busy = Text(frame, font="Arial 10", bg="silver", width=6, height=1, fg="navy")
docu = Text(frame, font="Arial 10", bg="silver", width=6, height=1, fg="navy")


#Button
transition1 = Button(frame, text="start", font="Arial 14", fg="steelblue", bg="aqua", padx=10, pady=10,
                     command=startclick)
transition1.pack()
transition1.place(x=260, y=175)
transition2 = Button(frame, text="change", font="Arial 14", fg="steelblue", bg="aqua", padx=10, pady=10,
                     command=changeclick)
transition2.pack()
transition2.place(x=660, y=175)
transition3 = Button(frame, text="end", font="Arial 14", fg="steelblue", bg="aqua", padx=10, pady=10,
                     command=endclick)
transition3.pack()
transition3.place(x=465, y=45)





L_input = Label(frame_input, text="Input the number of tokens ", font="Arial 14")
L_input.pack()
L_input.place(x=100, y=20)

L_wait = Label(frame_input, text="Wait: ", font="Arial 14")
L_wait.pack()
L_wait.place(x=20,y=60)

L_free = Label(frame_input, text="Free: ", font="Arial 14")
L_free.pack()
L_free.place(x=20,y=110)

input_wait = Entry(frame_input, width=55, bg="snow")
input_wait.pack()
input_wait.place(x=80, y=65)

input_free = Entry(frame_input,width=55,bg="snow")
input_free.pack()
input_free.place(x=80,y=116)

Enter_token = Button(frame_input, text="Enter", font="Arial 14", fg="royalblue", bg="lavender", padx=5, pady=5,
                     command=enter)
Enter_token.pack()
Enter_token.place(x=340, y=155)

text_area = scrolledtext.ScrolledText(frame2, wrap=tk.WORD, width=54, height=12, font=("Times New Roman", 13))
text_area.pack()
text_area.place(y=0)
text_area.config(state="disabled")

Clear = Button(frame2, text="Clear", font="Arial 14", fg="royalblue", bg="lavender", padx=5, pady=5, command=clear)
Clear.pack()
Clear.place(x=425, y=155)

window.mainloop()
