# Menu con los puntos señalados en la actividad 2

from cola import Cola
from pila import Pila
from persona import Persona

cola = Cola()
pila = Pila()


def añadirRegistros(opcion):
    while True:
        codigo = int(input("Ingrese el codigo: "))
        nombre = input("Ingrese el nombre: ")
        telefono = int(input("Ingrese el telefono: "))
        edad = int(input("Ingrese la edad: "))

        nueva_perosna = Persona(codigo, nombre, telefono, edad)
        datosPersona = nueva_perosna.obtenerDatos()

        if opcion == 1:
            cola.insertar(datosPersona)
        elif opcion == 4:
            pila.apilar(datosPersona)

        respuesta = input("Desea agregar otro registro? (s/n): ")
        if respuesta.lower() == "n":
            break

def mostrarElementos(opcion):
    if opcion == 2:
        print(f"Elementos: {cola.obtenerElementos()}")
    elif opcion == 5:
        print(f"Elementos: {pila.obtenerElementos()}")

def eliminarElemento(opcion):
    if opcion == 3:
        print(f"Elemento eliminado: {cola.eliminar()}")
    elif opcion == 6:
        print(f"Elemento eliminado: {pila.desapilar()}")

def menuActividadDos():
    while True:
        print("\n// Actividad 2 //\n")

        print("Opciones para tipo (Cola)\n")
        print("1. Añadir elementos")
        print("2. Mostrar elementos")
        print("3. Eliminar elemento")

        print("\nOpciones para tipo (Pila)\n")
        print("4. Añadir elementos")
        print("5. Mostrar elementos")
        print("6. Eliminar elemento")

        print("\n7. Salir")

        opcion = int(input("\nElige una opcion: "))

        if opcion == 1 or opcion == 4:
            añadirRegistros(opcion)
        elif opcion == 2 or opcion == 5:
            mostrarElementos(opcion)
        elif opcion == 3 or opcion == 6:
            eliminarElemento(opcion)
        elif opcion == 7:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menuActividadDos()