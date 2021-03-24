import tkinter as tk
from tkinter import messagebox 
import json

# Constants
FONT_NAME = "Open Sans"

root = tk.Tk()
root.title("Money Tracker")

transactions_history = {}
transactions = []

def set_listbox():
    """Refreshes the listbox"""
    
    global listbox

    listbox.delete(0, tk.END)

    for item in transactions:
        listbox.insert(tk.END, f"{item[0]} to {item[1]}, ${item[2]}, {item[3]}")

def save_json(data):
    """Saves the date to history.json file"""
    
    with open("history.json", "w") as file:
        json.dump(transactions_history, file, indent=4)

def check_fields():
    if sender_input.get() == "" or reciever_input.get() == "" or desc_input.get("1.0", tk.END) == "":
        return False
    return True

def clear_fields():
    sender_input.delete(0, tk.END)
    reciever_input.delete(0, tk.END)
    amount_input.delete(0, tk.END)
    desc_input.delete("1.0", tk.END)

def add_transactions():
    """Adds transactios to the listbox"""
    
    try:
        check_int = int(amount_input.get())
    except ValueError:
        messagebox.showwarning(title="❌ Error ❌", message="Please enter only numbers in amount field")
        return

    if check_fields():
        transactions.append([sender_input.get(), reciever_input.get(), amount_input.get(), desc_input.get("1.0", tk.END)])
        transactions_history["Transactions"] = transactions

        clear_fields()

        save_json(transactions_history)
        set_listbox()
    else:
        messagebox.showwarning(title="❌ Error ❌", message="Please do not leave any fields empty")

def delete_transaction():
    """Deletes transactions from the listbox"""    
    
    try:
        del transactions[listbox.curselection()[0]]
    except IndexError:
        messagebox.showwarning(title="❌ Error ❌", message="Please select any item")
    else:
        transactions_history["Transactions"] = transactions

        save_json(transactions_history)
        set_listbox()

def load_transactions():
    """Loads data of transactions from the selected item in the listbox"""

    try:
        selected_idx = listbox.curselection()[0]
        selected_item = transactions[selected_idx]
    except IndexError:
        messagebox.showwarning(title="❌ Error ❌", message="Please select any item")
    else:
        sender_var.set(selected_item[0])
        reciever_var.set(selected_item[1])
        amount_var.set(selected_item[2])
        desc_input.delete("1.0", tk.END)
        desc_input.insert(tk.END, selected_item[3])

def update_transactions():
    """Updates selected transaction to the details newly entered"""
    
    if check_fields():
        try:
            transactions[listbox.curselection()[0]] = [sender_var.get(), reciever_var.get(), amount_var.get(), desc_input.get("1.0", tk.END)]   
        except IndexError:
            messagebox.showwarning(title="❌ Error ❌", message="Please select any item")
        else:
            transactions_history["Transactions"] = transactions 

            save_json(transactions_history)
            set_listbox()
    else:
        messagebox.showwarning(title="❌ Error ❌", message="Please do not leave any fields empty")    


# Title
title = tk.Label(root, text="Money Tracker", font=(FONT_NAME, 15, "normal"))
title.grid(row=0, column=0, columnspan=2, pady=3)

# ---------------------------- ENTRIES AND LABELS ------------------------------- #
input_frame = tk.Frame(root)
input_frame.grid(row=1, column=0, pady=3)

# Sender
sender_label = tk.Label(input_frame, text="Sender: ", font=(FONT_NAME, 12, "normal"))
sender_label.grid(row=0, column=0, sticky="W")
sender_var = tk.StringVar()
sender_input = tk.Entry(input_frame, textvariable=sender_var, width=36, font=(FONT_NAME, 12, "normal"))
sender_input.focus()
sender_input.grid(row=0, column=1, sticky="W", pady=2)

# Reciever
reciever_label = tk.Label(input_frame, text="Reciever: ",  font=(FONT_NAME, 12, "normal"))
reciever_label.grid(row=1, column=0, sticky="W")
reciever_var = tk.StringVar()
reciever_input = tk.Entry(input_frame, textvariable=reciever_var, width=36, font=(FONT_NAME, 12, "normal"))
reciever_input.grid(row=1, column=1, sticky="W", pady=2)

