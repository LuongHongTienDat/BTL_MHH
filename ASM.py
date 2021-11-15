import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

class Place:
    def __init__(self, name = "", token = 0):
        self.name = name
        self.token = token

class Transition:
    def __init__(self, inputplace = [], outputplace = []):
        self.inputplace = inputplace
        self.outputplace = outputplace

    def fire(t):
        for i in range(len(t.inputplace)):
            if t.inputplace[i].token < 1:
                return False
            else: t.inputplace[i].token = t.inputplace[i].token - 1
        for i in range(len(t.outputplace)):
            t.outputplace[i].token = t.outputplace[i].token + 1
        return True

class PetriNet:
    def __init__(self, transMap = {}, placeSet = []):
        self.transMap = transMap
        self.placeSet = placeSet
    
    def printNet(N):
        print("[", end = '')
        for i in range(len(N.placeSet)):
            if i != 0: print(", ", end = '')
            print(N.placeSet[i].name, ".", N.placeSet[i].token, sep = '', end = '')
        print("]")

def UI_1():
    window = tk.Tk()
    window.resizable(False, False)

    window.title("The specialists' Petri Net")
    frame = Frame(window, bd = 10, bg = "silver")
    frame.pack(side = TOP)
    frame2 = Frame(window, bd = 10, bg = "silver")
    frame2.pack(side = RIGHT)
    frame_input = Frame(window, bd = 10, bg = "silver")
    frame_input.pack(side = LEFT)

    canvas = tk.Canvas(frame, bd = 1, height=330, width=1000)
    canvas.pack()
    canvas2 = tk.Canvas(frame2, bd = 1, height=280, width=500)
    canvas2.pack()
    canvas_input = tk.Canvas(frame_input, bd = 1, height=280, width=500)
    canvas_input.pack()
    window.geometry("1000x610")

    def create_circle(x, y, r, canvasName):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill = "silver")

    create_circle(295, 75, 30, canvas)  
    create_circle(500, 200, 30, canvas)  
    create_circle(705, 75, 30, canvas)  

    canvas.create_line(260, 200, 470, 200, arrow=tk.LAST)
    canvas.create_line(530, 200, 660, 200, arrow=tk.LAST)

    canvas.create_line(705, 175, 705, 105, arrow=tk.LAST)
    canvas.create_line(675, 75, 530, 75, arrow=tk.LAST)  
    canvas.create_line(465, 75, 325, 75, arrow=tk.LAST) 
    canvas.create_line(295, 105, 295, 175, arrow=tk.LAST)  

    canvas.create_text(500, 240, fill="dimgrey", font="Arial 14", text="busy")
    canvas.create_text(295, 30, fill="dimgrey", font="Arial 14", text="free")
    canvas.create_text(705, 30, fill="dimgrey", font="Arial 14", text="docu")

    def startclick():
        free.config(state="normal")
        busy.config(state="normal")

        if free.get("1.0", END) == '\n':
            messagebox.showerror("Error!!!", "Please input before firing.")
            return

        a = int(free.get("1.0", END))

        if a == 0:
            messagebox.showerror("Error!!!", "Transition 'start' is not enabled")
            return

        b = int(busy.get("1.0", END))
        c = int(docu.get("1.0", END))

        free.delete("1.0", END)
        busy.delete("1.0", END)

        a = a - 1
        b = b + 1

        free.tag_configure("tag_name", justify='center')
        free.insert(END, a)
        free.tag_add("tag_name", "1.0", "end")

        busy.tag_configure("tag_name", justify='center')
        busy.insert(END, b)
        busy.tag_add("tag_name", "1.0", "end")

        free.config(state = "disabled")
        busy.config(state = "disabled")

        mk = "\n[" + str(a) + ".free, " + str(b) + ".busy, " + str(c) + ".docu]";
        text_area.config(state = "normal")
        text_area.insert(INSERT, mk)
        text_area.config(state = "disabled")


    def changeclick():
        docu.config(state="normal")
        busy.config(state="normal")

        if docu.get("1.0", END) == '\n':
            messagebox.showerror("Error!!!", "Please input before firing.")
            return

        b = int(busy.get("1.0", END))

        if b == 0:
            messagebox.showerror("Error!!!", "Transition 'change' is not enabled.")
            return

        a = int(free.get("1.0", END))
        c = int(docu.get("1.0", END))

        busy.delete("1.0", END)
        docu.delete("1.0", END)

        b = b - 1
        c = c + 1

        busy.tag_configure("tag_name", justify='center')
        busy.insert(END, b)
        busy.tag_add("tag_name", "1.0", "end")

        docu.tag_configure("tag_name", justify='center')
        docu.insert(END, c)
        docu.tag_add("tag_name", "1.0", "end")

        busy.config(state = "disabled")
        docu.config(state = "disabled")

        mk = "\n[" + str(a) + ".free, " + str(b) + ".busy, " + str(c) + ".docu]";
        text_area.config(state = "normal")
        text_area.insert(INSERT, mk)
        text_area.config(state = "disabled")

    def endclick():
        free.config(state = "normal")
        docu.config(state = "normal")

        if docu.get("1.0", END) == '\n':
            messagebox.showerror("Error!!!", "Please input before firing.")
            return

        a = int(free.get("1.0", END))
        b = int(busy.get("1.0", END))
        c = int(docu.get("1.0", END))

        if c == 0:
            messagebox.showerror("Error!!!", "Transition 'end' is not enabled.")
            return

        free.delete("1.0", END)
        docu.delete("1.0", END)

        a = a + 1
        c = c - 1

        free.tag_configure("tag_name", justify='center')
        free.insert(END, a)
        free.tag_add("tag_name", "1.0", "end")

        docu.tag_configure("tag_name", justify='center')
        docu.insert(END, c)
        docu.tag_add("tag_name", "1.0", "end")

        free.config(state="disabled")
        docu.config(state="disabled")

        mk = "\n[" + str(a) + ".free, " + str(b) + ".busy, " + str(c) + ".docu]";
        text_area.config(state = "normal")
        text_area.insert(INSERT, mk)
        text_area.config(state = "disabled")

    def enter():
        a = input_free.get()
        b = input_busy.get()
        c = input_docu.get()

        input_free.delete(0, END)
        input_busy.delete(0, END)
        input_docu.delete(0, END)

        if a.isnumeric() == False or b.isnumeric() == False or c.isnumeric() == False:
            messagebox.showerror("Error!!!", "Your input is not a positive number.")
            return

        free.config(state = "normal")
        busy.config(state = "normal")
        docu.config(state = "normal")

        free.delete("1.0", END)
        busy.delete("1.0", END)
        docu.delete("1.0", END)

        a = int(a)
        b = int(b)
        c = int(c)
        
        free.tag_configure("tag_name", justify='center')
        free.pack()
        free.insert(END, a)
        free.tag_add("tag_name", "1.0", "end")
        free.config(state = "disabled")
        free.place(x = 273, y = 66)

        busy.tag_configure("tag_name", justify='center')
        busy.pack()
        busy.insert(END, b)
        busy.tag_add("tag_name", "1.0", "end")
        busy.config(state = "disabled")
        busy.place(x = 478, y = 191)

        docu.tag_configure("tag_name", justify='center')
        docu.pack()
        docu.insert(END, c)
        docu.tag_add("tag_name", "1.0", "end")
        docu.config(state = "disabled")
        docu.place(x = 683, y = 66)

        mk = "[" + str(a) + ".free, " + str(b) + ".busy, " + str(c) + ".docu]";
        text_area.config(state = "normal")
        text_area.delete("1.0", END)
        text_area.insert(INSERT, "Marking obtained after firing:\n")
        text_area.insert(INSERT, mk)
        text_area.config(state = "disabled")

    def clear():
        text_area.config(state = "normal")
        text_area.delete("1.0", END)
        text_area.config(state = "disabled")

    free = Text(frame, font="Arial 10", bg="silver", width=6, height=1, fg="navy")
    busy = Text(frame, font="Arial 10", bg="silver", width=6, height=1, fg="navy")
    docu = Text(frame, font="Arial 10", bg="silver", width=6, height=1, fg="navy")

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

    L_input = Label(frame_input, text = "Input the number of tokens ", font="Arial 14")
    L_input.pack()
    L_input.place(x=100, y=20)

    L_free = Label(frame_input, text = "Free: ", font = "Arial 14")
    L_free.pack()
    L_free.place(y = 50)

    L_busy = Label(frame_input, text = "Busy: ", font = "Arial 14")
    L_busy.pack()
    L_busy.place(y = 100)

    L_docu = Label(frame_input, text = "Docu: ", font = "Arial 14")
    L_docu.pack()
    L_docu.place(y = 150)

    input_free = Entry(frame_input, width = 55, bg = "snow")
    input_free.pack()
    input_free.place(x = 70, y = 55)

    input_busy = Entry(frame_input, width = 55, bg = "snow")
    input_busy.pack()
    input_busy.place(x = 70, y = 105)

    input_docu = Entry(frame_input, width = 55, bg = "snow")
    input_docu.pack()
    input_docu.place(x = 70, y = 155)

    Enter_token = Button(frame_input, text="Enter", font="Arial 14", fg="royalblue", bg="lavender", padx=5, pady=5,
                        command=enter)
    Enter_token.pack()
    Enter_token.place(x = 380, y = 185)

    text_area = scrolledtext.ScrolledText(frame2, wrap=tk.WORD, width=54, height=12, font=("Times New Roman", 13))
    text_area.pack()
    text_area.place(y=0)
    text_area.config(state="disabled")

    Clear = Button(frame2, text="Clear", font="Arial 14", fg="royalblue", bg="lavender", padx=5, pady=5, command=clear)
    Clear.pack()
    Clear.place(x = 425, y = 185)

    window.mainloop()

