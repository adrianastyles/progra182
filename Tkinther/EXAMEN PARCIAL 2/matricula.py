from tkinter import messagebox

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
        return self.__año[2], self.__año[3]
    
    def setAño (self, a):
        self.__año = a
        
    def getCarrera (self):
        return self.__carrera[0], self.__carrera[1], self.__carrera[2]
    
    def setCarrera (self, c):
        self.__carrera = c
        
    def getAñoCurso (self):
        return self.__añocurso
    