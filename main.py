import tkinter as tk
from tkinter import messagebox 
import json

root = tk.Tk()
root.title("Test")

transactions_history = {}
transactions = []

def load_transactions():
    with open("history.json", "r") as file:
        transaction_history = json.load(file)
    
    for key, values in transactions_history:
        transactions.append(values)

load_transactions()

def set_listbox():
    global listbox

    listbox.delete(0, tk.END)

    for item in transactions:
        listbox.insert(tk.END, f"{item[0]} to {item[1]}, {item[2]} Lunks")

set_listbox()

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

# Entries and Label
input_frame = tk.Frame(root)
input_frame.pack()

# Sender
sender_label = tk.Label(input_frame, text="Sender: ")
sender_label.grid(row=0, column=0, sticky="W")
sender_var = tk.StringVar()
sender_input = tk.Entry(input_frame, textvariable=sender_var)
sender_input.grid(row=0, column=1, sticky="W")

# Reciever
reciever_label = tk.Label(input_frame, text="Reciever: ")
reciever_label.grid(row=1, column=0, sticky="W")
reciever_var = tk.StringVar()
reciever_input = tk.Entry(input_frame, textvariable=reciever_var)
reciever_input.grid(row=1, column=1, sticky="W")

# Amounr
amount_label = tk.Label(input_frame, text="Amount: ")
amount_label.grid(row=2, column=0, sticky="S")
amount_var = tk.StringVar()
amount_input = tk.Entry(input_frame, textvariable=amount_var)
amount_input.grid(row=2, column=1, sticky="S")

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()
add_btn= tk.Button(btn_frame, text=" Add    ", command=add_transactions)
update_btn = tk.Button(btn_frame, text="Update ")
del_btn = tk.Button(btn_frame, text="Delete ", command=delete_transaction)
load_btn = tk.Button(btn_frame, text="Load   ")
refresh_btn = tk.Button(btn_frame, text="Refresh")
add_btn.pack(side=tk.LEFT)
update_btn.pack(side=tk.LEFT)
del_btn.pack(side=tk.LEFT)
load_btn.pack(side=tk.LEFT)
refresh_btn.pack(side=tk.LEFT)

# Listbox
data_frame = tk.Frame(root)
data_frame.pack()
listbox = tk.Listbox(data_frame, height=8, width=40)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

root.mainloop()