def UI_2():
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

        if wait.get("1.0", END) == '\n':
            messagebox.showerror("Error!!!", "Please input before firing.")
            return

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

        if inside.get("1.0", END) == '\n':
            messagebox.showerror("Error!!!", "Please input before firing.")
            return

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

def UI_3():
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

    create_circle(100, 200, 30, canvas)
    create_circle(500, 320, 30, canvas) 
    create_circle(900, 200, 30, canvas)

    create_circle(295, 75, 30, canvas)
    create_circle(500, 200, 30, canvas) 
    create_circle(705, 75, 30, canvas)  

    canvas.create_line(130, 200, 260, 200, arrow=tk.LAST)
    canvas.create_line(260, 200, 470, 200, arrow=tk.LAST)
    canvas.create_line(530, 200, 660, 200, arrow=tk.LAST)
    canvas.create_line(670, 200, 870, 200, arrow=tk.LAST)

    canvas.create_line(705, 175, 705, 105, arrow=tk.LAST)
    canvas.create_line(675, 75, 530, 75, arrow=tk.LAST) 
    canvas.create_line(465, 75, 325, 75, arrow=tk.LAST) 
    canvas.create_line(295, 105, 295, 175, arrow=tk.LAST) 

    canvas.create_line(295, 230, 295, 320) 
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

        if free.get("1.0", END) == '\n':
            messagebox.showerror("Error!!!", "Please input before firing.")
            return

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

        if free.get("1.0", END) == '\n':
            messagebox.showerror("Error!!!", "Please input before firing.")
            return

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
        if free.get("1.0", END) == '\n':
            messagebox.showerror("Error!!!", "Please input before firing.")
            return
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
        docu.config(state="normal")
        done.config(state="normal")
        busy.config(state="normal")
        inside.config(state="normal")

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

