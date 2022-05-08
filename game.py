from tkinter import *
from math import *

root= Tk()
root.title("Calculator")
root.configure(background="white", padx=5, pady=5)
root.resizable(width=False, height=False)

expression= ""
status= False

text_input = Entry(root, width=50, relief=FLAT, justify=LEFT)
text_input.grid(row=0, column=0, columnspan=6, ipady=100)
text_input.focus_set()