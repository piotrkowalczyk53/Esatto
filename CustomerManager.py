import datetime

# A class that represents a customer
class Customer:
    # Constructor takes current date as date of object creation
    def __init__(self, name, vat_id, address):
        self.name = name
        self.vat_id = vat_id
        self.creation_date = datetime.date.today()
        self.address = address  


# A class that impleents temp database
class CustomerDatabase:
    def __init__(self):
        self.customers = []

    def add_customer(self, name, vat_id, address):
        customer = Customer(name, vat_id, address)
        self.customers.append(customer)

    def edit_customer(self, index, name=None, vat_id=None, address=None):
        customer = self.customers[index]
        if name is not None:
            customer.name = name
        if vat_id is not None:
            customer.vat_id = vat_id
        if address is not None:
            customer.address = address

    def delete_customer(self, index):
        del self.customers[index]

    def get_customer(self, index):
        return self.customers[index]


# A class that represents address of a customer
class Address:
    def __init__(self, street, city, postal_code, country):
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.country = country

    # Usefull for printing customer info in GUI
    def __str__(self):
        return f"{self.street}, {self.postal_code} {self.city}, {self.country}"

    
if __name__ == "__main__":
    pass