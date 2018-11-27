
def eliminar_de_archivo(ruta, dato):
    with open(ruta, "r") as input:
        with open("data\movies.csv", "w+") as output:
            for line in input:
                if line != dato + "\n":
                    output.write(line)
    input.close()
    output.close()