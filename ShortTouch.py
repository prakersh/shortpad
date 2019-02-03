from tkinter import *
import sys
cmd1 = ""
cmd2 = ""
cmd3 = ""
cmd4 = ""

class config_frame(object):
	def __init__(self, masterfrommain):
		self.master= masterfrommain
		self.master.grid(column=0,row=0, sticky=(N,W,E,S) )
		self.master.columnconfigure(0, pad=60, weight = 1)
		self.master.rowconfigure(0, weight = 1)
		self.master.pack(pady = 30, padx = 30)

		# Dictionary with options
		self.command_choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe', 'custom'}

		for i in range(4):
			continue	
		# Create a Tkinter variable
		self.var1 = StringVar(root)
		self.var2 = StringVar(root)
		self.var3 = StringVar(root)
		self.var4 = StringVar(root)
 

		self.var1.set('None') # set the default option
		self.var2.set('None') # set the default option
		self.var3.set('None') # set the default option
		self.var4.set('None') # set the default option
 
		Label(master, text="Choose upper left command").grid(row =0, column = 0)
		popupMenu = OptionMenu(self.master, self.var1, *self.command_choices)
		popupMenu.grid(row = 0, column =1, sticky=E)
		Label(master, text="Choose upper right command").grid(row = 2, column = 0)
		popupMenu = OptionMenu(self.master, self.var2, *self.command_choices)
		popupMenu.grid(row = 2, column =1 , sticky=E)
		Label(master, text="Choose a lower left command").grid(row = 3, column = 0)
		popupMenu = OptionMenu(self.master, self.var3, *self.command_choices)
		popupMenu.grid(row = 3, column =1, sticky=E)
		Label(master, text="Choose a lower left command").grid(row = 4, column = 0)
		popupMenu = OptionMenu(self.master, self.var4, *self.command_choices)
		popupMenu.grid(row = 4, column =1, sticky=E)

		# link function to change dropdown
		self.var1.trace('w', self.change_dropdown1)
		self.var2.trace('w', self.change_dropdown2)
		self.var3.trace('w', self.change_dropdown3)

		self.var4.trace('w', self.change_dropdown4)
		
		self.button1 = Button(master, text="Start", fg="red",command=self.starting).grid(row=5, column=0,pady=20, padx=0)
		self.button2 = Button(master, text="Apply", fg="red",command=self.applying).grid(row=5, column=1, pady=20, padx=0)
		self.button3 = Button(master, text="Stop", fg="red",command=self.stoping).grid(row=5, column=2, pady=20, padx=0 )

	def applying(self):
		global cmd1, cmd2, cmd3 , cmd4
		print(cmd1, "\n",cmd2, "\n",cmd3, "\n",cmd4 )

	def starting(self):
		print("working")	
	def stoping(self):
		print(self.var4.get())

	def change_dropdown1(self,*args):
		global cmd1
		if self.var1.get() == "custom":
			self.w1=popupWindow(self.master)
			self.master.wait_window(self.w1.top)
			cmd1 = self.w1.value
		else:
			cmd1 = self.var1.get()
			print(cmd1)

	def change_dropdown2(self,*args):
		global cmd2
		if self.var2.get() == "custom":
			self.w2=popupWindow(self.master)
			self.master.wait_window(self.w2.top)
			cmd2 = self.w2.value
		else:
			cmd2 = self.var2.get()
		
	def change_dropdown3(self,*args):
		global cmd3
		if self.var3.get() == "custom":
			self.w3=popupWindow(self.master)
			self.master.wait_window(self.w3.top)
			cmd3 = self.w3.value
		else:
			cmd3 = self.var3.get()

	def change_dropdown4(self,*args):
		global cmd4
		if self.var4.get() == "custom":
			self.w4=popupWindow(self.master)
			self.master.wait_window(self.w4.top)
			cmd4 = self.w4.value
		else:
			cmd4 = self.var4.get()


class popupWindow(object):
	def __init__(self,master):
		top=self.top=Toplevel(master)
		self.l=Label(top,text="Hello World")
		self.l.pack()
		self.e=Entry(top)
		self.e.pack()
		self.b=Button(top,text='Ok',command=self.cleanup)
		self.b.pack()
	def cleanup(self):
		self.value=self.e.get()
		self.top.destroy()
	
 
if __name__ == "__main__":
	root = Tk()
	root.title("Tk dropdown example")
	master = Frame(root)
	k=config_frame(master)
	root.mainloop()



		
