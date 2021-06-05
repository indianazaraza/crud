from tkinter import Tk, Frame
from buttons_navbar import Buttons_navbar

class Crud:
	def __init__(self, root):
		#main class where the application runs
		#receive a root as a parameter
		self.root = root
		self.root.title("CRUD")
		self.root.config(bg="black")
		self.frame = Frame()
		self.frame.pack()
		self.frame.config(bg="black")
		self.frame2 = Frame()
		self.frame2.pack()
		self.frame2.config(bg="black")

		#this class contains buttons, navigation bar, database connection and functions
		Buttons_navbar(self.root, self.frame, self.frame2)



if (__name__ == "__main__") :
	root = Tk()
	app = Crud(root)
	root.mainloop()