# Amount
amount_label = tk.Label(input_frame, text="Amount: ", font=(FONT_NAME, 12, "normal"))
amount_label.grid(row=2, column=0, sticky="W")
amount_var = tk.StringVar()
amount_input = tk.Entry(input_frame, textvariable=amount_var, width=36, font=(FONT_NAME, 12, "normal"))
amount_input.grid(row=2, column=1, sticky="W", pady=2)

# Description
desc_label = tk.Label(input_frame, text="Description: ", font=(FONT_NAME, 12, "normal"))
desc_label.grid(row=3, column=0, sticky="N")
desc_input = tk.Text(input_frame, width=36, height=8, font=(FONT_NAME, 12, "normal"))
desc_input.grid(row=3, column=1, sticky="W", pady=2)

# ---------------------------- BUTTONS ------------------------------- #
btn_frame = tk.Frame(root)
btn_frame.grid(row=2, column=0)

# Add
add_btn= tk.Button(btn_frame, text="    Add    ", command=add_transactions, font=(FONT_NAME, 11, "normal"))
add_btn.pack(side=tk.LEFT, padx=3, pady=2)

# Update
update_btn = tk.Button(btn_frame, text="  Update  ", command=update_transactions, font=(FONT_NAME, 11, "normal"))
update_btn.pack(side=tk.LEFT, padx=3, pady=2)

# Delete
del_btn = tk.Button(btn_frame, text="  Delete  ", command=delete_transaction, font=(FONT_NAME, 11, "normal"))
del_btn.pack(side=tk.LEFT, padx=3, pady=2)

# Load
load_btn = tk.Button(btn_frame, text="   Load   ", command=load_transactions, font=(FONT_NAME, 11, "normal"))
load_btn.pack(side=tk.LEFT, padx=3, pady=2)

# Refresh
refresh_btn = tk.Button(btn_frame, text="  Refresh  ", command=set_listbox, font=(FONT_NAME, 11, "normal"))
refresh_btn.pack(side=tk.LEFT, padx=3, pady=2)

# ---------------------------- LISTBOX ------------------------------- #
data_frame = tk.Frame(root)
data_frame.grid(row=1, column=1, rowspan=2)

# Scroll Bars
scroll_bar_y = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
scroll_bar_x = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)

# Listbox
listbox = tk.Listbox(data_frame, height=13, width=45, yscrollcommand=scroll_bar_y.set, xscrollcommand=scroll_bar_x.set, font=(FONT_NAME, 12, "normal"))

# Scroll Bars
scroll_bar_y.config(command=listbox.yview)
scroll_bar_y.pack(side=tk.RIGHT, fill=tk.Y)
scroll_bar_x.config(command=listbox.xview)
scroll_bar_x.pack(side=tk.BOTTOM, fill=tk.X)

listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, pady=2)

# ---------------------------- STATUS BAR ------------------------------- #
status_frame = tk.LabelFrame(root, bd=1, relief=tk.SUNKEN)
status_frame.grid(padx=2, pady=2, sticky=tk.N+tk.S+tk.E+tk.W, columnspan=2)

# Made By
made_by = tk.Label(status_frame, text="Made By Arnav Ghatti", anchor=tk.E, font=(FONT_NAME, 9, "normal"))
made_by.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

# Version
version_label = tk.Label(status_frame, text="Version: 2.2.7", anchor=tk.W, font=(FONT_NAME, 9, "normal"))
version_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

def load_data():
    """Loads data from the history.json file to the listbox"""
    
    global transactions, listbox
    
    with open("history.json", "r") as file:
        transaction_history = json.load(file)

    transactions = transaction_history["Transactions"]
    listbox.delete(0, tk.END)

    for item in transactions:
        listbox.insert(tk.END, f"{item[0]} to {item[1]}, ${item[2]}, {item[3]}")

load_data()

root.mainloop()
