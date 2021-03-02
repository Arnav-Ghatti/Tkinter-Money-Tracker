import tkinter as tk

root = tk.Tk()
root.title("Test")

title = tk.Label(root, text="Test Title")
title.grid(row=0, column=0, columnspan=5, pady=2)

# Entries and Labels
# Sender
sender_label = tk.Label(root, text="Sender: ")
sender_label.grid(row=1, column=0, columnspan=1, pady=2)
sender_input = tk.Entry(root, width=30, borderwidth=3)
sender_input.grid(row=1, column=1, pady=2)

# Reciever
reciever_label = tk.Label(root, text="Reciever: ")
reciever_label.grid(row=2, column=0, columnspan=1, pady=2)
reciever_input = tk.Entry(root, width=30, borderwidth=3)
reciever_input.grid(row=2, column=1, pady=2)

# Amount
amount_label = tk.Label(root, text="Amount: ")
amount_label.grid(row=3, column=0, columnspan=1, pady=2)
amount_input = tk.Entry(root, width=30, borderwidth=3)
amount_input.grid(row=3, column=1, pady=2)

# Search
search_input = tk.Entry(root, width=30, borderwidth=3)
search_input.grid(row=4, column=1, pady=2)
search_button = tk.Button(root, text="Search")
search_button.grid(row=4, column=0, pady=2)

# listbox = tk.Listbox(root)
# listbox.grid(row=5, column=0)

root.mainloop()