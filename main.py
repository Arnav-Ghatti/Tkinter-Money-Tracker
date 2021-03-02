import tkinter as tk
from tkinter import messagebox 
import json

root = tk.Tk()
root.title("Test")

transactions_history = {}
transactions = []

def set_listbox():
    global listbox

    listbox.delete(0, tk.END)

    for item in transactions:
        listbox.insert(tk.END, f"{} | {item[0]} to {item[1]}, {item[2]} Lunks")

def save_json(data):
    with open("history.json", "w") as file:
        json.dump(transactions_history, file, indent=4)

def add_transactions():
    global listbox, sender_input, reciever_input, amount_input
    
    transactions.append([sender_input.get(), reciever_input.get(), amount_input.get()])
    transactions_history["Transactions"] = transactions

    save_json(transactions_history)

    set_listbox()

def delete_transaction():
    try:
        del transactions[listbox.curselection()[0]]
    except IndexError:
        messagebox.showerror("showerror", "No item selected")

    save_json(transactions_history)

    set_listbox()

def load_transactions():
    global sender_var, reciever_var, amount_var, sender_input, reciever_input, amount_input
    
    try:
        selected_idx = listbox.curselection()[0]
        selected_item = transactions[selected_idx]

        sender_var.set(selected_item[0])
        reciever_var.set(selected_item[1])
        amount_var.set(selected_item[2])
    
    except IndexError:
        messagebox.showerror("showerror", "No item selected")

def update_transactions():
    
    transactions[listbox.curselection()[0]] = [sender_var.get(), reciever_var.get(), amount_var.get()]
    save_json()
    
    set_listbox()

# Entries and Label
input_frame = tk.Frame(root)
input_frame.pack()

# Sender
sender_label = tk.Label(input_frame, text="Sender: ")
sender_label.grid(row=0, column=0, sticky="W")
sender_var = tk.StringVar()
sender_input = tk.Entry(input_frame, textvariable=sender_var, width=33)
sender_input.grid(row=0, column=1, sticky="W", pady=2)

# Reciever
reciever_label = tk.Label(input_frame, text="Reciever: ")
reciever_label.grid(row=1, column=0, sticky="W")
reciever_var = tk.StringVar()
reciever_input = tk.Entry(input_frame, textvariable=reciever_var, width=33)
reciever_input.grid(row=1, column=1, sticky="W", pady=2)

# Amounr
amount_label = tk.Label(input_frame, text="Amount: ")
amount_label.grid(row=2, column=0, sticky="W")
amount_var = tk.StringVar()
amount_input = tk.Entry(input_frame, textvariable=amount_var, width=33)
amount_input.grid(row=2, column=1, sticky="W", pady=2)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()
add_btn= tk.Button(btn_frame, text=" Add    ", command=add_transactions)
update_btn = tk.Button(btn_frame, text="Update ", command=update_transactions)
del_btn = tk.Button(btn_frame, text="Delete ", command=delete_transaction)
load_btn = tk.Button(btn_frame, text="Load   ", command=load_transactions)
refresh_btn = tk.Button(btn_frame, text="Refresh", command=set_listbox)
add_btn.pack(side=tk.LEFT, padx=2, pady=2)
update_btn.pack(side=tk.LEFT, padx=2, pady=2)
del_btn.pack(side=tk.LEFT, padx=2, pady=2)
load_btn.pack(side=tk.LEFT, padx=2, pady=2)
refresh_btn.pack(side=tk.LEFT, padx=2, pady=2)

# Listbox
data_frame = tk.Frame(root)
data_frame.pack()
scroll_bar = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
listbox = tk.Listbox(data_frame, height=8, width=45, yscrollcommand=scroll_bar.set)
scroll_bar.config(command=listbox.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, pady=2)

def load_data():
    global transactions, listbox
    
    with open("history.json", "r") as file:
        transaction_history = json.load(file)

    transactions = transaction_history["Transactions"]
    listbox.delete(0, tk.END)

    for item in transactions:
        listbox.insert(tk.END, f"{item[0]} to {item[1]}, {item[2]} Lunks")

load_data()

root.mainloop()