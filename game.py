from sre_parse import FLAGS
from tkinter import *
from math import *
from turtle import clear

root= Tk()
root.title("Calculator")
root.configure(background="white", padx=5, pady=5)
root.resizable(width=False, height=False)

expression= ""
status= False

text_input = Entry(root, width=50, relief=FLAT, justify=LEFT)
text_input.grid(row=0, column=0, columnspan=6, ipady=100)
text_input.focus_set()

def get_expr(operand=""):
    global status
    if str(operand).isdigit() and status == True:
        clear()
        status = False
    status = False
    global expression
    expression = text_input.get() + str(operand)
    return expression

def btn_click(operand):
    expression = get_expr(operand)
    text_input.delete(0, END)
    text_input.insert(0, expression)
    
def solve():
    global status
    expression = get_expr()
    try:
        solution = eval(expression.lower())
        text_input.delete(0, END)
        text_input.insert(0, solution)
    except Exception as e:
        text_input.delete(0, END)
        text_input.insert(0, "Error: " + str(e))
        
    status = True
    
def clear():
    text_input.delete(0, END)
    
def clear_one():
    expression = get_expr()
    text_input.delete(0, END)
    text_input.insert(0, expression[: -1])
    
#First Row

btn_7 = Button(
    root, text="7", width=5, height=3, relief=FLAT, command=lambda: btn_click(7)
)
btn_7.grid(row=1, column=0)

btn_8 = Button(
    root, text="8", width=5, height=3, relief=FLAT, command=lambda: btn_click(8)
)
btn_8.grid(row=1, column=1)

btn_9 = Button(
    root, text="9", width=5, height=3, relief=FLAT, command=lambda: btn_click(9)
)
btn_9.grid(row=1, column=2)

btn_div = Button(
    root, text="/", width=5, height=3, relief=FLAT, command=lambda: btn_click("/")
)
btn_div.grid(row=1, column=3)

btn_cos = Button(root, text="<", width=5, height=3, relief=FLAT, command=clear_one)
btn_cos.grid(row=1, column=4)

btn_reset = Button(root, text="c", width=5, height=3, relief=FLAT, command=clear)
btn_reset.grid(row=1, column=5)

# Second Row
btn_4 = Button(
    root, text="4", width=5, height=3, relief=FLAT, command=lambda: btn_click(4)
)
btn_4.grid(row=2, column=0)

btn_5= Button(
    root, text="5", width=5, height=3, relief=FLAT, command=lambda: btn_click(5)
)
btn_5.grid(row=2, column=1)

btn_6=Button(
    root, text="6", width=5, height=3, relief=FLAT, command=lambda: btn_click(6)
)
btn_6.grid(row=2, column=2)

btn_mul = Button(
    root, text="x", width=5, height=3, relief=FLAT, command=lambda: btn_click("*")
)

btn_mul.grid(
    row=2,
    column=3,
)

btn_ob = Button(
    root, text="(", width=5, height=3, relief=FLAT, command=lambda: btn_click("(")
)
btn_ob.grid(row=2, column=4)

btn_cb = Button(
    root, text=")", width=5, height=3, relief=FLAT, command=lambda: btn_click(")")
)
btn_cb.grid(row=2, column=5)

# Third Row
btn_1 = Button(
    root, text="1", width=5, height=3, relief=FLAT, command=lambda: btn_click(1)
)
btn_1.grid(row=3, column=0)

btn_2 = Button(
    root, text="2", width=5, height=3, relief=FLAT, command=lambda: btn_click(2)
)
btn_2.grid(row=3, column=1)

btn_3 = Button(
    root, text="3", width=5, height=3, relief=FLAT, command=lambda: btn_click(3)
)
btn_3.grid(row=3, column=2)

btn_minus = Button(
    root, text="-", width=5, height=3, relief=FLAT, command=lambda: btn_click("-")
)

btn_minus.grid(row=3, column=3)

btn_sq = Button(
    root, text="x^2", width=5, height=3, relief=FLAT, command=lambda: btn_click("**2")

)
btn_sq.grid(row=3, column=4)

btn_sqrt = Button(
    root,
    text="sqrt(x)",
    width=5,
    height=3,
    relief=FLAT,
    command=lambda: btn_click("**(1/2)"),
)
btn_sqrt.grid(row=3, column=5)

# Forth Row

btn_0 = Button(
    root, text="0", width=5, height=3, relief=FLAT, command=lambda: btn_click(0)
)
btn_0.grid(row=4, column=0)

btn_point = Button(
    root, text=".", width=5, height=3, relief=FLAT, command=lambda: btn_click(".")
)

btn_point.grid(row=4, column=1)

btn_percent = Button(
    root, text="%", width=5, height=3, relief=FLAT, command=lambda: btn_click("%") 
)

btn_percent.grid(row=4, column=2)

btn_plus = Button(
    root, text="+", width=5, height=3, relief=FLAT, command=lambda: btn_click("+")
)
btn_plus.grid(row=4, column=3)

btn_equal = Button(
        root, text="=", width=14, height=3, background="#34b549", relief=FLAT, command=solve
)

btn_equal.grid(row=4, column=4, columnspan=2)

root.mainloop