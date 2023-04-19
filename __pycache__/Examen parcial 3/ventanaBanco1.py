from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBanco import *

controlador = controladorBDBanco

def Insert():
    controlador.Guardar(varNom.get(), varNCuenta.get(), varSaldo.get())



Ventana = Tk()
Ventana.title("TU CUENTA DE BANCO")
Ventana.geometry("500x350")

panel = ttk.Notebook(Ventana)
panel.pack(fill = 'both', expand = 'yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)

#PESTAÑA 1

titulo = Label(pestana1, text = "Registrar nuevo", fg = "blue", font = ("Modern", 18)). pack()
varNom = tk.StringVar()
varNCuenta = tk.StringVar()
varSaldo = tk.StringVar()

lblNom = Label(pestana1, text = "Nombre del titular:").pack()
txtNom = Entry(pestana1, textvariable = varNom).pack()

lblCor = Label(pestana1, text = "Número de cuenta:").pack()
txtCor = Entry(pestana1, textvariable = varNCuenta).pack()

lblCont = Label(pestana1, text = "Saldo:").pack()
txtCont = Entry(pestana1, textvariable = varSaldo).pack()

btnGuardar = Button(pestana1, text = "Guardar", command = Insert).pack()

#PESTAÑA 2

varID = tk.StringVar()
varNomA = tk.StringVar()
varNumCA = tk.StringVar()
varSaldoA = tk.StringVar()
titulo4 = Label(pestana2, text = "Actualizar", fg = "blue", font = ("Modern", 18)). pack()
lblID2 = Label(pestana2, text = "Identificador de usuario:").pack()
txtID2 = Entry(pestana2, textvariable = varID).pack()
lblNom1 = Label(pestana2, text = "Nombre:").pack()
txtNom1 = Entry(pestana2, textvariable = varNomA).pack()
btnNom = Button(pestana2, text = "Actualizar nombre").pack()
lblCor1 = Label(pestana2, text = "Número de cuenta:").pack()
txtCor1 = Entry(pestana2, textvariable = varNumCA).pack()
btnCor = Button(pestana2, text = "Actualizar número de cuenta").pack()
lblCon1 = Label(pestana2, text = "Saldo:").pack()
txtCon1 = Entry(pestana2, textvariable = varSaldoA).pack()
btnCon = Button(pestana2, text = "Actualizar saldo").pack()

#PESTAÑA 3

titulo3 = Label(pestana3, text = "Consulta", fg = "blue", font = ("Modern", 18)). pack()
lbl3 = Label(pestana3, text = "Consultar todos los usuarios").pack()
tabla = ttk.Treeview (pestana3)
tabla ["columns"] = ("Nombre", "Número de cuenta", "Saldo")
tabla.column("#0", width = 60, minwidth = 60)
tabla.column("Nombre", width = 100, minwidth = 100)
tabla.column("Número de cuenta", width = 200, minwidth = 200)
tabla.column("Saldo", width = 100, minwidth = 100)
tabla.heading("#0", text = "ID", anchor = tk.CENTER)
tabla.heading("Nombre", text = "Nombre", anchor = tk.CENTER)
tabla.heading("Número de cuenta", text = "Número de cuenta", anchor = tk.CENTER)
tabla.heading("Saldo", text = "Saldo", anchor = tk.CENTER)
tabla.pack()
btnBuscar = Button(pestana3, text = "Buscar").pack()

panel.add(pestana1, text = 'Formuario')
panel.add(pestana2, text = 'Actualizar')
panel.add(pestana3, text = 'Consultar cuentas')


Ventana.mainloop()