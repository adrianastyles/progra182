from tkinter import Tk, Button, Frame
import tkinter as tk
from tkinter import *
from matricula import *


def Generar():
    datos = GeneradorMatricula(var1.get(), var2.get(), var3.get(), var4.get(), var5.get())
    GeneradorMatricula.Generador1(nombre1, apellidoP1, apellidoM1, año1, carrera1)

ventana = Tk()
ventana.title("Generador de matrículas")
ventana.geometry("450x250")

seccion1 = Frame(ventana, bg = "#e9edd1")
seccion1.pack(expand = True, fill = 'both')

#NOMBRE
var1 = tk.StringVar()
label1=tk.Label(seccion1, text="Nombre:")
label1.place (x=20, y=30)
nombre1= Entry(seccion1, width=35, textvariable = var1)
nombre1.place(x=80, y = 30)

#APELLIDO PATERNO
var2 = tk.StringVar()
label2=tk.Label(seccion1, text="Apellido Paterno:")
label2.place (x=20, y=60)
apellidoP1=Entry(seccion1, width=35, textvariable = var2)
apellidoP1.place(x=140, y = 60)

#APELLIDO PATERNO
var3 = tk.StringVar()
label3=tk.Label(seccion1, text="Apellido Materno:")
label3.place (x=20, y=90)
apellidoM1=Entry(seccion1, width=35, textvariable = var3)
apellidoM1.place(x=140, y = 90)

#AÑO DE NACIMIENTO
var4 = tk.StringVar()
label4=tk.Label(seccion1, text="Año de nacimiento:")
label4.place (x=20, y=120)
año1=Entry(seccion1, width=10, textvariable = var4)
año1.place(x=140, y = 120)

#CARRERA
var5 = tk.StringVar()
label5=tk.Label(seccion1, text="Carrera:")
label5.place (x=20, y=150)
carrera1=Entry(seccion1, width=35, textvariable = var5)
carrera1.place(x=80, y = 150)

botonGenerar = Button(seccion1, text = "GENERAR", fg = "black", bg = "#d5d6ce", command = Generar)
botonGenerar.place(x=170, y=200, width = 100, height = 30)

ventana.mainloop()