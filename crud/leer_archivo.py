import csv
def leer_archivo(ruta):
 with open(ruta, newline='', encoding="utf8") as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)
