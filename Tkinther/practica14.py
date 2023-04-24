from tkinter import Tk, Button, Frame
import tkinter as tk
from tkinter import *
from tkinter import ttk
from generadorp14 import *
from user import *

ventana = Tk()
ventana.title("GENERADOR DE CONTRASEÑAS")
ventana.geometry("450x300")

panel = ttk.Notebook(ventana)
panel.pack(fill = 'both', expand = 'yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

d = Generador14()


def Retirar():
    d.Retirar(int(varRetirar.get()))
    
def Ingresar():
    d.Ingresar(int(varIngresar.get()))

def Consultar():
    u = User(varCuenta.get(), varTitular.get(), varEdad.get())
    messagebox.showinfo("Consulta", "Cuenta: " + str(u.getCuenta()) + "\nTitular: " +  str(u.getTitular()) +
                        "\nEdad: " + str(u.getEdad()) + 
                        "\nSaldo actual: " + str(d.getSaldo()) + " pesos")
    
def Depositar():
    d.Depositar(int(var13.get()))

    
#PESTAÑA 1

titulo1 = Label(pestana1, text = "Consulta de saldo", fg = "blue", font = ("Modern", 18)). pack()

varCuenta = tk.StringVar()
label1=tk.Label(pestana1, text="No. de cuenta:")
label1.pack()
c1= Entry(pestana1, width=25, textvariable = varCuenta)
c1.pack()

varTitular = tk.StringVar()
label2=tk.Label(pestana1, text="Titular:")
label2.pack()
c2= Entry(pestana1, width=25, textvariable = varTitular)
c2.pack()

varEdad = tk.StringVar()
label3=tk.Label(pestana1, text="Edad:")
label3.pack()
c3= Entry(pestana1, width=10, textvariable = varEdad)
c3.pack()

btnCon = Button(pestana1, text = "Consultar", command = Consultar).pack()

#PESTAÑA 2

titulo2 = Label(pestana2, text = "Retiro de efectivo", fg = "blue", font = ("Modern", 18)). pack()

var5 = tk.StringVar()
label5=tk.Label(pestana2, text= "No. de cuenta:")
label5.pack()
c5= Entry(pestana2, width=25, textvariable = var5)
c5.pack()

varRetirar = tk.StringVar()
label6=tk.Label(pestana2, text="Ingrese saldo a retirar:")
label6.pack()
c6= Entry(pestana2, width=10, textvariable = varRetirar)
c6.pack()

btnRet = Button(pestana2, text = "Retirar", command = Retirar).pack()

#PESTAÑA 3

titulo3 = Label(pestana3, text = "Ingreso de efectivo", fg = "blue", font = ("Modern", 18)). pack()

var7 = tk.StringVar()
label7=tk.Label(pestana3, text="No. de cuenta:")
label7.pack()
c7= Entry(pestana3, width=25, textvariable = var7)
c7.pack()

varIngresar = tk.StringVar()
label8=tk.Label(pestana3, text= "Ingrese saldo a ingresar:")
label8.pack()
c8= Entry(pestana3, width=10, textvariable = varIngresar)
c8.pack()

btnIngresar = Button(pestana3, text = "Ingresar", command = Ingresar).pack()

#PESTAÑA 4

titulo3 = Label(pestana4, text = "Depósito a otra cuenta", fg = "blue", font = ("Modern", 18)). pack()

var9 = tk.StringVar()
label9=tk.Label(pestana4, text= "No. de cuenta:")
label9.pack()
c9= Entry(pestana4, width=25, textvariable = var9)
c9.pack()

var10 = tk.StringVar()
label10=tk.Label(pestana4, text= "Titular:")
label10.pack()
c10= Entry(pestana4, width=25, textvariable = var10)
c10.pack()

var11 = tk.StringVar()
label11=tk.Label(pestana4, text= "No. de cuenta a depositar:")
label11.pack()
c11= Entry(pestana4, width=25, textvariable = var11)
c11.pack()

var12 = tk.StringVar()
label12=tk.Label(pestana4, text= "Titular de la cuenta a depositar:")
label12.pack()
c12= Entry(pestana4, width=25, textvariable = var12)
c12.pack()

var13 = tk.StringVar()
label13=tk.Label(pestana4, text="Saldo a depositar:")
label13.pack()
c13= Entry(pestana4, width=10, textvariable = var13)
c13.pack()

btnDep = Button(pestana4, text = "Depositar", command = Depositar).pack()


panel.add(pestana1, text = 'Consultar')
panel.add(pestana2, text = 'Retirar')
panel.add(pestana3, text = 'Ingresar')
panel.add(pestana4, text = 'Depositar')

ventana.mainloop()