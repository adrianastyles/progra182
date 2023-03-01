from tkinter import Tk, Button, Frame, messagebox

#5. Agregar función de mensaje
def mostrarMensaje():
    messagebox.showinfo('Información', "Ventana de información")
    messagebox.showerror('Error', "Fallo")
    print(messagebox.askokcancel('Pregunta', "¿Seguro que quieres guardar?"))
    print(messagebox.askyesno('Pregunta', "¿O no? ¿O nada?"))

#6. Función agregar botones
def agregarBoton():
    botonVerde.config(text = '+', bg = "#18a83e", fg = "white")
    botonNuevo = Button(seccion3, text = "Boton nuevo", bg = "#1122ba", fg = "white")
    botonNuevo.pack()

#1. Generar una ventana
ventana = Tk()
ventana.title("Práctica 11")
ventana.geometry("600x400")

#2. Agregar Frames
seccion1 = Frame(ventana, bg = "#f5c493")
seccion1.pack(expand = True, fill = 'both')

seccion2 = Frame(ventana, bg = "#faa0d3")
seccion2.pack(expand = True, fill = 'both')

seccion3 = Frame(ventana, bg = "#c079d4")
seccion3.pack(expand = True, fill = 'both')

#3. Agregamos botones
botonAzul = Button(seccion1, text = "Botón azul", fg = "black", bg = "#bcf5eb", command = mostrarMensaje)
botonAzul.place(x=60, y=60, width = 100, height = 30)

botonNegro = Button(seccion2, text = "Botón negro", fg = "white", bg = "black")
botonNegro.grid(row = 0, column = 0)

botonAmarillo = Button(seccion2, text = "Botón amarillo", fg = "black", bg = "#ffff4f")
botonAmarillo.grid(row = 1, column = 1)

botonVerde = Button(seccion3, text = "Botón verde", fg = "black", bg = "#98fa7f", command = agregarBoton)
botonVerde.pack()

ventana.mainloop()