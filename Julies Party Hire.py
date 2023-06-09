import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


#Empty list for customer information storage
julies_party_hire_customers = []

#Creating constants incase the user bypasses the limits
min_item_no = 1
max_item_no = 500

#Creating a command that can take information from the entry boxes and store it.
def customer_information():
    name = customer_name_entry.get()
    receipt_no = receipt_number_entry.get()
    item = item_hire_entry.get()
    no_of_item = no_item_spinbox.get()

    # This part of the code checks if the no_of_item spin box has a correct value of an
    if not no_of_item.isdigit():
        messagebox.showwarning(title='Error!', message='Invalid value for Number of Items.')
        return

    no_of_item = int(no_of_item)

    if no_of_item > max_item_no:
        messagebox.showwarning(title='Error!', message='Too many Items!')
    elif no_of_item < min_item_no:
        messagebox.showwarning(title='Error!', message='Invalid Number!')
    else:
        print("Number of Item being Hired (converted):", no_of_item)

    
    print("Full Name of Customer: ", name)
    print("Reciept Number: ", receipt_no)
    print("Item being Hired: ", item)
    print("Number of Item being Hired", no_of_item)

    #formatting the lists
    appendlist = [name, receipt_no, item, no_of_item]
    julies_party_hire_customers.append(appendlist)

    #ERROR CODE
    if name  == "":
        messagebox.showwarning(title='Error!', message='Customer Name has not been entered.')
    elif name.isalpha() == False:
        messagebox.showwarning(title='Error!', message='Please Enter Only Alphabetical Characters')
    elif receipt_no == "":
        messagebox.showwarning(title='Error!', message='Receipt Number has not been entered.')
    elif receipt_no.isnumeric() == False:
        messagebox.showwarning(title='Error!', message= 'Receipt Number Invalid!')
    elif item == "":
        messagebox.showwarning(title='Error!', message='Item for Hire has not been entered.')
    elif no_of_item > max_item_no:
        messagebox.showwarning(title='Error!', message='Too many Items!')
    elif no_of_item < min_item_no:
        messagebox.showwarning(title='Error!', message='Invalid Number!')
    else:
        messagebox.showinfo(title='Stored!', message='Customer information has been stored!')
        table.insert( parent='', index =tk.END,values =appendlist)
        customer_name_entry.delete(0, tk.END)
        receipt_number_entry.delete(0, tk.END)
        item_hire_entry.delete(0, tk.END)
        no_item_spinbox.delete(0, tk.END)
        
        
#TKINTER GUI

#Main Window
window = tk.Tk() 
window.title("Julie's Party Hire")

#Main Frame
frame = tk.Frame(window) 
frame.pack()

#label frame within the Frame
julies_party_hire_frame = tk.LabelFrame(frame, text = "JULIE'S PARTY HIRE", width = 900, height = 900)
julies_party_hire_frame.pack(padx=10, pady=10)

#Creating the Entry Boxes / Spin Boxes / Combo Boxes
customer_name_entry = tk.Entry(julies_party_hire_frame)
customer_name_entry.grid(column=1,row=0)
receipt_number_entry = tk.Entry(julies_party_hire_frame)
receipt_number_entry.grid(column=1, row=1)
item_hire_entry = ttk.Combobox(julies_party_hire_frame, values=["Balloons", "Food Warmers", "Tables", "Chairs", "Table Liners", "Speakers", "LED Lights" ], state='readonly')
item_hire_entry.grid(column=1,row=2)
no_item_spinbox = tk.Spinbox(julies_party_hire_frame, from_=1, to=500)
no_item_spinbox.grid(column=1, row=3)

#Creating Entry Box labels
customer_name_entry_label = tk.Label(julies_party_hire_frame, text="Customer Name: ")
customer_name_entry_label.grid(column=0,row=0)
receipt_number_entry_label = tk.Label(julies_party_hire_frame, text="Receipt Number: ")
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

#Making the table
table = ttk.Treeview(window, columns=('name', 'receipt number', 'item', 'no of item'), show="headings")
table.heading('name', text = 'Customer Name')
table.heading('receipt number', text = 'Receipt Number')
table.heading('item', text = 'Item')
table.heading('no of item', text = 'Number of Item')
table.pack()

#Code for Delete Button
def delete_selected_rows():
    for i in table.selection():
        table.delete(i)
        messagebox.showinfo(title='Deleted!', message='Customer Information deleted.')

#Delete button
delete_button = tk.Button(frame, text="Delete Selected Row", command=delete_selected_rows)
delete_button.pack(padx=20, pady=20)



window.mainloop()


