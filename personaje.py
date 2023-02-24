class Personaje:
    
    #agregar constructor
    
    def __init__ (self, esp, nom, alt):
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
    
    #métodos
    
    def correr(self, status):
        if(status):
            print("El personaje " + self.__nombre + " está corriendo.")
        else:
            print("El personaje " + self.__nombre + " se detuvo.")
    
    def lanzarGranadas(self):
        print ("Se lanzó la granada.")
    
    def recargarArma(self, municiones):
        cargador = 10
        cargador = cargador + municiones
        print ("El arma recargada tiene " + str(cargador) + " balas")