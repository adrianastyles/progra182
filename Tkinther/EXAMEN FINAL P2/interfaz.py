from tkinter import Tk, Button, Frame
import tkinter as tk
from tkinter import *
from tkinter import ttk
from convertidor import *

ventana = Tk()
ventana.title("CONVERTIDOR")
ventana.geometry("450x200")

seccion = Frame(ventana, bg = "#c2c4c3")
seccion.pack(expand = True, fill = 'both')

conv = Convertidor1()

def Romano():
    conv.RomanosAArabigo(varRom.get())

def Arabigo():
    conv.ArabigoaRomano(int(varAra.get()))
    

titulo1 = Label(seccion, text = "Conversión de números arábigos a romanos y viceversa", fg = "blue", font = ("Modern", 15)). pack()

varAra = tk.StringVar()
label1=tk.Label(seccion, text="Ingrese un número arábigo para convertir a romano:")
label1.pack()
entry1= Entry(seccion, width=20, textvariable = varAra)
entry1.pack()

btnConvA = Button(seccion, text = "Convertir arábigo", command = Arabigo).pack()

varRom = tk.StringVar()
label2=tk.Label(seccion, text="Ingrese un número romano para convertir a arábigo en mayúsculas:")
label2.pack()
entry2= Entry(seccion, width=20, textvariable = varRom)
entry2.pack()

btnConvR = Button(seccion, text = "Convertir romano", command = Romano).pack()

ventana.mainloop()