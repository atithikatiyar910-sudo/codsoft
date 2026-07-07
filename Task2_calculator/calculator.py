from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Simple Calculator")
window.geometry("350x350")
window.configure(bg="lightgreen")

def calculate():

    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
            result = num1 / num2

        else:
            messagebox.showwarning("Warning", "Select an operation.")
            return

        result_label.config(text="Result = " + str(result))

    except:
        messagebox.showerror("Error", "Enter valid numbers.")

title = Label(window,
              text="Simple Calculator",
              font=("Arial",20,"bold"),
              bg="lightblue")
title.pack(pady=10)

Label(window,text="First Number",bg="white").pack()

entry1 = Entry(window,font=("Arial",12))
entry1.pack()

Label(window,text="Second Number",bg="white").pack()

entry2 = Entry(window,font=("Arial",12))
entry2.pack()

operation_var = StringVar()
operation_var.set("+")

OptionMenu(
    window,
    operation_var,
    "+",
    "-",
    "*",
    "/"
).pack(pady=10)

Button(
    window,
    text="Calculate",
    command=calculate,
    width=15
).pack()

result_label = Label(
    window,
    text="Result = ",
    font=("Arial",14),
    bg="white"
)

result_label.pack(pady=20)

window.mainloop()