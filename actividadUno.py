# Menu con los puntos señalados en la actividad 1

from cola import Cola
from pila import Pila

cola = Cola()
pila = Pila()


def añadirNumero(opcion):
    while True:
        numero = int(input("Ingrese un numero: "))

        if opcion == 1:
            cola.insertar(numero)
        elif opcion == 3:
            pila.apilar(numero)

        respuesta = input("Desea agregar otro numero? (s/n): ")
        if respuesta.lower() == "n":
            break

def mostrarElementosYResultados(opcion):
    if opcion == 2:
        print(f"Elementos: {cola.obtenerElementos()}")
        print(f"Cantidad de numeros pares: {cola.cantidadElementosPares()}")
        print(f"Promedio: {cola.promedioElementos()}")
        print(f"Último elemento: {cola.ultimoElemento()}")
    elif opcion == 4:
        print(f"Elementos: {pila.obtenerElementos()}")
        print(f"Cantidad de numeros pares: {pila.cantidadElementosPares()}")
        print(f"Promedio: {pila.promedioElementos()}")
        print(f"Último elemento: {pila.ultimoElemento()}")

def menuActividadUno():
    while True:
        print("\n// Actividad 1 //\n")

        print("Opciones para tipo (Cola)\n")
        print("1. Añadir elementos")
        print("2. Mostrar elementos y resultados")

        print("\nOpciones para tipo (Pila)\n")
        print("3. Añadir elementos")
        print("4. Mostrar elementos y resultados")

        print("\n5. Salir")

        opcion = int(input("\nElige una opcion: "))

        if opcion == 1 or opcion == 3:
            añadirNumero(opcion)
        elif opcion == 2 or opcion == 4:
            mostrarElementosYResultados(opcion)
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menuActividadUno()