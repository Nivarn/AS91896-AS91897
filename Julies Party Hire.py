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

window.mainloop()