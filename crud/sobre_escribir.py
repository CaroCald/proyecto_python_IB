
pathArchivo = "data\movies.csv"
def sobre_escribir_archivo(ruta):
    with open(ruta, "r") as input:
        with open(pathArchivo, "w+") as output:
            for line in input:
                output.write(line)
    input.close()
    output.close()
