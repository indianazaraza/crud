from tkinter import Entry, Label

class Fields:
    def __init__(self, frame, id_entry, name_entry, surname_entry, address_entry, pass_entry):
        #generate all text fields of the application taking id_entry, name_entry, surname_entry, address_entry and pass_entry as variables
        #id_entry, name_entry, surname_entry, address_entry and pass_entry are stringvar type
        #frame is frame type
        #receive a frame, a id_entry, a name_entry, a surname_entry, a address_entry and a pass_entry as parameters
        self.frame = frame
        self.id_entry = id_entry
        self.name_entry = name_entry
        self.surname_entry = surname_entry
        self.address_entry = address_entry
        self.pass_entry = pass_entry

        #----------------------------field id-----------------------------
        Entry(self.frame, textvariable=self.id_entry).grid(column=1, row=0, pady=10, padx=10, columnspan=3)
        Label(self.frame, text="ID", bg="black", fg="#c4ff4d").grid(column=0, row=0, pady=10, padx=10, sticky="w")

        #----------------------------field name-----------------------------
        Entry(self.frame, textvariable=self.name_entry).grid(column=1, row=1, pady=10, padx=10, columnspan=3)
        Label(self.frame, text="Name", bg="black", fg="#c4ff4d").grid(column=0, row=1, pady=10, padx=10, sticky="w")

        #----------------------------field last name-----------------------------
        Entry(self.frame, textvariable=self.surname_entry).grid(column=1, row=2, pady=10, padx=10, columnspan=3)
        Label(self.frame, text="Surname", bg="black", fg="#c4ff4d").grid(column=0, row=2, pady=10, padx=10, sticky="w")

        #----------------------------field address-----------------------------
        Entry(self.frame, textvariable=self.address_entry).grid(column=1, row=3, pady=10, padx=10, columnspan=3)
        Label(self.frame, text="Address", bg="black", fg="#c4ff4d").grid(column=0, row=3, pady=10, padx=10, sticky="w")

        #----------------------------field password-----------------------------
        Entry(self.frame, textvariable=self.pass_entry, show="*").grid(column=1, row=4, pady=10, padx=10, columnspan=3)
        Label(self.frame, text="Password", bg="black", fg="#c4ff4d").grid(column=0, row=4, pady=10, padx=10, sticky="w")