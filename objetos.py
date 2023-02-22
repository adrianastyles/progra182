from personaje import *

print ("\nSOLICITUD DE DATOS PARA EL HÉROE \n")

especieH = input("Escribe la especie del héroe: ")
nombreH = input("Escribe el nombre del héroe: ")
alturaH = float(input("Escribe la altura del héroe: "))
recargaH = int(input("Ingresa las balas para el héroe: "))

print ("\nSOLICITUD DE DATOS PARA EL VILLANO \n")

especieV = input("Escribe la especie del villano: ")
nombreV = input("Escribe el nombre del villano: ")
alturaV = float(input("Escribe la altura del villano: "))
recargaV = int(input("Ingresa las balas para el villano: "))

#crear objetos
heroe = Personaje(especieH, nombreH, alturaH)
villano = Personaje(especieV, nombreV, alturaV)

#usamos atributos héroe y villano

print("\nHÉROE: \n")
print("El héroe se llama " + heroe.nombre)
print("Pertenece a la especie " + heroe.especie)
print("Su altura es " + str(heroe.altura))

print("\nVILLANO: \n")
print("El villano se llama " + villano.nombre)
print("Pertenece a la especie " + villano.especie)
print("Su altura es " + str(villano.altura) + "\n")

#usar los métodos

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(37)