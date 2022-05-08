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
    
