from tkinter import Tk, Button, Frame, messagebox, ttk
import tkinter as tk

ventana = Tk()
ventana.title("Login")
ventana.geometry("450x220")

seccion1 = Frame(ventana, bg = "#e9edd1")
seccion1.pack(expand = True, fill = 'both')

#CREAR FUNCIONES

def Ingresar():
    correo=tk.StringVar()
    contraseña=tk.StringVar()
    if (correo == "" or contraseña == ""):
        messagebox.showerror('Error', "Ingrese sus datos")
    else:
        messagebox.showinfo('Información', "Inicio de sesión exitoso")

#CORREO

correo=tk.StringVar()

label1=tk.Label(seccion1,text="Ingrese su correo:")
label1.place (x=30, y=60)
entry1=tk.Entry(seccion1, width=35, textvariable = correo)
entry1.place(x=140, y = 60)

#CONTRASEÑA

contraseña=tk.StringVar()

label2=tk.Label(seccion1,text="Ingrese su contraseña:")
label2.place (x=30, y=110)
entry2=tk.Entry(seccion1, width=35, textvariable = contraseña)
entry2.place(x=160, y = 110)

#BOTON INGRESAR

botonIngresar = Button(seccion1, text = "Ingresar", fg = "black", bg = "#d5d6ce", command = Ingresar)
botonIngresar.place(x=60, y=180, width = 100, height = 30)

#BOTON LIMPIAR

botonLimpiar = Button(seccion1, text = "Limpiar", fg = "black", bg = "#d5d6ce")
botonLimpiar.place(x=300, y=180, width = 100, height = 30)

ventana.mainloop()