from tkinter import messagebox
from random import choice

class Generador:
    
    def __init__ (self, l, m, c):
        self.__longitud = l
        self.__mayusculas = m
        self.__caracteres = c
    
        
    def Generador1(self, long, mayus, caracter):
        long = self.__longitud
        mayus = self.__mayusculas
        caracter = self.__caracteres
        
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
            
    
    def getLongitud (self):
        return self.__longitud
    
    def setLongitud (self, l):
        self.__longitud = l
        
    def getMayusculas (self):
        return self.__mayusculas
    
    def setMayusculas (self, m):
        self.__mayusculas = m
    
    def getCaracteres (self):
        return self.__caracteres
    
    def setCaracteres (self, c):
        self.__caracteres = c