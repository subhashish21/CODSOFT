import tkinter
import pickle
import tkinter.messagebox
window = tkinter.Tk()
window.title("Todos List")

def add_task():
    todo = task_add.get()
    if todo!= " ":
        todo_list.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="task is empty ", message="hey pls add a task")
def remove_task():
        try:
            index_todo = todo_list.curselection()
            todo_list.delete(index_todo[0])
        
        except:
            tkinter.messagebox.showwarning(title="Attention !!", message="to delete a task you must select")

def task_refresh():
    try:
        todo_task = pickle.load(open("tasks.dat","rb"))
        task.delete(0,tkinter,)
        for todo in task:
            task.inset(tkinter.END,todo)
    
    except:
        tkinter.messagebox.showwarning(title="Attention !!",message="cannot find task.dat")
    

task = tkinter.Frame(window)
task.pack()
todo_list = tkinter.Listbox(task,height=20, width=40)
todo_list.pack(side=tkinter.LEFT)
scroll = tkinter.Scrollbar(task)
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
todo_list.config(yscrollcommand = scroll.set)

task_add = tkinter.Entry(window,width=70)
task_add.pack()
task_add_button = tkinter.Button(window, text = "Add Task", font=("roboto",20,"normal"),background="blue",width=30,command=add_task)

task_add_button.pack()
task_delete_button = tkinter.Button(window, text = "Delete Task", font=("roboto",20,"normal"),background="red",width=30, command=remove_task)
task_delete_button.pack()
task_refresh_button = tkinter.Button(window, text = "Refresh Task", font=("roboto",20,"normal"),background="yellow",width=30,command=task_refresh)
task_refresh_button.pack()
window.mainloop()