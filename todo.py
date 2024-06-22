import tkinter as tk
from datetime import datetime

def add_task():
    task = entry_task.get()
    if task:
        current_date = datetime.now().strftime("%Y-%m-%d")
        task_with_date = f"{task} ({current_date})"
        listbox_tasks.insert(tk.END, task_with_date)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        pass

def mark_as_done():
    try:
        index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(index)
        task_parts = task.split("(")
        task_done = task_parts[0].strip() + " (Done)"
        listbox_tasks.delete(index)
        listbox_tasks.insert(index, task_done)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50, fg="blue")  # Set text color to blue
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task, fg="green")  # Set button color to green
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task, fg="red")  # Set button color to red
button_delete_task.pack()

button_mark_done = tk.Button(root, text="Mark as Done", width=48, command=mark_as_done)
button_mark_done.pack()

root.mainloop()
