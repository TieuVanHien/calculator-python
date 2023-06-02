import tkinter as tk

window = tk.Tk()
window.geometry("600x500")

# Define the number of columns in the app
num_columns = 3

# Configure the columns
for i in range(num_columns):
    window.grid_columnconfigure(i, weight=1)

# create label and entry for task name
label_task = tk.Label(master=window, text="Task:")
label_task.grid(row=0, column=0)

entry_task = tk.Entry(master=window, width=50)
entry_task.grid(row=0, column=1, sticky=tk.W)
entry_task.focus()

tasks = []

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)  # Add the task to the list
        entry_task.delete(0, tk.END)  # Clear the entry widget
        update_task_label()

def update_task_label():
    todo_task.config(text="\n".join(tasks))
     
# label for created tasks
label_task = tk.Label(master=window, text="Task Created")
label_task.grid(row=1, column=1)

todo_task = tk.Label(master=window, text="", bg="white", width=30, )
todo_task.grid(row=2, column=1)

# button
button = tk.Button(
    text="Add Task",
    width=10,
    height=2,
    command=add_task
)
button.grid(row=0, column=2, padx=10)

window.mainloop()