def problem_1():
    UI_1()

    free = Place("Free", 0)
    busy = Place("Busy", 0)
    docu = Place("Docu", 0)

    start = Transition([free], [busy])
    change = Transition([busy], [docu])
    end = Transition([docu], [free])

    SpecialistNet = PetriNet()
    SpecialistNet.transMap["start"] = start
    SpecialistNet.transMap["change"] = change
    SpecialistNet.transMap["end"] = end
    SpecialistNet.placeSet = [free, busy, docu]

    print("Format: {x.free, y.busy, z.docu}\n")
    free.token = int(input("Enter x: "))
    busy.token = int(input("Enter y: "))
    docu.token = int(input("Enter z: "))

    if free.token < 0 or free.token > 10 or busy.token < 0 or busy.token > 10 or docu.token < 0 or docu.token > 10:
        print("Exception: The number of specialists must be from 0 to 10!!!")
        return

    cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

    while cmd != "END":
        if cmd != "start" and cmd != "change" and cmd != "end":
            print(cmd, "is not a transition")
        else:
            if SpecialistNet.transMap[cmd].fire() == True:
                print("Marking obtained after firing:")
                SpecialistNet.printNet()
            else: 
                print(cmd, "is not currently enabled")
                if cmd == "start": print("\"No specialists are free\"")
                elif cmd == "change": print("\"No specialists are treating\"")
                else: print("\"No specialists are documenting\"") 
        cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

def problem_2():
    UI_2()

    wait = Place("Wait", 0)
    inside = Place("Inside", 0)
    done = Place("Done", 0)

    start = Transition([wait], [inside])
    change = Transition([inside], [done])

    SpecialistNet = PetriNet()
    SpecialistNet.transMap["start"] = start
    SpecialistNet.transMap["change"] = change
    SpecialistNet.placeSet = [wait, inside, done]

    print("Format: {x.wait, y.inside, z.done}\n")
    wait.token = int(input("Enter x: "))
    inside.token = int(input("Enter y: "))
    done.token = int(input("Enter z: "))

    if wait.token < 0 or wait.token > 10 or inside.token < 0 or inside.token > 10 or done.token < 0 or done.token > 10:
        print("Exception: The number of patients must be from 0 to 10!!!")
        return

    cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

    while cmd != "END":
        if cmd != "start" and cmd != "change":
            print(cmd, "is not a transition")
        else:
            if SpecialistNet.transMap[cmd].fire() == True:
                print("Marking obtained after firing:")
                SpecialistNet.printNet()
            else: 
                print(cmd, "is not currently enabled")
                if cmd == "start": print("\"No patients are waiting\"")
                else: print("\"No patients are being treated\"")
            if wait.token == 0 and inside.token == 0:
                print("\nNOTE: All of patients have been done treatment!!!")
                return
        cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

