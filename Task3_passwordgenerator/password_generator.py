from tkinter import *
from tkinter import messagebox
import random
import string

window = Tk()
window.title("Password Generator")
window.geometry("400x300")
window.configure(bg="lightyellow")

def generate_password():

    length = length_entry.get()

    if length == "":
        messagebox.showwarning("Warning", "Please enter password length.")
        return

    try:
        length = int(length)

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(characters)

        result_label.config(text=password)

    except:
        messagebox.showerror("Error", "Enter a valid number.")

title = Label(
    window,
    text="Password Generator",
    font=("Arial",18,"bold"),
    bg="lightyellow"
)

title.pack(pady=10)

Label(
    window,
    text="Password Length",
    bg="lightyellow"
).pack()

length_entry = Entry(
    window,
    width=20,
    font=("Arial",12)
)

length_entry.pack(pady=10)

Button(
    window,
    text="Generate Password",
    command=generate_password,
    width=18
).pack()

result_label = Label(
    window,
    text="",
    font=("Arial",12),
    bg="lightyellow",
    wraplength=350
)

result_label.pack(pady=20)

window.mainloop()
