import tkinter as tk

root = tk.Tk()
root.title("Test")

title = tk.Label(root, text="Test Title")
title.grid(row=0, column=0, columnspan=5, pady=5, padx=5)

sender = tk.Label(root, text="Sender: ")
sender.grid(row=1, column=0)
sender_input

listbox = tk.Listbox(root)
listbox.grid(row=5, column=0)

root.mainloop()