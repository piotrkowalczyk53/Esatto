from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Import Address & Customer
from CustomerManager import *


class CustomerManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Customer Manager")

        # Create temp database and variables
        self.customer_db = CustomerDatabase()
        self.customer = None
        self.address = None

        # Create labels and input entries for an address
        self.customer_dropdown_label = Label(master, text="Select Customer:")
        self.customer_dropdown_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.customer_dropdown = ttk.Combobox(master, state="readonly", width=20)
        self.customer_dropdown.grid(row=0, column=1, padx=5, pady=5)
        self.customer_dropdown.bind("<<ComboboxSelected>>", self.populate_fields)
   
        self.update_customer_dropdown()

        self.address_label = Label(master, text="Address:")
        self.address_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.street_label = Label(master, text="Street:")
        self.street_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        self.street_entry = Entry(master)
        self.street_entry.grid(row=2, column=1, padx=5, pady=5)

        self.city_label = Label(master, text="City:")
        self.city_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.city_entry = Entry(master)
        self.city_entry.grid(row=3, column=1, padx=5, pady=5)

        self.postal_code_label = Label(master, text="Postal Code:")
        self.postal_code_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        self.postal_code_entry = Entry(master)
        self.postal_code_entry.grid(row=4, column=1, padx=5, pady=5)

        self.country_label = Label(master, text="Country:")
        self.country_label.grid(row=5, column=0, padx=5, pady=5, sticky=W)

        self.country_entry = Entry(master)
        self.country_entry.grid(row=5, column=1, padx=5, pady=5)

        # Create labels and input entries for the client data
        self.customer_label = Label(master, text="Customer:")
        self.customer_label.grid(row=6, column=0, padx=5, pady=5, sticky=W)

        self.name_label = Label(master, text="Name:")
        self.name_label.grid(row=7, column=0, padx=5, pady=5, sticky=W)

        self.name_entry = Entry(master)
        self.name_entry.grid(row=7, column=1, padx=5, pady=5)

        self.vat_id_label = Label(master, text="VAT ID:")
        self.vat_id_label.grid(row=8, column=0, padx=5, pady=5, sticky=W)

        self.vat_id_entry = Entry(master)
        self.vat_id_entry.grid(row=8, column=1, padx=5, pady=5)

        self.creation_date_label = Label(master, text="Creation Date:")
        self.creation_date_label.grid(row=9, column=0, padx=5, pady=5, sticky=W)

        self.creation_date_entry = Entry(master, state="readonly")
        self.creation_date_entry.grid(row=9, column=1, padx=5, pady=5)

        # Create buttons
        self.add_button = Button(master, text="Add Customer", command=self.add_customer)
        self.add_button.grid(row=10, column=0, padx=(10, 5), pady=5, sticky="EW")

        self.edit_button = Button(master, text="Edit Customer", command=self.edit_customer)
        self.edit_button.grid(row=10, column=1, padx=5, pady=5, sticky="EW")

        self.delete_button = Button(master, text="Delete Customer", command=self.delete_customer)
        self.delete_button.grid(row=10, column=2, padx=5, pady=5, sticky="EW")

        self.list_button = Button(master, text="List Customers", command=self.list_customers)
        self.list_button.grid(row=10, column=3, padx=5, pady=5, sticky="EW")

        self.list_button = Button(master, text="List Full Info", command=self.list_customers_full_info)
        self.list_button.grid(row=10, column=4, padx=(5, 10), pady=5, sticky="EW")

    def add_address(self):
        # Checking if all address data has been provided
        if not self.is_entry_empty(self.street_entry) and \
            not self.is_entry_empty(self.country_entry) and \
            not self.is_entry_empty(self.postal_code_entry) and \
            not self.is_entry_empty(self.city_entry):

            # Creating temp address variable
            self.address = Address(self.street_entry.get(),
                               self.city_entry.get(),
                               self.postal_code_entry.get(),
                               self.country_entry.get())
            
    # A function that adds a customer to the database
    def add_customer(self):
        # Creating Address of the customer
        self.add_address()

        # Checking if all data has been provided
        if not self.is_entry_empty(self.name_entry) and \
                not self.is_entry_empty(self.vat_id_entry) and \
                self.address is not None:

            # Getting the data and adding the customer to the database
            name = self.name_entry.get()
            vat_id = self.vat_id_entry.get()
            self.customer_db.add_customer(name, vat_id, self.address)

            # Clearing fileds and updating dropdown list
            self.clear_entries()
            self.update_customer_dropdown()

    # A function that allows to edit customer info
    def edit_customer(self):
        # Checking if the customer was selected - their data would be in the entries
        if not self.is_entry_empty(self.name_entry) and \
                not self.is_entry_empty(self.vat_id_entry):

            # Editing customer data in the database
            index = self.customer_db.customers.index(self.customer)
            name = self.name_entry.get()
            vat_id = self.vat_id_entry.get()
            address = self.address
            self.customer_db.edit_customer(index, name, vat_id, address)

            # Clearing fileds and updating dropdown list
            self.clear_entries()
            self.update_customer_dropdown()

            messagebox.showinfo("Customer Edited", "The customer has been successfully edited.")
        else:
            messagebox.showerror("Error", "No customer selected.")

    def delete_customer(self):
        # Checking if the customer was selected - their data would be in the entries
        if not self.is_entry_empty(self.name_entry) and \
                not self.is_entry_empty(self.vat_id_entry):
            
            # Deleting customer data form the database
            index = self.customer_db.customers.index(self.customer)
            self.customer_db.delete_customer(index)
            self.customer = None

            # Clearing fileds and updating dropdown list
            self.clear_entries()
            self.update_customer_dropdown()

            messagebox.showinfo("Customer Deleted", "The customer has been successfully deleted.")
        else:
            messagebox.showerror("Error", "No customer selected.")

    # A function that lists basic customer data
    def list_customers(self):
        message = ""
        for index, customer in enumerate(self.customer_db.customers):
            message += f"{index+1}: {customer.name} (VAT ID: {customer.vat_id})\n"
        messagebox.showinfo("Customer Information", message)

    # A function that lists basic customer data
    def list_customers_full_info(self):
        message = ""
        for index, customer in enumerate(self.customer_db.customers):
            message += f"{index+1}: {customer.name} (VAT ID: {customer.vat_id})\n"
            message += f"Address: {customer.address}\n"
            message += f"Creation Date: {customer.creation_date}\n\n"
        messagebox.showinfo("Customer Information", message)

    # A function that clears data in entries   
    def clear_entries(self):
        self.name_entry.delete(0, END)
        self.vat_id_entry.delete(0, END)
        self.street_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.postal_code_entry.delete(0, END)
        self.country_entry.delete(0, END)

    # A function that writes data to the entries 
    def populate_entries(self):
        self.name_entry.insert(0, self.customer.name)
        self.vat_id_entry.insert(0, self.customer.vat_id)
        self.creation_date_entry.insert(0, self.customer.creation_date)
        self.street_entry.insert(0, self.customer.address.street)
        self.city_entry.insert(0, self.customer.address.city)
        self.postal_code_entry.insert(0, self.customer.address.postal_code)
        self.country_entry.insert(0, self.customer.address.country)

    # A function that dynamically updates values in dropbox
    def update_customer_dropdown(self):
        customer_names = [""]
        customer_names += [str(index+1) + ": " + customer.name for index, customer in enumerate(self.customer_db.customers)]
        self.customer_dropdown["values"] = customer_names
        self.customer_dropdown.current(0)
        
        if len(self.customer_db.customers) > 0:
            max_width = max(len(name) for name in customer_names)
            if max_width > 20:
                self.customer_dropdown.config(width=max_width)           

    # A fucntion that automatically fills entries with the selected customer's data
    def populate_fields(self, event):
        self.clear_entries()
        customer_str = self.customer_dropdown.get()
        if customer_str:
            customer_index = int(customer_str.split(":")[0]) - 1
            self.customer = self.customer_db.get_customer(customer_index)
            self.populate_entries()

    # A function that checks if a entry is empty
    def is_entry_empty(self, entry):
        if entry.get() == "":
            return True
        else:
            return False
        
if __name__ == "__main__":
    pass