from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorBD import *

#Instancia: puente entre los dos archivos
controlador = controladorBD()

#metodo que usará mi objeto controlador para insertar
def EjecutaInsert():
    controlador.GuardarUsuario(varNom.get(), varCor.get(), varCont.get())

Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x300")

panel = ttk.Notebook(Ventana)
panel.pack(fill = 'both', expand = 'yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

# Pestaña 1

titulo = Label(pestana1, text = "Registro de usuarios", fg = "blue", font = ("Modern", 18)). pack()
varNom = tk.StringVar()
varCor = tk.StringVar()
varCont = tk.StringVar()

lblNom = Label(pestana1, text = "Nombre:").pack()
txtNom = Entry(pestana1, textvariable = varNom).pack()

lblCor = Label(pestana1, text = "Correo:").pack()
txtCor = Entry(pestana1, textvariable = varCor).pack()

lblCont = Label(pestana1, text = "Contraseña:").pack()
txtCont = Entry(pestana1, textvariable = varCont).pack()

btnGuardar = Button(pestana1, text = "Guardar usuario", command = EjecutaInsert).pack()


panel.add(pestana1, text = 'Formulario de usuarios')
panel.add(pestana2, text = 'Buscar usuario')
panel.add(pestana3, text = 'Consultar usuarios')
panel.add(pestana4, text = 'Actualizar usuario')




Ventana.mainloop()