from tkinter import messagebox

class Generador14:
    
    def __init__(self):
        self.__saldo=1000    

    def Ingresar(self,r):
        saldo=self.__saldo+r
        messagebox.showinfo("Ingreso exitoso", "El saldo es: " + str(saldo))
        self.__saldo=saldo

    def Retirar(self,r):
        if (r <= self.__saldo):
            saldo=self.__saldo-r
            messagebox.showinfo("Retiro exitoso", "El saldo es: " + str(saldo))
            self.__saldo=saldo
        else:
            messagebox.showerror("Warning", "Saldo insuficiente")
            
    def Depositar(self, r):
        if(r <= self.__saldo):
            saldo=self.__saldo-r
            messagebox.showinfo("Depósito exitoso", "El saldo depositado fue: " + str(r) + ". Su saldo actual es: " +  str(saldo))
            self.__saldo=saldo
        else:
            messagebox.showerror("Warning", "Saldo insuficiente")
        
    def getSaldo(self):
        return self.__saldo
    
    