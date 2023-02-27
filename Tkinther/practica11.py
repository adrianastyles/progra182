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

#3. Agregamos botones
botonAzul = Button(seccion1, text = "Botón azul", fg = "blue")
botonAzul.place(x=60, y=60, width = 100, height = 30)

botonNegro = Button(seccion2, text = "Botón negro", fg = "black")
botonNegro.grid(row = 0, column = 0)

botonCafe = Button(seccion2, text = "Botón café", fg = "brown")
botonCafe.grid(row = 1, column = 1)

botonVerde = Button(seccion3, text = "Botón verde", fg = "green")
botonVerde.pack()

ventana.mainloop()