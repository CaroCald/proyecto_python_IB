def agregar_a_archivo(path, *lineas_a_escribir):
    try:
        archivo_abierto = open(path, "a")  # por defecto es la r -> read
        for linea in lineas_a_escribir:
            archivo_abierto.write("\n" + linea)

        archivo_abierto.close()
        return print('Ingresado con exito!')
    except Exception:
        return print("No se pudo leer")