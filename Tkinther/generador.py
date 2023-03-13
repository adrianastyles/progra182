from tkinter import messagebox
from random import choice

class Generador:
    
    def __init__ (self):
        self.__longitud = self
        self.__mayusculas = self
        self.__caracteres = self
    
        
    def Generador1(self):
        
        if (self.__mayusculas == "si" and self.__caracteres == "si"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
            p = ""
            p = p.join([choice(valores) for i in range(self.__longitud)])
            print(p)
        elif (self.__mayusculas == "no" and self.__caracteres == "si"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyz<=>@#%&+"
            p = ""
            p = p.join([choice(valores) for i in range(self.__longitud)])
            print(p)
        elif (self.__mayusculas == "si" and self.__caracteres == "no"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            p = ""
            p = p.join([choice(valores) for i in range(self.__longitud)])
            print(p)
        elif (self.__mayusculas == "no" and self.__caracteres == "no"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyz"
            p = ""
            p = p.join([choice(valores) for i in range(self.__longitud)])
            print(p)
      