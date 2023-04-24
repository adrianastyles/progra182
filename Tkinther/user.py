from tkinter import messagebox

class User:
    
    def __init__(self, c, t, e):
        self.__cuenta= c
        self.__titular= t
        self.__edad = e
        
    def getCuenta(self):
        return self.__cuenta
    
    def getTitular(self):
        return self.__titular
    
    def getEdad(self):
        return self.__edad
    
