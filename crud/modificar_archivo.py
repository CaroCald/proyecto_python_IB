
import pandas as pd
pathArchivo = "data/movies.csv"


def actualizar_dato(nuevo_dato, dato):
   filename = "data/movies.csv"
   valin = ""+dato
   valout = ""+nuevo_dato
   df = pd.read_csv(filename)

   try:
       df.loc[df['director_name'] == valin, "director_name"] = valout
       df.to_csv(filename)
       return print("Dato actualizado con exito!!!");
   except KeyError:
       pass