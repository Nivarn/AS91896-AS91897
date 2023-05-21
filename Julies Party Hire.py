import tkinter as tk

#Main Window
window = tk.Tk() 
window.title("Julie's Party Hire")

#Main Frame
frame = tk.Frame(window) 
frame.pack()

#label frame within the Frame
julies_party_hire_frame = tk.LabelFrame(frame, text = "JULIE'S PARTY HIRE", width = 900, height = 900)
julies_party_hire_frame.pack(padx=10, pady=10)

#Creating the Entry Boxes
customer_name_entry = tk.Entry(julies_party_hire_frame)
customer_name_entry.grid(column=1,row=0)
receipt_number_entry = tk.Entry(julies_party_hire_frame)
receipt_number_entry.grid(column=1, row=1)
item_hire_entry = tk.Entry(julies_party_hire_frame)
item_hire_entry.grid(column=1,row=2)
no_item_spinbox = tk.Spinbox(julies_party_hire_frame, from_=1, to=500)
no_item_spinbox.grid(column=1, row=3)

#Creating Entry Box labels
customer_name_entry_label = tk.Label(julies_party_hire_frame, text="Customer Name: ")
customer_name_entry_label.grid(column=0,row=0)
receipt_number_entry_label = tk.Label(julies_party_hire_frame, text="Receipt Number  (12 Digits): ")
receipt_number_entry_label.grid(column=0, row=1)
item_hire_label= tk.Label(julies_party_hire_frame, text="Item for Hire: ")
item_hire_label.grid(column=0, row=2)
no_item_label = tk.Label(julies_party_hire_frame, text="Number of Item Being Hired: ")
no_item_label.grid(column=0, row=3)

#Spacing the widgets out
for widget in julies_party_hire_frame.winfo_children():
    widget.grid_configure(pady=5, padx=10)

window.mainloop()