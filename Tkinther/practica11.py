from tkinter import Tk, Button, Frame

#1. Generar una ventana
ventana = Tk()
ventana.title("Práctica 11")
ventana.geometry("600x400")

#2. Agregar Frames
seccion1 = Frame(ventana, bg = "orange")
seccion1.pack(expand = True, fill = 'both')

seccion2 = Frame(ventana, bg = "pink")
seccion2.pack(expand = True, fill = 'both')

seccion3 = Frame(ventana, bg = "purple")
seccion3.pack(expand = True, fill = 'both')

ventana.mainloop()