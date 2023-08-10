import tkinter as tk
from tkinter import messagebox

# For add a new task to the list
def add_task():
    task_text = task_entry.get()
    if task_text:
        todo_list.insert(tk.END, task_text)
        task_entry.delete(0, tk.END)

# Foe edit the selected task
def edit_task():
    try:
        selected_task_index = todo_list.curselection()[0]
        edited_task_text = task_entry.get()
        if edited_task_text:
            todo_list.delete(selected_task_index)
            todo_list.insert(selected_task_index, edited_task_text)
            task_entry.delete(0, tk.END)
    except IndexError:
        pass

# For delete the task
def delete_task():
    try:
        selected_task_index = todo_list.curselection()[0]
        todo_list.delete(selected_task_index)
    except IndexError:
        pass

app = tk.Tk()
app.title("To-Do List Application")

# For background colour
app.configure(bg="#f0f0f0")

task_entry = tk.Entry(app, width=50, bg="white", fg="black")
task_entry.grid(row=0, column=0, padx=10, pady=10)

todo_list = tk.Listbox(app, width=50, height=15, bg="white", fg="black")
todo_list.grid(row=1, column=0, padx=10, pady=10)

# For "Add" button
add_button = tk.Button(app, text="Add Task", command=add_task, bg="green", fg="white")
add_button.grid(row=2, column=0, padx=10, pady=5)

# For "Edit" button
edit_button = tk.Button(app, text="Edit Task", command=edit_task, bg="orange", fg="white")
edit_button.grid(row=3, column=0, padx=10, pady=5)

# For "Delete" button
delete_button = tk.Button(app, text="Delete Task", command=delete_task, bg="red", fg="white")
delete_button.grid(row=4, column=0, padx=10, pady=5)

# Start event loop
app.mainloop()
