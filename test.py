# -*- enconding: utf-8 -*-

import c_parser 
from tkinter import filedialog
from tkinter import*
from tkinter import messagebox 

class ideADK():
	def __init__(self):
		self.ruta="none"
		self.iniciarVista()
		pass
	def iniciarVista(self):
		self.vista=Tk()
		self.vista.title("ideADK justline")
		self.vista.geometry('500x610')
		self.boton= Button(self.vista,text="cargar",fg="black",command=self.cargarArchivo)
		self.boton.place(x=0, y=0)
		self.boton= Button(self.vista,text="guardar",fg="black",command=self.guardarArchivo)
		self.boton.place(x=100, y=0)
		self.boton= Button(self.vista,text="compilar",fg="black",command=self.compilar)
		self.boton.place(x=45, y=0)

		self.text = Text(self.vista,width=60,height=35)
		self.text.place(x=8,y=27)
		self.vista.mainloop()

	def cargarArchivo(self):
		self.text.delete("1.0",END)
		self.ruta = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("ADK files","*.ADK"),("all files","*.*")))
		f = open(self.ruta, 'r')
		data = f.read()
		self.text.insert(INSERT, data)
		f.close()

	def guardarArchivo(self):
		if(self.ruta!="none"):
			f = open(self.ruta, 'w')
			f.write(self.text.get("1.0",END))
			f.close()
		else:
			self.ruta=filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("ADK files","*.ADK"),("all files","*.*")))
			aux=self.ruta+".ADK"
			f = open(aux, 'w')
			f.write(self.text.get("1.0",END))
			f.close()
		
	def compilar(self):
		datos=self.text.get("1.0",END)
		c_parser.VERBOSE = 0
		try:
			print(self.text.get("1.0",END))
			c_parser.parser.parse(datos, tracking=True)
			print ('[ok]')
			messagebox.showinfo(message="Compilado", title="resultado")

		except:
			print ('[error]')
			messagebox.showerror(message="error sintaxis", title="resultado")

x=ideADK()

	
