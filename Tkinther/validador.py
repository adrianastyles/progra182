from tkinter import messagebox
class Validador:
    

    def __init__ (self):
        self.__contraseña = "harrystyles"
        self.__correo = "121038379@upq.edu.mx"
        
        
    def Validador1(self, c, cont):
        if (c == "" or cont == ""):
            messagebox.showerror('Error', "Llene todos los campos")
        else:
            if (self.__correo == c and  self.__contraseña == cont):
                messagebox.showinfo('Información', "Inicio de sesión exitoso")
            else:
                messagebox.showerror('Error', "Ingrese la contraseña correcta")