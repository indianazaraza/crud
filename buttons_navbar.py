from tkinter import Label, StringVar, messagebox, Menu, Button
import tkinter.scrolledtext as scrolled_text
from fields import Fields
import mariadb

class Buttons_navbar:
	def __init__(self, root, frame, frame2):
		#generate buttons, nav-bar and database connection
		#receive a root and two frames as parameters
		self.root = root
		self. frame = frame
		self.frame2 = frame2

		messagebox.showwarning("Aviso", "SIEMPRE crea una base de datos antes de comenzar a operar. File->Create database")

		#variables assigned to inputs
		self.id_entry = StringVar()
		self.name_entry = StringVar()
		self.surname_entry = StringVar()
		self.address_entry = StringVar()
		self.pass_entry = StringVar()

		#mariadb connector
		self.connection = mariadb.connect(user="root", password=here goes your password, host="localhost", port=3306)
		self.cursor = self.connection.cursor()

		#this class contains all the text fields of the application
		Fields(self.frame, self.id_entry, self.name_entry, self.surname_entry, self.address_entry, self.pass_entry)

		#-------------------field comments--------------------
		self.field_comments = scrolled_text.ScrolledText(self.frame, width=18, height=7)
		self.field_comments.grid(row=5, column=1, pady=10, padx=10, columnspan=3)
		Label(self.frame, text="Comments", bg="black", fg="#c4ff4d").grid(row=5, column=0, pady=10, padx=10, sticky="w")

		#-------------------submenu--------------------
		self.navbar = Menu(self.root, bg="black", fg="#c4ff4d")
		self.root.config(menu=self.navbar)

		#file
		self.file = Menu(self.navbar, tearoff=0, bg="black", fg="#c4ff4d")
		self.file.add_command(label="Create database", command=self.create_db)
		self.file.add_command(label="Exit", command=self.exit_program)

		#edit
		self.edit = Menu(self.navbar, tearoff=0, bg="black", fg="#c4ff4d")
		self.edit.add_command(label="Clear all", command=self.clear_all_entrys)

		#crud options
		self.crud = Menu(self.navbar, tearoff=0, bg="black", fg="#c4ff4d")
		self.crud.add_command(label="Create", command=self.create_user)
		self.crud.add_command(label="Read", command=self.read_user)
		self.crud.add_command(label="Update", command=self.update_user)
		self.crud.add_command(label="Delete", command=self.delete_user)

		#help
		self.help_nav = Menu(self.navbar, tearoff=0, bg="black", fg="#c4ff4d")
		self.help_nav.add_command(label="License")
		self.help_nav.add_command(label="About...")

		#-------------------navbar--------------------
		self.navbar.add_cascade(label="File", menu=self.file)
		self.navbar.add_cascade(label="Edit", menu=self.edit)
		self.navbar.add_cascade(label="Crud", menu=self.crud)
		self.navbar.add_cascade(label="Help", menu=self.help_nav)

		#-------------------buttons--------------------
		#create
		Button(self.frame2, text="Create", fg="#c4ff4d", bg="black", width=4, command=self.create_user).grid(row=6, column=0, pady=10, padx=10)

		#read
		Button(self.frame2, text="Read", fg="#c4ff4d", bg="black", width=4, command=self.read_user).grid(row=6, column=1, pady=10, padx=10)

		#update
		Button(self.frame2, text="Update", fg="#c4ff4d", bg="black", width=4, command=self.update_user).grid(row=6, column=2, pady=10, padx=10)

		#delete
		Button(self.frame2, text="Delete", fg="#c4ff4d", bg="black", width=4, command=self.delete_user).grid(row=6, column=3, pady=10, padx=10)

	#--------------------functions----------------------
	def create_db(self):
		#create a database if it doesn't exist
		self.cursor.execute("CREATE DATABASE IF NOT EXISTS data_users")
		self.cursor.execute("USE data_users")
		self.cursor.execute("CALL create_table()")
		messagebox.showinfo("Estado de base de datos", "Base de datos creada con éxito")


	def clear_all_entrys(self):
		#remove everything in the inputs
		self.id_entry.set("")
		self.name_entry.set("")
		self.surname_entry.set("")
		self.address_entry.set("")
		self.pass_entry.set("")
		self.field_comments.delete("0.0", 'end')


	def create_user(self):
		#create a new user, otherwise if any required data is missing it will be notified with a message
		if (self.there_are_empty_fields()):
			messagebox.showerror("Oops", "Name, Surname, Address y Password son requeridos")
		else:
			self.cursor.execute("CALL adding_user(NULL, ?, ?, ?, ?, ?)", self.list_data_user())
			self.connection.commit()
			messagebox.showinfo("Registro", "Se ha creado un nuevo registro")


	def there_are_empty_fields(self):
		#check if all fields are empty
		#returns a boolean
		return self.is_empty_name_or_surname() or self.is_empty_address_or_pass()


	def is_empty_name_or_surname(self):
		#check if field name or field surname are empty
		#returns a boolean
		return self.is_empty_field(0) or self.is_empty_field(1)


	def is_empty_address_or_pass(self):
		#check if field address or field password are empty
		#returns a boolean
		return self.is_empty_field(2) or self.is_empty_field(3)


	def is_empty_field(self, num):
		#check if any text field is empty
		#receive a field number
		#returns a boolean
		return self.list_data_user()[num] == ""


	def delete_user(self):
		#remove a user from the database indicated by the id
		self.cursor.execute("CALL delete_user(?)", (self.id_entry.get(), ))
		self.connection.commit()
		self.clear_all_entrys()
		messagebox.showinfo("Estado del registro", "El registro se ha borrado")


	def read_user(self):
		#shows the data of user indicated by the id
		self.cursor.execute("CALL read_user(?)", (self.id_entry.get(), ))
		user_info = self.cursor.fetchall()
		self.send_to_entry(user_info)


	def send_to_entry(self, user_info):
		#sends the user data contained in the received tuple to the inputs, otherwise display a message that the user does exist
		#receive a tuple with user information
		try:
			self.name_entry.set(user_info[0][1])
			self.surname_entry.set(user_info[0][2])
			self.address_entry.set(user_info[0][3])
			self.pass_entry.set(user_info[0][4])
			self.field_comments.insert("0.0", user_info[0][5])
		except IndexError:
			messagebox.showerror("Estado del registro", "El usuario no existe o ha sido borrado, intenté con otro id")


	def update_user(self):
		#update user information in database
		self.cursor.execute("CALL update_user(" + self.id_entry.get() + ", ?, ?, ?, ?, ?)", self.list_data_user())
		self.connection.commit()
		messagebox.showinfo("Estado del registro", "El registro se ha actualizado")


	def list_data_user(self):
		#list all the strings in inputs except id
		#returns a tuple
		return self.name_entry.get(),self.surname_entry.get(),self.address_entry.get(),self.pass_entry.get(),self.field_comments.get("0.0", 'end')


	def exit_program(self):
		#exits the program, close the connection to the database and destroy root widget
		self.cursor.close()
		self.connection.close()
		self.root.destroy()


