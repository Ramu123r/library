# 18. Write a python program to draw shapes & GUI controls.
from tkinter import *

root = Tk()
root.title("Shapes and GUI Controls")

# GUI Control
label = Label(root, text="Hello Python")
label.pack()

button = Button(root, text="Click Me")
button.pack()

# Drawing Shapes
canvas = Canvas(root, width=300, height=200)
canvas.pack()

canvas.create_rectangle(50, 50, 150, 100)
canvas.create_oval(170, 50, 270, 100)

root.mainloop()