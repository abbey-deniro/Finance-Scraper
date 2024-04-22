import tkinter as tk
import tkinter.messagebox
from tkinter import *
import final
import json

root = Tk()
root.geometry('500x500')
append_data_list = []

def googleFin():

    title = Label(root, text="Market Trends")
    title.pack()
    div1_totals = final.getDiv1()
    div1 = Message(root, text=div1_totals, width=800)
    div1.pack()
    div2_totals = final.getDiv2()
    div2 = Message(root, text=div2_totals, width=800)
    div2.pack()
    div3_totals = final.getDiv3()
    div3 = Message(root, text=div3_totals, width=800)
    div3.pack()
    div4_totals = final.getDiv4()
    div4 = Message(root, text=div4_totals, width=800)
    div4.pack()
    div5_totals = final.getDiv5()
    div5 = Message(root, text=div5_totals, width=800)
    div5.pack()
def toDoList():
    def add_task():
        tsk = entry_tasks.get()
        if tsk != '':
            listbox_tasks.insert(tk.END, tsk)
            entry_tasks.delete(0, tk.END)
            append_data_list.append("added: " + str(tsk))
            print(append_data_list)
            with open('append_data.json', 'w') as file:
                json.dump(str(append_data_list), file)
                file.close()
        else:
            tk.messagebox.showwarning(message='You must enter a task! try again.')

    def del_task():
        try:
            tsk_i = listbox_tasks.curselection()[0]
            listbox_tasks.delete(tsk_i)
        except:
            tk.messagebox.showwarning(message='You must select a task! try again.')

    title = Label(root, text='TO-DO List')
    title.pack()
    listbox_tasks = tk.Listbox(root, height=5, width=35)
    listbox_tasks.pack()
    entry_tasks = tk.Entry(root, width=35)
    entry_tasks.pack()
    add_button = tk.Button(root, text="Add", width=30, comman=add_task)
    add_button.pack()
    del_button = tk.Button(root, text="Delete", width=30, comman=del_task)
    del_button.pack()


main_title = Label(root, text="Welcome! Click a button to choose your app to run!", font=('Ariel', 12)).pack()

gf_button = tk.Button(root, text='Google Finance Trends', width=25, font=('Ariel', 8), command=googleFin).pack()

to_do_list_button = tk.Button(root, text='To-Do List', width=25, font=('Ariel', 8), command=toDoList).pack()

root.mainloop()

