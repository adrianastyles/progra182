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

heroe.setNombre("Louis")

#usamos atributos héroe y villano

print("\nHÉROE: \n")
print("El héroe se llama " + heroe.getNombre())
print("Pertenece a la especie " + heroe.getEspecie())
print("Su altura es " + str(heroe.getAltura()))
heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargaH)

print("\nVILLANO: \n")
print("El villano se llama " + villano.getNombre())
print("Pertenece a la especie " + villano.getEspecie())
print("Su altura es " + str(villano.getAltura()))
villano.correr(True)
villano.lanzarGranadas()
villano.recargarArma(recargaV)
#villano.__pensar()