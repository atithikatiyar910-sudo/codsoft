from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("My To-Do List")
window.geometry("400x500")
window.configure(bg="lightpink")

tasks = []

def add_task():
    task = task_entry.get()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
    else:
        tasks.append(task)
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Select a task first.")

def clear_tasks():
    answer = messagebox.askyesno("Confirmation","Delete all tasks?")

    if answer:
        task_listbox.delete(0, END)
        tasks.clear()

title = Label(
    window,
    text="My To-Do List",
    font=("Arial",20,"bold"),
    bg="lightblue"
)

title.pack(pady=10)

task_entry = Entry(
    window,
    width=30,
    font=("Arial",14)
)

task_entry.pack(pady=10)

add_button = Button(
    window,
    text="Add Task",
    command=add_task,
    width=15
)

add_button.pack(pady=5)

task_listbox = Listbox(
    window,
    width=35,
    height=12,
    font=("Arial",12)
)

task_listbox.pack(pady=10)

delete_button = Button(
    window,
    text="Delete Selected",
    command=delete_task,
    width=15
)

delete_button.pack(pady=5)

clear_button = Button(
    window,
    text="Clear All",
    command=clear_tasks,
    width=15
)

clear_button.pack(pady=5)

window.mainloop()