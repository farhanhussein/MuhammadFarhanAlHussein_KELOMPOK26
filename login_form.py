from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.font import Font


class login_form:
	def __init__(self,root):
		self.root=root
		root.configure(bg="brown")
		root.title("Login")
		
		
		# login label
		bigfont = Font(
			family = "Comic Sans MS",
			size = 25, 
			weight = "normal",
			slant = "roman",
			underline = 0,
			overstrike=0)
		login_label=Label(root,text="Welcome to Pizza Corner",font=bigfont ,bg='sky blue')
		login_label.place(x=125,y=20)
		#username label
		user_label=Label(root,text="Username :",font="helvetica 15 ",bg="light steel blue")
		user_label.place(x=200,y=150)

		global user_inp
		global pass_inp
		user_inp=StringVar()
		pass_inp=StringVar()
		# entry widget untuk username
		user_e=Entry(root,textvariable=user_inp)
		user_e.place(x=320,y=153,height=25)
		#pin label
		pass_label=Label(root,text="Pin :",font="helvetica 15 ",bg="light steel blue")
		pass_label.place(x=210,y=200)

		# entry widget untuk pin
		pass_e=Entry(root,textvariable=pass_inp)
		pass_e.place(x=320,y=200,height=25)

		login_b=Button(root,text="Login",font="helvetica 18 ",bg="light steel blue",command=lambda :self.login())
		login_b.place(x=250,y=300)
		# button untuk exit
		exit_b=Button(root,text="Exit",font="helvetica 15 ",bg="light steel blue",command=lambda :self.destroy())
		exit_b.place(x=260,y=400)

	#login function untuk authentication, apakah user dan password benar atau salah
	def login(self):
		if user_inp.get() == "farhanhussein" and pass_inp.get() == "1234":
			root.destroy()
			import pos_form
		else:
			messagebox.showinfo('Error','Authentication Failed')
			user_inp.set("")
			pass_inp.set("")


	def destroy(self):
		root.destroy()


root = Tk()

image_1 = Image.open('C:\\Users\\LENOVO\\Downloads\\w1.jpg')
bck_end = ImageTk.PhotoImage(image_1)
lbl = Label(root, image=bck_end)
lbl.place(x=0, y=0)
obj2=login_form(root)
root.geometry("600x500")
root.resizable(width=0, height=0)
root.mainloop()
