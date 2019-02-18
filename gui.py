from tkinter import *
calculator = Tk()
calculator.title('Calculator')
calculator.resizable(0, 0)

class Application(Frame):
	def _init_(self, master, *args, **kwargs):
		Frame._init_(self, master, *args, **kwargs)
		self.createWidgets()

def createWidgets(self):
	self.display = Entry(self, font = ('Helvetica', 16), relief = RAISED, justify = RIGHT)
	self.display.insert(0, '0')
	self.display.grid(row=0, column=0)

	self.sevenButton = Button(self, font=('Helvetica', 11), text='7')
	self.sevenButton.grid(row=1, column=0)


app = Application(calculator).grid()
calculator.mainloop()