def problem_3():
    UI_3()

    wait = Place("Wait", 0)
    inside = Place("Inside", 0)
    done = Place("Done", 0)
    free = Place("Free", 0)
    busy = Place("Busy", 0)
    docu = Place("Docu", 0)

    start = Transition([free, wait], [busy, inside])
    change = Transition([busy, inside], [docu, done])
    end = Transition([docu], [free])

    SpecialistNet = PetriNet()
    SpecialistNet.transMap["start"] = start
    SpecialistNet.transMap["change"] = change
    SpecialistNet.transMap["end"] = end
    SpecialistNet.placeSet = [wait, inside, done, free, busy, docu]

    print("Format: {x.wait, y.inside, z.done, a.free, b.busy, c.docu}\n")
    wait.token = int(input("Enter x: "))
    inside.token = int(input("Enter y: "))
    done.token = int(input("Enter z: "))
    free.token = int(input("Enter a: "))
    busy.token = int(input("Enter b: "))
    done.token = int(input("Enter c: "))

    if wait.token < 0 or wait.token > 10 or inside.token < 0 or inside.token > 10 or done.token < 0 or done.token > 10 or free.token < 0 or free.token > 10 or busy.token < 0 or busy.token > 10 or docu.token < 0 or docu.token > 10:
        print("Exception: The number of tokens must be from 0 to 10!!!")
        return

    cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

    while cmd != "END":
        if cmd != "start" and cmd != "change" and cmd != "end":
            print(cmd, "is not a transition")
        else:
            if SpecialistNet.transMap[cmd].fire() == True:
                print("Marking obtained after firing:")
                SpecialistNet.printNet()
            else: 
                print(cmd, "is not currently enabled")
                if cmd == "start":
                    if wait.token == 0: print("\"No patients are waiting\"")
                    else: print("No specialists are free")
                elif cmd == "change":
                    print("\"No treatments are occurring\"")
                else: print("\"The specialist isn't documenting\"")
            if wait.token == 0 and inside.token == 0 and busy.token == 0 and docu.token == 0:
                print("\nNOTE: All of patients have been done treatment and specialists are free!!!")
                return
        cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

def problem_4():
    x = int(input("Format: {x.wait, 0.inside, 1.done, 1.free, 0.busy, 0.docu}\nEnter the number of patients x: "))
    
    if x < 0 or x > 10:
        print("Exception: The number of patients must be from 0 to 10!!!")
        return

    marking_key = ["wait", "inside", "done", "free", "busy", "docu"]
    marking_value = [x, 0, 1, 1, 0, 0]

    str = ""
    for i in range(x * 3 + 1):
        print("Firing sequence: [", str, "]\nMarking: [", sep = '', end = '')
        for k in range(6):
            if k != 5: print(marking_key[k], ".", marking_value[k], ", ", sep = '', end = '')
            else: print(marking_key[k], ".", marking_value[k], "]\n", sep = '')
        
        if i % 3 == 0:
            marking_value[0] = marking_value[0] - 1
            marking_value[3] = marking_value[3] - 1
            marking_value[1] = marking_value[1] + 1
            marking_value[4] = marking_value[4] + 1
        
        elif i % 3 == 1:
            marking_value[1] = marking_value[1] - 1
            marking_value[4] = marking_value[4] - 1
            marking_value[2] = marking_value[2] + 1
            marking_value[5] = marking_value[5] + 1

        else:
            marking_value[5] = marking_value[5] - 1
            marking_value[3] = marking_value[3] + 1
        
        str = str + ("start" if str == "" else ",start" if i % 3 == 0 else ",change" if i % 3 == 1 else ",end")

def main():
    a = input("Input the problem you want to solve: ")
    if a == '1':
        problem_1()
    elif a == '2':
        problem_2()
    elif a == '3':
        problem_3()
    elif a == '4':
        problem_4()
    else: print("Exception: Your input must be from 1 to 4!!!")

if __name__ == "__main__":
    main()