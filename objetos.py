from personaje import *

#instancia de la clase personaje
heroe = Personaje()

#usamos atributos
print("El personaje se llama " + heroe.nombre)
print("Pertenece a la especie " + heroe.especie)
print("Su altura es " + str(heroe.altura))

#usar los métodos

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(37)