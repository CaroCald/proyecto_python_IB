from crud import leer_archivo
from crud import  insertar_dato
ruta="data\movies.csv";


def registro_vuelos(opcion):
    def seleccion():
        if opcion == "1":
            leer_archivo.leer_archivo(ruta);
        elif opcion == "2":
            hora = input("ingrese hora ")
            insertar_dato.agregar_a_archivo(ruta, hora)

    return seleccion();

while True:
    print("Ingrese una opcion: ")
    eleccion = input("\n 1. Consultar: \n 2. Insertar \n 3. Actualizar  \n 4. Eliminar \n 5. Salir")
    registro_vuelos(eleccion)
    if eleccion == "5":
        break
