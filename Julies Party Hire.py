import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


#Empty list for customer information storage
julies_party_hire_customers = []

#Creating constants incase the user bypasses the limits
min_item_no = 1
max_item_no = 500

#Creating Constants for Valid Receipt Numbers
min_receipt_number = 100000000000
max_receipt_number = 999999999999

def customer_information():
    name = customer_name_entry.get()
    receipt_no = int(receipt_number_entry.get())
    item = item_hire_entry.get()
    no_of_item = int(no_item_spinbox.get())

    print("Full Name of Customer: ", name)
    print("Reciept Number: ", receipt_no)
    print("Item being Hired: ", item)
    print("Number of Item being Hired", no_of_item)



    
    appendlist = [name, receipt_no, item, no_of_item]
    julies_party_hire_customers.append(appendlist)
    #ERROR CODE
    if name  == "":
        messagebox.showwarning(title='Error!', message='Customer Name has not been entered.')
    elif receipt_no == "":
        messagebox.showwarning(title='Error!', message='Reciept Number has not been entered.')
    elif receipt_no > max_receipt_number:
        messagebox.showwarning(title='Error!', message='Invalid Receipt Number!')
    elif receipt_no < min_receipt_number:
        messagebox.showwarning(title = 'Error!', message='Invalid Receipt Number')
    elif item == "":
        messagebox.showwarning(title='Error!', message='Item for Hire has not been entered.')
    elif no_of_item > max_item_no:
        messagebox.showwarning(title='Error!', message='Too many Items!.')
    elif no_of_item < min_item_no:
        messagebox.showwarning(title='Error!', message='Invalid Number!')
    else:
        messagebox.showinfo(title='Stored!', message='Group information has been stored!')
        



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

#Done Button
done_button = tk.Button(frame, text="Store", command=customer_information)
done_button.pack(padx= 20, pady= 20)


#Spacing the widgets out
for widget in julies_party_hire_frame.winfo_children():
    widget.grid_configure(pady=5, padx=10)

window.mainloop()


