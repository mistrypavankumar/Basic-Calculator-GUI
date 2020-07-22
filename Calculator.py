from tkinter import *

def Add():
    result = number1.get() + number2.get()
    Label(f1, text = f"{str(result)}" ).grid(row = 3, column = 0)

def Sub():
    result = number1.get() - number2.get()
    Label(f1, text = f"{str(result)}" ).grid(row = 3, column = 0)

def Multi():
    result = number1.get() * number2.get()
    Label(f1, text = f"{str(result)}" ).grid(row = 3, column = 0)

def Div():
    result = number1.get() / number2.get()
    Label(f1, text = f"{str(result)}" ).grid(row = 3, column = 0)





root = Tk()
root.title("Basic Calculator")
root.geometry("500x50")
root.minsize(500,350)
root.maxsize(500,350)

frame = Frame(root, width = 500, height = 100, pady = 20)
label = Label(frame, text = "Basic Calculator", font = "Times 20 bold")
label.pack()
frame.pack()

f1 = Frame(root, width = 400, height = 200, pady = 10)
Label(f1, text = "Enter first number : ",pady = 10).grid(row = 1, column = 0)
Label(f1, text = "Enter second number : ",pady = 10).grid(row = 2, column = 0)

number1 = IntVar()
number2 = IntVar()

num1 = Entry(f1, textvariable = number1)
num2 = Entry(f1, textvariable = number2)
num1.grid(row = 1,column = 1)
num2.grid(row = 2, column = 1)

add = Button(f1, text = "Add two numbers", command = Add, pady = 5, padx = 5)
add.grid(row = 3, column = 1)

add = Button(f1, text = "sub two numbers", command = Sub, pady = 5, padx= 6)
add.grid(row = 4, column = 1)

add = Button(f1, text = "Mutli two numbers", command = Multi, pady =5)
add.grid(row = 5, column = 1)

add = Button(f1, text = "Div two numbers", command = Div, pady =5, padx = 6)
add.grid(row = 6, column = 1)

f1.pack()






root.mainloop()