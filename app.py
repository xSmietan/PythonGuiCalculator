from tkinter import *
import tkinter.font as font
from math import factorial
import parser

# creating the window for calculator
root = Tk()
root.attributes("-alpha", 0.95)
root["bg"] = "#2f2f2f"
root.title("GUI Calculator")

# responsive design for every row and col
n_rows = 7
n_col = 4
for i in range(n_rows):
    root.grid_rowconfigure(i, weight=1)
for i in range(n_col):
    root.grid_columnconfigure(i, weight=1)

# font for display
myDisplayFont = font.Font(family='Helvetica', size=20)

# adding input field
display = Entry(root)
display.grid(row=1, columnspan=6, ipady=10, sticky=N+E+W+S)
display['bg'] = '#2f2f2f'
display['font'] = myDisplayFont
display['fg'] = 'white'
display['justify'] = RIGHT

# changing font to make it bigger
myFont = font.Font(family='Helvetica', size=10)

# i keeps the track of current position on the input text field
i = 0


# Receives the digit as parameter and display it on the input field
def get_variables(param):
    global i
    display.insert(i, param)
    i += 1


# mapping operator buttons
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


# mapping AC button
def clear_all():
    display.delete(0, END)


# mapping undo button
def undo():
    entire_string = display.get()
    new_string = entire_string[:-1]
    clear_all()
    display.insert(0, new_string)


# mapping = button
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Err")


# mapping factorial button
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Err")


# adding buttons
Button(root, text="AC", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: clear_all()).grid(
    row=2, column=0, padx=1, pady=1, sticky=N+S+E+W)
Button(root, text="<-", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: undo()
       ).grid(row=2, column=1, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="%", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_operation(
    "%")).grid(row=2, column=2, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="x^2", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_operation(
    "**2")).grid(row=2, column=3, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="x!", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: fact()).grid(
    row=3, column=0, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="(", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_operation(
    "(")).grid(row=3, column=1, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text=")", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_operation(
    ")")).grid(row=3, column=2, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="/", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_operation(
    "/")).grid(row=3, column=3, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="7", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_variables(
    "7")).grid(row=4, column=0, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="8", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_variables(
    "8")).grid(row=4, column=1, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="9", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_variables(
    "9")).grid(row=4, column=2, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="*", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_operation(
    "*")).grid(row=4, column=3, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="4", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_variables(
    "4")).grid(row=5, column=0, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="5", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_variables(
    "5")).grid(row=5, column=1, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="6", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_variables(
    "6")).grid(row=5, column=2, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="-", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_operation(
    "-")).grid(row=5, column=3, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="1", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_variables(
    "1")).grid(row=6, column=0, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="2", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_variables(
    "2")).grid(row=6, column=1, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="3", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_variables(
    "3")).grid(row=6, column=2, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="+", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_operation(
    "+")).grid(row=6, column=3, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="+/-", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_operation(
    "+/-")).grid(row=7, column=0, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="0", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_variables(
    "0")).grid(row=7, column=1, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text=",", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: get_variables(
    ",")).grid(row=7, column=2, padx=1, ipady=1, sticky=N+S+E+W)
Button(root, text="=", height=3, width=10, bg="#2f2f2f", fg="white", font=myFont, command=lambda: calculate()).grid(
    row=7, column=3, padx=1, ipady=1, sticky=N+S+E+W)


root.mainloop()
