from tkinter import messagebox
import random
class GeneradorMatricula:
    
    def __init__ (self, n, ap, am, a, c):
        self.__nombre = n
        self.__apellidoPaterno = ap
        self.__apellidoMaterno = am
        self.__año = a
        self.__carrera = c
        self.__añocurso = 23

    def getNombre (self):
        return self.__nombre[0]
    
    def setNombre (self, n):
        self.__nombre = n
        
    def getApellidoP (self):
        return self.__apellidoPaterno[0]
    
    def setApellidoP (self, ap):
        self.__apellidoPaterno = ap
        
    def getApellidoM (self):
        return self.__apellidoMaterno[0]
    
    def setApellidoM (self, am):
        self.__apellidoMaterno = am
    
    def getAño (self):
        return self.__año[2]
    
    def getAño1 (self):
        return self.__año[3]
    
    def setAño (self, a):
        self.__año = a
        
    def getCarrera (self):
        return self.__carrera[0]
    
    def getCarrera1 (self):
        return self.__carrera[1]
    
    def getCarrera2 (self):
        return self.__carrera[2]
        
    def getAñoCurso (self):
        return self.__añocurso
    
    def getNumeros (self):
        valores = "0123456789"
        r = [random.choice(valores) for i in range(3)]
        return r
    