"""
En primer lugar debemos de llevar a cabo el analisis de datos mediante python. 
Una vez introducidos los conceptos aplicables y que nos valdran para le tramtamiento de datasets 
(la mayoria de llos vendran en un formato conocido como CSV,Excel,JSON,XML).
Para ello vamos a dividir este articulo en los siguientes puntos que iremos explicando a continuacion:
1. Importacion de datos con Python.
2.

IMPORTACION DE DATOS CON PYTHON

Tenemos varios metodos para importar los datos desde fichero. El primero de los casos sera desde un fichero CSV.
Metodo de read_csv:
"""
import pandas as pd
import numpy as np
df = pd.read_csv(path) #este metodo tiene diferentes sobrecargas para poder trabajar con el. Nos devuelve una imagen de nuestro csv
#cargamos todos los datos en memoria del tiron sin iterear durante la carga.
type(df) # nos indicara que se trata de un dataframe, elemento clave en pandas. (Columnas y filas)
"""
Vamos a indicar las sobreacargas que soporta este comando de lectura de un fichero.
 - sep => nos permite indicar el tipo de separador de los valores alojados por columnas, por defecto python entiende este valor como ","
 - header => como valor predefinido vendra True, nos indica si nuestro fichero csv contiene cabeceras, podemos indicar que no tiene None.
 - dtype => valor predifinido de None, python importa los datos del csv y asigna el tipo de variable que le considera correcto. 
            Nosotros podemos imponer que tipo de variable recoge cada una de las columnas detype{"Columna1": np.float.64,"Columna2":np.int32}
            Estas columnas se cargaran con ese tipo de variable.
 - names => Lo empleamos para renombrar nuestras cabeceras, es decir nosotros imponemos los nombres de las cabeceras.
            names = {"Ingresos","Edad","Camisa"} los nombres de las columnas se cargan de atras, hacia delante, podemos pasar una lista 
            como parametro para que se cargue.
  - skiprows => nos permite saltarnos columnas que cargamos skiprows = 12
  - index_col => None por defecto, nos permite indicar que columna queremos que sea el indice, es decir el marcador. index_col = 2
  - skip_blank_lines = True, saltamos las columnas blancas, todos los NaN saldran en blanco.
  - na_filter => borra las lineas que tienen algun valor NaN. No es recomendable su empleo.
  - na_values => nos permite identificar otros caracteres que se clasificaran como NaN na_values=[""] - ahora las comillas seran tambien NaN
  - keep_default_na => es de tipo Boolean, y por defecto lleva True. Se convina con na_values y na_filter:
      . si keep_default_na = True y na_values tiene un valor asignado, el valor asignado se englobara en los NaN
      . si kee_default_na = True y na_values esta vacio, solo se parsean los NaN
      . si keep_default_na = False, y na_values tiene valor, solo los pasados como valor en na_values seran NaN
      . Si na_filter = Flase; los valores de keep_default_na y na_values son ignorados.
  
 Una vez cargado nuestro dataframe podemos ver las caracteristicas estadisticas mediante el uso de => df.describe() y mediante df.describe(all)

  df.describe {suma de valores(count), media de los valores, desviacion estandar(std),valores máximos y mínimos, valores porcentuales(25%,50%,75%)}
  df.describe(include= "all") aumenta  los parametros que salen con describe (top = objeto con mayor aparición,unique = número de objetos diferentes por cada columnas,
                              fres = número de veces que aparece el top en nuestra columna)
                              
  """
# Vamos a escribir un fichero csv con pandas
import pandas as pd
from pandas import DataFrame
Data = {'Columna1':['Python','C#','Java','Ruby'],'Columna2':['Medio','Desarrollo Web','Complicado','Antiguo']}
df = DataFrame(Data,columnas=['Columna1','Columna2'])
export_csv = df.to_csv(path_donde_escribir,index=None,header=True)
#Ya tendriamos nuestro fichero creado, no tiene porque existir previamente ya que Python lo crea por nosotros.




#METODO DE CARGA OPEN Y CSV. Metodo mas empleado para la carga de datos, nos permite iterar a traves de las lineas
#pudiendo elegir cuales son las que queremos emplear o cuales no.
#Lo bueno de los metodos With open, es que una vez trabajado sobre la linea, esta se libera de memoria.
import csv 
import pandas as pd
import numpy as np

with open(path,encoding ='latin1') as fichero_csv:
  lector = csv.reader(fichero_csv)
  next(lector,None) #Nos saltamos la primera fila ya que se trata de las cabeceras
  for linea in lector:
    valor_str = linea[2] #tambien podriamos poner linea['Nombre Columna que queremos cargar"]
    
  #Ahora mismo ya tendriamos abierto nuestro fichero path y lo recorremos linea por linea mediante un bucle for.
  contador = 0
  with open(path) as fichero_csv:
  lector = csv.reader(fichero_csv)
  next(lector,None)
  for linea in lector:
    linea_str = linea[2]
      if linea_str == 'alfa-romero':
        vector_coches[contador] = linea_str
        contador+=1

""" 
Debemos de mencionar que esta manera de recorrer un Data Frame no es la manera mas correcta de hacarlo, si miramos desde el punto de vista del
tiempo de ejecución, cuando tengamos un DataFrame con muchas filas, tardará un tiempo elevado.
En un siguiente post veremos el metodo idoneo de recorrer lineas y columnas de un DataFrame para interactuar con el.

El paquete csv tiene mas metodos a parte del csv.reader, comentaremos algún interesante:

  - csv.writer => para escribir datos en un fichero csv.writer(path,dialect='excel'...)
  - csv.DicReader ==> se explicara con un ejemplo a continuacion
  - csv.DicWriter => Para poder escribir en un fichero.
  - csv.Sniffer => Para deducir el tipo de fichero csv, el cual tiene dos metodos:
      dialect = csv.Sniffer().sniff(fichero_csv.read(1024)
      fichero_csv.seek(0)
      reader = csv.reader(fichero_csv,dialect)
  
  Tenemos que mencionar tambien la sobrecarga "quoting", nos permite determinar el entrecomillado, podemos indicar que valores 
  van a ir entrecomillados.
  ===> csv.reader(fichero_csv,delimeter =",",quoting =csv.QUOTE_NONE)
  podemos indicar tambien:
    - csv.QUOTE_NONE = ningun valor se entrecomilla
    - csv.QUOTE_NONNUMERIC = valores que no son númericos.
    - csv.QUOTE_MINIMAL = para aquellos que contienen caracteres especiales.
    - csv.QUOTE_ALL = todos los valores se entrecomillan.

Los dialectos son los elementos que nos permiten delimitar nuestro fichero cuando no  tenemos comillas,etc
Podemos registrar nuevos dialectos en el lector csv
  import csv
  csv.register_dialect('nombre que le damos',"?") ? => es la variable que vamos a usar para delimitar
    with open(fichero_csv,'r',new line = '') as fichero:
      reader = csv.reader(fichero,dialect= 'nombre del dialecto')
        try:
          for row in reader:
            print(row)
         except csv.Error as e:
         ys.exit('file {}, line {}: {}'.format(fichero_csv, reader.line_num, e))
    
  
"""
#USO DE DICTREADER

with open(path, 
