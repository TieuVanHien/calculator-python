import tkinter as tk

window = tk.Tk()
window.geometry("600x500")

# create label and entry for task name
label_task = tk.Label(master=window, text="Task:", width=20)
label_task.grid(row=0, column=0)

entry_task = tk.Entry(master=window, width=50)
entry_task.grid(row=0, column=1, sticky=tk.W)
entry_task.focus()

tasks = []
completed_tasks = []

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)  # Add the task to the list
        entry_task.delete(0, tk.END)  # Clear the entry widget
        update_task_frame()  # Update the task frame

# Create a created task frame
frame1 = tk.LabelFrame(window, bg="white", width=100)
frame1.grid(row=2, column=0, padx=10, sticky="nwe")

# Create completed task frame
frame2 = tk.LabelFrame(window, bg="white", width=100)
frame2.grid(row=2, column=1, padx=10, sticky="nwe")
frame2.configure(bg="white")

# label for created tasks
label_created_task = tk.Label(master=window, text="Task Created")
label_created_task.grid(row=1, column=0)

todo_task = tk.Label(frame1, bg="white", text="", width=50)
todo_task.grid(row=0, column=0)

# Label for completed tasks
label_completed = tk.Label(master=window, text="Completed Tasks")
label_completed.grid(row=1, column=1)

completed_task = tk.Label(frame2, bg="white",text="", width=60)
completed_task.grid(row=0, column=0)

# button
button = tk.Button(
    text="Add Task",
    width=10,
    height=2,
    command=add_task
)
button.grid(row=0, column=2, padx=10)

# Delete function
def delete_task(index):
    if index < len(tasks):
        del tasks[index]  # Remove the task from the list 
        update_task_frame()  # Update the task frame

# Complete task function
def completed_taks(index):
    task = tasks.pop(index)
    completed_tasks.append(task)
    update_task_frame()


def update_task_frame():
    for widget in frame1.winfo_children():
        widget.destroy()
    for i, task in enumerate(tasks):
        task_label = tk.Label(master=frame1, text=task)
        task_label.grid(row=i, column=0, sticky="w")
        delete_button = tk.Button(
            master=frame1,
            text="Delete",
            command=lambda index=i: delete_task(index)
        )
        delete_button.grid(row=i, column=1, padx=5)
        complete_button = tk.Button( 
            master=frame1,
            text="Complete",
            command=lambda index=i: completed_taks(index)
        )
        complete_button.grid(row=i, column=2, padx=5)
    
    for widget in frame2.winfo_children():
        widget.destroy()
     # Update completed tasks frame
    for i, task in enumerate(completed_tasks):
        task_label = tk.Label(master=frame2, text=task)
        task_label.grid(row=i, column=0, sticky="w")
        # delete_button = tk.Button(
        #     master=frame2,
        #     text="Delete",
        #     command=lambda index=i: delete_completed_task(index)
        # )
        # delete_button.grid(row=i, column=1, padx=5)    


update_task_frame()    
window.mainloop()
