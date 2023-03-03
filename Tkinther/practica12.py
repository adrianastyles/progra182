from tkinter import Tk, Button, Frame, messagebox, ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from validador import *

ventana = Tk()
ventana.title("Login")
ventana.geometry("450x220")

seccion1 = Frame(ventana, bg = "#e9edd1")
seccion1.pack(expand = True, fill = 'both')


#CREAR FUNCIONES

def Ingresar():
    Validador2 = Validador(correo1, contraseña1)
    Validador2.getCorreo()
    Validador2.getContraseña()
    Validador.Validador1()

#CORREO

label1=tk.Label(seccion1,text="Ingrese su correo:")
label1.place (x=30, y=60)
correo1= Entry(seccion1, width=35)
correo1.place(x=140, y = 60)

#CONTRASEÑA

label2=tk.Label(seccion1,text="Ingrese su contraseña:")
label2.place (x=30, y=110)
contraseña1=tk.Entry(seccion1, width=35, show = "*")
contraseña1.place(x=160, y = 110)

#BOTON INGRESAR

botonIngresar = Button(seccion1, text = "Ingresar", fg = "black", bg = "#d5d6ce", command = Ingresar)
botonIngresar.place(x=170, y=180, width = 100, height = 30)

ventana.mainloop()