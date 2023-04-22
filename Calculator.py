from tkinter import *

# Define the window that the program will be run in

root = Tk()
root.title("Calculator")

screen = Entry(root, width=35, borderwidth=5)
screen.grid(row=0, column=0, columnspan=3, padx=10, pady=10) 

# The operations that will occur when buttons are pressed

def button_click(number):
    # When button clicked takes current num and adds clicked num
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))

def button_clear():
    screen.delete(0, END)

def button_add():
    first_number = screen.get()
    global f_num
    global math
    math = "addition" # Variable used to indicate what operation is happening
    f_num = float(first_number)
    screen.delete(0, END)
    
def button_subtract():
    first_number = screen.get()
    global f_num
    global math
    math = "subtraction" # Variable used to indicate what operation is happening
    f_num = float(first_number)
    screen.delete(0, END)
       
def button_multiply():
    first_number = screen.get()
    global f_num
    global math
    math = "multiplication" # Variable used to indicate what operation is happening
    f_num = float(first_number)
    screen.delete(0, END)

def button_divide():   
    first_number = screen.get()
    global f_num
    global math
    math = "division" # Variable used to indicate what operation is happening
    f_num = float(first_number)
    screen.delete(0, END)

def button_square():
    first_number = int(screen.get())
    screen.delete(0, END)
    global answer
    answer = first_number * first_number
    screen.insert(0, answer)

def button_root():
    first_number = int(screen.get())
    screen.delete(0, END)
    global answer
    answer = first_number ** 1/2
    screen.insert(0, answer)

def button_percent():
    global percent
    percent = True

def button_equal():
    second_number = float(screen.get())
    screen.delete(0, END)

    global answer

    if percent == True:
        if math == "addition":
            second_number = (f_num*second_number)/100
            answer = f_num + second_number
            screen.insert(0, answer)
        elif math == "subtraction":
            second_number = (f_num*second_number)/100
            answer = f_num - second_number
            screen.insert(0, answer)
    else:
        if math == "addition":
            answer = f_num + second_number
            screen.insert(0, answer)
        elif math == "subtraction":
            answer = f_num - second_number
            screen.insert(0, answer)
        elif math == "division":
            answer = f_num / second_number
            screen.insert(0, answer)
        elif math == "multiplication":
            answer = f_num * second_number
            screen.insert(0, answer)

def button_ans():
    screen.insert(0, answer)


# Define the buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)) 
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39.1, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=90, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="x", padx=41, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

button_ans = Button(root, text="ANS", padx=32, pady=20, command=button_ans)
button_square = Button(root, text="x²", padx=38, pady=20, command=button_square)
button_root = Button(root, text="√", padx=40, pady=20, command=button_root)
button_percent = Button(root, text="%", padx=39, pady=20, command=button_percent)

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_ans.grid(row=7, column=2)
button_square.grid(row=7 , column=0)
button_root.grid(row=7 , column=1)
button_percent.grid(row=8 , column=2)



root.mainloop()