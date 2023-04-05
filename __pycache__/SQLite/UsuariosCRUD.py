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
        
    if (rsUsu):
        for usu in rsUsu:
            tabla1.delete(*tabla1.get_children())
            tabla1.insert("", "end", text = usu[0], values = (usu[1], usu[2], usu[3]))
    else:
        messagebox.showwarning ("No encontrado", "El usuario no existe en la base de datos", icon = "error")

def EjecutaBusquedaUsuarios():
    bus = controlador.consultarTodosLosUsuarios()
    tabla.delete(*tabla.get_children()) #limpia
    for usu in bus:
        tabla.insert("", "end", text = usu[0], values = (usu[1], usu[2], usu[3]))

def EliminaSelectU():
    msg = messagebox.askquestion("Warning", "¿Está seguro de eliminar al usuario?")
    if (msg == "no"):
        messagebox.showinfo("No eliminado", "Usuario no eliminado")
    else:
        controlador.EliminarUsuarios(varDelete.get())
        messagebox.showinfo("Eliminado exitoso", "Usuario eliminado")
    
def ActualizarNombreU():
    controlador.ActualizarUsuariosNom(varAct.get(), varNomA.get())
    messagebox.showinfo("Actualización exitosa", "Se actualizó el nombre del usuario exitosamente")

def ActualizarCorreoU():
    controlador.ActualizarUsuariosCor(varAct.get(), varCorA.get())
    messagebox.showinfo("Actualización exitosa", "Se actualizó el correo del usuario exitosamente")

def ActualizarContraseñaU():
    controlador.ActualizarUsuariosCon(varAct.get(), varConA.get())
    messagebox.showinfo("Actualización exitosa", "Se actualizó la contraseña del usuario exitosamente")

Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x450")

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
tabla1 = ttk.Treeview (pestana2)
tabla1 ["columns"] = ("Nombre", "Correo", "Contraseña")
tabla1.column("#0", width = 60, minwidth = 60)
tabla1.column("Nombre", width = 100, minwidth = 100)
tabla1.column("Correo", width = 200, minwidth = 200)
tabla1.column("Contraseña", width = 100, minwidth = 100)
tabla1.heading("#0", text = "ID", anchor = tk.CENTER)
tabla1.heading("Nombre", text = "Nombre", anchor = tk.CENTER)
tabla1.heading("Correo", text = "Correo", anchor = tk.CENTER)
tabla1.heading("Contraseña", text = "Contraseña", anchor = tk.CENTER)
tabla1.pack()

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

#PESTAÑA 4
varAct = tk.StringVar()
varNomA = tk.StringVar()
varCorA = tk.StringVar()
varConA = tk.StringVar()
titulo4 = Label(pestana4, text = "Actualizar usuarios", fg = "blue", font = ("Modern", 18)). pack()
lblID2 = Label(pestana4, text = "Identificador de usuario:").pack()
txtID2 = Entry(pestana4, textvariable = varAct).pack()
lblNom1 = Label(pestana4, text = "Nombre:").pack()
txtNom1 = Entry(pestana4, textvariable = varNomA).pack()
btnNom = Button(pestana4, text = "Actualizar nombre", command = ActualizarNombreU).pack()
lblCor1 = Label(pestana4, text = "Correo:").pack()
txtCor1 = Entry(pestana4, textvariable = varCorA).pack()
btnCor = Button(pestana4, text = "Actualizar correo", command = ActualizarCorreoU).pack()
lblCon1 = Label(pestana4, text = "Contraseña:").pack()
txtCon1 = Entry(pestana4, textvariable = varConA).pack()
btnCon = Button(pestana4, text = "Actualizar contraseña", command = ActualizarContraseñaU).pack()

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