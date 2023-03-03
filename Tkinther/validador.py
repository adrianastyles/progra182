class Validador:
    

    def __init__ (self, c, cont):
        self.__contraseña = cont
        self.__correo = c
        
        
    def Validador1(self, cont):
        
        from tkinter import messagebox
        cont1 = "harrystyles"
        if (c == "" or cont == ""):
            messagebox.showerror('Error', "Llene todos los campos")
        else:
            if (cont == cont1):
                messagebox.showinfo('Información', "Inicio de sesión exitoso")
            else:
                messagebox.showerror('Error', "Ingrese la contraseña correcta")
            
    def getContraseña (self):
        return self.__contraseña
    
    def setContraseña (self, cont):
        self.__contraseña = cont
        
    def getCorreo (self):
        return self.__correo
    
    def setCorro (self, c):
        self.__correo = c