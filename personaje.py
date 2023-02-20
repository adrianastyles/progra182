class Personaje:
    
    #atributos
    especie = "Humano"
    nombre = "Harry Styles"
    altura = 1.83
    
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
        print ("El arma recargada tiene " + cargador + " balas")