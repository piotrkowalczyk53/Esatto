from tkinter import Tk
from GUI import CustomerManagerGUI

if __name__ == "__main__":
    root = Tk()
    root.option_add('*Dialog.msg.bell', False)
    root.option_add('*Dialog.msg.no', '<Return>')
    root.title("Customer Manager")

    app = CustomerManagerGUI(root)

    root.mainloop()