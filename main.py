import tkinter as tk
import json

root = tk.Tk()
root.title("Test")

transactions_history = {}

def save_json(data):
    data_dict

def add_transactions():
    global listbox, sender_input, reciever_input, amount_input
    transactions_history["Transactions"] = [sender_input.get(), reciever_input.get(), amount_input.get()]

    listbox.insert(tk.END, f"{sender_input.get()} to {reciever_input.get()}, {amount_input.get()} Lunks")



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
del_btn = tk.Button(btn_frame, text="Delete ")
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