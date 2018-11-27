from crud import leer_archivo
from crud import insertar_dato
from crud import modificar_archivo
from crud import eliminar_dato
from crud import sobre_escribir
ruta="data\movies.csv";


def registro_vuelos(opcion):
    def seleccion():
        if opcion == "1":
            leer_archivo.leer_archivo(ruta);
        elif opcion == "2":
            hora = input("ingrese hora ")
            insertar_dato.agregar_a_archivo(ruta, hora)
        elif opcion == "3":
            dato_anterior = input("Ingrese el dato que desea actualizar ")
            nuevo_dato = input("Ingrese el valor del dato que desea actualizar")
            modificar_archivo.actualizar_dato(nuevo_dato=nuevo_dato,dato=dato_anterior)
        elif opcion == "4":
            dato_a_eliminar = input("dato a eliminar")
            eliminar_dato.eliminar_de_archivo(ruta, dato_a_eliminar)
            sobre_escribir.sobre_escribir_archivo("./registro_vuelos_nuevo.txt")

    return seleccion();

while True:
    print("Ingrese una opcion: ")
    eleccion = input("\n 1. Consultar: \n 2. Insertar \n 3. Actualizar  \n 4. Eliminar \n 5. Salir")
    registro_vuelos(eleccion)
    if eleccion == "5":
        break
