from tkinter import Tk, Button, Frame
import tkinter as tk
from tkinter import *
from generador import *

#CREAR FUNCIONES

ventana = Tk()
ventana.title("GENERADOR DE CONTRASEÑAS")
ventana.geometry("450x250")

seccion1 = Frame(ventana, bg = "#e6f8fa")
seccion1.pack(expand = True, fill = 'both')


def Ingresar():
    datos = Generador()
    datos.Generador1(int(var1.get()), var2.get(), var3.get())
    
def Validar():
    datos = Generador()
    datos.Validar1(int(var1.get()), var2.get(), var3.get())

#CONTRASEÑA

var1 = tk.StringVar()
label1=tk.Label(seccion1, text="Ingrese la longitud de contraseña:")
label1.place (x=10, y=30)
c1= Entry(seccion1, width=10, textvariable = var1)
c1.place(x=200, y = 30)

var2 = tk.StringVar()
label1=tk.Label(seccion1, text="¿Desea mayúsculas?:")
label1.place (x=10, y=70)
c2= Entry(seccion1, width=10, textvariable = var2)
c2.place(x=200, y = 70)

var3 = tk.StringVar()
label1=tk.Label(seccion1, text="¿Desea caracteres especiales?:")
label1.place (x=10, y=110)
c3= Entry(seccion1, width=10, textvariable = var3)
c3.place(x=200, y = 110)


#BOTON GENERAR/VALIDAR

botonIngresar = Button(seccion1, text = "Generar", fg = "black", bg = "#d5d6ce", command = Ingresar)
botonIngresar.place(x=70, y=160, width = 100, height = 30)

botonValidar = Button(seccion1, text = "Validar", fg = "black", bg = "#d5d6ce", command = Validar)
botonValidar.place(x=250, y=160, width = 100, height = 30)

ventana.mainloop()