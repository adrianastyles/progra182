from personaje import *

print ("SOLICITUD DE DATOS PARA EL HÉROE \n")

especieH = input("Escribe la especie del héroe: ")
nombreH = input("Escribe el nombre del héroe: ")
alturaH = float(input("Escribe la altura del héroe: "))
recargaH = int(input("Ingresa las balas para el héroe: "))

print ("SOLICITUD DE DATOS PARA EL VILLANO \n")

especieV = input("Escribe la especie del villano: ")
nombreV = input("Escribe el nombre del villano: ")
alturaV = float(input("Escribe la altura del villano: "))
recargaV = int(input("Ingresa las balas para el villano: "))

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