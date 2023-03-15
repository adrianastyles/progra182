from tkinter import messagebox

class GeneradorMatricula:
    
    def __init__ (self, n, ap, am, a, c):
        self.__nombre = n
        self.__apellidoPaterno = ap
        self.__apellidoMaterno = am
        self.__año = a
        self.__carrera = c
        self.__añocurso = 23
        
    def Generador1(self, nom, aPaterno, aMaterno, añoN, carrera2):
        nom = self.__nombre
        aPaterno = self.__apellidoPaterno
        aMaterno = self.__apellidoMaterno
        añoN= self.__año
        carrera2 = self.__carrera
        print (nom[1])
        print (aPaterno[1])
        print (aMaterno[1])
        print (añoN[1])
        print (carrera2[1])
        print(self.__añocurso)
            