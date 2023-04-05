from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorBD import *

#Instancia: puente entre los dos archivos
controlador = controladorBD()

#metodo que usará mi objeto controlador para insertar
def EjecutaInsert():
    controlador.GuardarUsuario(varNom.get(), varCor.get(), varCont.get())
    
def EjecutaSelectU():
    rsUsu = controlador.consultarUsuario(varBus.get())
    for usu in rsUsu:
        cadena = str(usu[0]) + " " + usu[1] + " " + usu[2] + " " + str(usu[3])
        
    if (rsUsu):
        textBus.config(state = 'normal')
        textBus.delete(1.0, 'end')
        textBus.insert('end', cadena)
        textBus.config(state='disabled')
    else:
        messagebox.showwarning ("No encontrado", "El usuario no existe en la base de datos")

def EjecutaBusquedaUsuarios():
    bus = controlador.consultarTodosLosUsuarios()
    tabla.delete(*tabla.get_children()) #limpia
    for usu in bus:
        tabla.insert("", "end", text = usu[0], values = (usu[1], usu[2], usu[3]))

def EliminaSelectU():
        controlador.EliminarUsuarios(varDelete.get())
        

Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x350")

panel = ttk.Notebook(Ventana)
panel.pack(fill = 'both', expand = 'yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

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
txtCont = Entry(pestana1, textvariable = varCont, show = "*").pack()

btnGuardar = Button(pestana1, text = "Guardar usuario", command = EjecutaInsert).pack()

#Pestaña 2: Buscar usuario

titulo2 = Label(pestana2, text = "Buscar usuario", fg = "green", font = ("Modern",18)).pack()

varBus = tk.StringVar()
lblid = Label(pestana2, text = "Identificador de usuario:").pack()
txtid = Entry(pestana2, textvariable = varBus).pack()
btnBusqueda = Button(pestana2, text = "Buscar", command = EjecutaSelectU).pack()

subBus = Label(pestana2, text = "Registrado:", fg = "blue", font = ("Modern",15)).pack()
textBus = tk.Text(pestana2, height=5, width=52)
textBus.pack()

#PESTAÑA 3
titulo3 = Label(pestana3, text = "Consultar usuarios", fg = "blue", font = ("Modern", 18)). pack()
tabla = ttk.Treeview (pestana3)
tabla ["columns"] = ("Nombre", "Correo", "Contraseña")
tabla.column("#0", width = 60, minwidth = 60)
tabla.column("Nombre", width = 100, minwidth = 100)
tabla.column("Correo", width = 200, minwidth = 200)
tabla.column("Contraseña", width = 100, minwidth = 100)
tabla.heading("#0", text = "ID", anchor = tk.CENTER)
tabla.heading("Nombre", text = "Nombre", anchor = tk.CENTER)
tabla.heading("Correo", text = "Correo", anchor = tk.CENTER)
tabla.heading("Contraseña", text = "Contraseña", anchor = tk.CENTER)
tabla.pack()
btnUsu = Button(pestana3, text = "Buscar", command = EjecutaBusquedaUsuarios).pack()

#PESTAÑA 5

varDelete = tk.StringVar()
titulo5 = Label(pestana5, text = "Eliminar usuarios", fg = "blue", font = ("Modern", 18)). pack()
lblID1 = Label(pestana5, text = "Identificador de usuario:").pack()
txtID1 = Entry(pestana5, textvariable = varDelete).pack()
btnEliminar = Button(pestana5, text = "Eliminar", command = EliminaSelectU).pack()

panel.add(pestana1, text = 'Formulario de usuarios')
panel.add(pestana2, text = 'Buscar usuario')
panel.add(pestana3, text = 'Consultar usuarios')
panel.add(pestana4, text = 'Actualizar usuario')
panel.add(pestana5, text = 'Eliminar usuario')


Ventana.mainloop()