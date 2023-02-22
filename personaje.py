class Personaje:
    
    #agregar constructor
    def __init__ (self, esp, nom, alt):
        self.especie = esp
        self.nombre = nom
        self.altura = alt
    
    #métodos
    def correr(self, status):
        if(status):
            print("El personaje " + self.nombre + " está corriendo.")
        else:
            print("El personaje " + self.nombre + " se detuvo.")
    
    def lanzarGranadas(self):
        print ("Se lanzó la granada.")
    
    def recargarArma(self, municiones):
        cargador = 10
        cargador = cargador + municiones
        print ("El arma recargada tiene " + str(cargador) + " balas")