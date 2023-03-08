from tkinter import messagebox
from random import choice
class Generador:
    

    def __init__ (self):
        self.__longitud = 
        self.__mayusculas = 
        self.__caracteres = 
        
        
    def Generador1(self, long, mayus, caracter):
        long = self.__longitud
        
        if (mayus == "si" and caracter == "si"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
            p = ""
            p = p.join([choice(valores) for i in range(long)])
            print(p)
        elif (mayus == "no" and caracter == "si"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyz<=>@#%&+"
            p = ""
            p = p.join([choice(valores) for i in range(long)])
            print(p)
        elif (mayus == "si" and caracter == "no"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            p = ""
            p = p.join([choice(valores) for i in range(long)])
            print(p)
        elif (mayus == "no" and caracter == "no"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyz"
            p = ""
            p = p.join([choice(valores) for i in range(long)])
            print(p)