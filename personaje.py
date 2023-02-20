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
    